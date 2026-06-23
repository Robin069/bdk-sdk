# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import CriticalDataElementsOperations  # type: ignore
from ._operations import DataAssetsOperations  # type: ignore
from ._operations import DataProductsOperations  # type: ignore
from ._operations import BusinessDomainOperations  # type: ignore
from ._operations import TermsOperations  # type: ignore
from ._operations import OkrOperations  # type: ignore
from ._operations import PoliciesOperations  # type: ignore
from ._operations import DataColumnsOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CriticalDataElementsOperations",
    "DataAssetsOperations",
    "DataProductsOperations",
    "BusinessDomainOperations",
    "TermsOperations",
    "OkrOperations",
    "PoliciesOperations",
    "DataColumnsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
