"""Convert Swagger 2.0 definitions to OpenAPI 3.0 components/schemas.

Usage:
    python3 scripts/convert_swagger_to_oas3.py \\
      api-specs/.../scanningService.json \\
      /tmp/oas3_spec.json

Converts:
  - definitions → components/schemas
  - $ref paths from #/definitions/X → #/components/schemas/X
  - Flattens allOf chains into single schemas
  - Converts discriminator + x-ms-discriminator-value → oneOf with discriminator
"""

from __future__ import annotations

import copy
import json
import sys
from collections import defaultdict


def fix_refs(obj, from_prefix="#/definitions/", to_prefix="#/components/schemas/"):
    """Recursively update $ref paths."""
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str) and v.startswith(from_prefix):
                result[k] = to_prefix + v[len(from_prefix) :]
            else:
                result[k] = fix_refs(v, from_prefix, to_prefix)
        return result
    elif isinstance(obj, list):
        return [fix_refs(item, from_prefix, to_prefix) for item in obj]
    return obj


def deep_merge(base, override):
    """Deep merge two dicts."""
    result = copy.deepcopy(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        elif k in result and isinstance(result[k], list) and isinstance(v, list):
            result[k] = result[k] + v
        else:
            result[k] = v
    return result


def merge_all_of(schema, defs, visited=None):
    """Merge an allOf chain into a single schema with updated $ref paths."""
    if visited is None:
        visited = set()
    merged = {}
    if "allOf" in schema:
        for item in schema["allOf"]:
            if "$ref" in item:
                ref_name = item["$ref"].split("/")[-1]
                if ref_name in visited:
                    continue
                if ref_name in defs:
                    visited.add(ref_name)
                    resolved = fix_refs(defs[ref_name])
                    sub_merged = merge_all_of(resolved, defs, visited)
                    merged = deep_merge(merged, sub_merged)
            else:
                merged = deep_merge(merged, fix_refs(item))
    own = {
        k: fix_refs(v)
        for k, v in schema.items()
        if k not in ("allOf", "x-ms-discriminator-value", "discriminator")
    }
    merged = deep_merge(merged, own)
    return merged


def convert(swagger_path: str, output_path: str) -> None:
    """Main conversion function."""
    with open(swagger_path) as f:
        swagger = json.load(f)

    definitions = swagger.get("definitions", {})

    # --- Classify definitions ---
    discriminated_parents = {}
    discriminated_children = defaultdict(list)

    for name, schema in definitions.items():
        if not isinstance(schema, dict):
            continue
        if "discriminator" in schema:
            discriminated_parents[name] = schema["discriminator"]
        if "x-ms-discriminator-value" in schema:
            for ref_obj in schema.get("allOf", []):
                if "$ref" in ref_obj:
                    ref_name = ref_obj["$ref"].split("/")[-1]
                    if ref_name in discriminated_parents:
                        discriminated_children[ref_name].append(
                            (name, schema["x-ms-discriminator-value"])
                        )

    oas3_schemas = {}
    all_child_names = {
        c[0] for children in discriminated_children.values() for c in children
    }

    # Pass 1: Simple definitions (no discriminator, not a child)
    for name, schema in definitions.items():
        if not isinstance(schema, dict):
            oas3_schemas[name] = schema
            continue
        if name in discriminated_parents or name in all_child_names:
            continue
        if "allOf" not in schema:
            oas3_schemas[name] = fix_refs(copy.deepcopy(schema))
        else:
            merged = fix_refs(merge_all_of(schema, definitions))
            oas3_schemas[name] = merged

    # Pass 2: Discriminated parents → oneOf
    for parent_name, discriminator_prop in discriminated_parents.items():
        children = discriminated_children.get(parent_name, [])
        if not children:
            merged = fix_refs(merge_all_of(definitions[parent_name], definitions))
            oas3_schemas[parent_name] = merged
            continue

        one_of_refs = []
        mapping = {}
        for child_name, disc_value in children:
            mapping[disc_value] = f"#/components/schemas/{child_name}"
            one_of_refs.append({"$ref": f"#/components/schemas/{child_name}"})

        oas3_schemas[parent_name] = {
            "oneOf": one_of_refs,
            "discriminator": {"propertyName": discriminator_prop, "mapping": mapping},
        }

    # Pass 3: Discriminated children → flat schemas with const discriminator
    for parent_name, children in discriminated_children.items():
        discriminator_prop = discriminated_parents[parent_name]
        for child_name, disc_value in children:
            child_def = definitions[child_name]
            merged = fix_refs(merge_all_of(child_def, definitions))

            if discriminator_prop not in merged.get("properties", {}):
                merged.setdefault("properties", {})[discriminator_prop] = {
                    "const": disc_value
                }

            merged.setdefault("required", [])
            if discriminator_prop not in merged["required"]:
                merged["required"].append(discriminator_prop)

            oas3_schemas[child_name] = merged

    # Build OAS 3.0 document
    oas3 = {
        "openapi": "3.0.0",
        "info": swagger.get("info", {"title": "Converted", "version": "1.0.0"}),
        "paths": {},
        "components": {"schemas": oas3_schemas},
    }

    with open(output_path, "w") as f:
        json.dump(oas3, f, indent=2)

    print(
        f"Converted {len(oas3_schemas)} schemas "
        f"({len(discriminated_parents)} discriminated parents, "
        f"{sum(len(v) for v in discriminated_children.values())} children) "
        f"→ {output_path}"
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <swagger_2.0.json> <oas3_output.json>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
