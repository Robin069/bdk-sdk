from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, model_validator

from ._generated.scanning import DataSource


class DataSourceSpec(BaseModel):
    """YAML-friendly data source specification.

    Accepts a flat dict::

        {"name": "my-ds", "kind": "AdlsGen2", "properties": {"endpoint": "..."}}

    The ``name`` field is used as the URL path key and is excluded from the
    API request body.  Validation of the kind-specific structure is delegated
    to the generated ``DataSource`` discriminated union.
    """

    name: str = Field(description="Data source name used as the URL path key")
    data_source: DataSource = Field(
        description="The data source body, validated via the kind discriminated union"
    )

    @model_validator(mode="before")
    @classmethod
    def _extract_name(cls, data: Any) -> Any:
        if isinstance(data, dict) and "data_source" not in data:
            data = dict(data)  # don't mutate the caller's dict
            name = data.pop("name", None)
            if name is None:
                raise ValueError("name is required")
            data_source = DataSource.model_validate(data)
            return {"name": name, "data_source": data_source}
        return data

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        """Serialize to the API request body: the data source only (no ``name``)."""
        kwargs.setdefault("by_alias", True)
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("exclude_unset", True)
        return self.data_source.model_dump(**kwargs)
