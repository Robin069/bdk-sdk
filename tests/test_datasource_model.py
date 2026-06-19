"""Tests for ``bdk_sdk.models.datasource.DataSourceSpec``."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from bdk_sdk.models.datasource import DataSourceSpec


class TestDataSourceSpec:
    """DataSourceSpec validation and serialization."""

    _VALID = {
        "name": "my-ds",
        "kind": "AdlsGen2",
        "properties": {
            "endpoint": "https://example.dfs.core.windows.net/",
            "collection": {"referenceName": "Collection-xyz"},
        },
    }

    def test_valid_minimal_spec(self):
        spec = DataSourceSpec.model_validate(self._VALID)
        assert spec.name == "my-ds"
        assert spec.data_source.root.kind == "AdlsGen2"

    def test_name_required(self):
        with pytest.raises(ValidationError) as exc:
            DataSourceSpec.model_validate({"kind": "AdlsGen2", "properties": {}})
        assert "name is required" in str(exc.value)

    def test_kind_required(self):
        with pytest.raises(ValidationError) as exc:
            DataSourceSpec.model_validate({"name": "x", "properties": {"endpoint": "https://e"}})
        assert "kind" in str(exc.value).lower() or "validation error" in str(exc.value).lower()

    def test_invalid_kind_raises(self):
        with pytest.raises(ValidationError):
            DataSourceSpec.model_validate({"name": "x", "kind": "NotARealKind", "properties": {}})

    def test_model_dump_excludes_name_and_readonly(self):
        spec = DataSourceSpec.model_validate(self._VALID)
        dumped = spec.model_dump()

        assert "name" not in dumped
        assert "kind" in dumped
        assert dumped["kind"] == "AdlsGen2"
        assert "properties" in dumped
        assert dumped["properties"]["endpoint"] == "https://example.dfs.core.windows.net/"

    def test_model_dump_excludes_none(self):
        spec = DataSourceSpec.model_validate(
            {"name": "x", "kind": "AdlsGen2", "properties": {"endpoint": "https://e"}}
        )
        dumped = spec.model_dump()

        assert "id" not in dumped
        assert "scans" not in dumped
        assert "creationType" not in dumped

    def test_non_dict_input_passes_through(self):
        # Test that model_validate with "data_source" already present works
        from bdk_sdk.models._generated.scanning import AdlsGen2DataSource

        inner = AdlsGen2DataSource(
            kind="AdlsGen2",
            properties={"endpoint": "https://e"},
        )
        spec = DataSourceSpec.model_validate({"name": "x2", "data_source": inner})
        assert spec.name == "x2"
        assert spec.data_source.root.kind == "AdlsGen2"

    def test_azure_storage_kind(self):
        """Verify that AzureStorage kind is valid (from the example)."""
        spec = DataSourceSpec.model_validate(
            {
                "name": "my-storage",
                "kind": "AzureStorage",
                "properties": {
                    "endpoint": "https://azurestorage.core.windows.net/",
                    "collection": {"referenceName": "Collection-rZX"},
                },
            }
        )
        dumped = spec.model_dump()
        assert dumped["kind"] == "AzureStorage"
        assert dumped["properties"]["endpoint"] == "https://azurestorage.core.windows.net/"
