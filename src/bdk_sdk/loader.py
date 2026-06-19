from __future__ import annotations

from pathlib import Path
from typing import TypeVar

import yaml
from pydantic import BaseModel

M = TypeVar("M", bound=BaseModel)


def load_spec(path: str | Path, model: type[M]) -> M:
    """Load a YAML file and validate it as the given pydantic model."""
    with open(path) as f:
        data = yaml.safe_load(f)
    return model.model_validate(data)
