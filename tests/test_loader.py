"""Tests for ``bdk_sdk.loader.load_spec``."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from pydantic import BaseModel, Field

from bdk_sdk.loader import load_spec


class _SampleModel(BaseModel):
    name: str
    value: int = Field(default=42)


class TestLoadSpec:
    def test_loads_yaml_and_validates(self, tmp_path: Path):
        spec_path = tmp_path / "spec.yaml"
        spec_path.write_text("name: hello\nvalue: 99\n")

        result = load_spec(spec_path, _SampleModel)

        assert isinstance(result, _SampleModel)
        assert result.name == "hello"
        assert result.value == 99

    def test_uses_defaults_when_missing(self, tmp_path: Path):
        spec_path = tmp_path / "spec.yaml"
        spec_path.write_text("name: hello\n")

        result = load_spec(spec_path, _SampleModel)
        assert result.value == 42

    def test_raises_on_validation_error(self, tmp_path: Path):
        spec_path = tmp_path / "spec.yaml"
        spec_path.write_text("name: 123\n")  # value should be int, name should be str

        # name can coerce int to str, so this might pass. Let's test missing required:
        spec_path.write_text("value: 1\n")

        with pytest.raises(Exception):  # pydantic ValidationError
            load_spec(spec_path, _SampleModel)

    def test_raises_on_missing_file(self, tmp_path: Path):
        with pytest.raises(FileNotFoundError):
            load_spec(tmp_path / "nonexistent.yaml", _SampleModel)


class TestLoadSpecWithDataSourceSpec:
    """Integration test with DataSourceSpec."""

    def test_loads_valid_datasource_yaml(self, tmp_path: Path):
        from bdk_sdk.models.datasource import DataSourceSpec

        spec_path = tmp_path / "ds.yaml"
        spec_path.write_text(
            yaml.dump(
                {
                    "name": "my-adls",
                    "kind": "AdlsGen2",
                    "properties": {
                        "endpoint": "https://example.dfs.core.windows.net/",
                        "collection": {"referenceName": "Collection-abc"},
                    },
                }
            )
        )

        result = load_spec(spec_path, DataSourceSpec)

        assert result.name == "my-adls"
        body = result.model_dump()
        assert body["kind"] == "AdlsGen2"
        assert body["properties"]["endpoint"] == "https://example.dfs.core.windows.net/"
