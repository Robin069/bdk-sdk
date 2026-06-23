# pylint: disable=too-many-lines
# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, IO, Optional, TypeVar, Union, overload
import urllib.parse

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.paging import ItemPaged
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._configuration import PurviewUnifiedCatalogClientConfiguration
from .._utils.model_base import SdkJSONEncoder, _deserialize
from .._utils.serialization import Deserializer, Serializer

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, dict[str, Any]], Any]]
List = list

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_critical_data_elements_list_request(  # pylint: disable=name-too-long
    *,
    domain_id: Optional[str] = None,
    keyword: Optional[str] = None,
    order_by: Optional[str] = None,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if domain_id is not None:
        _params["domainId"] = _SERIALIZER.query("domain_id", domain_id, "str")
    if keyword is not None:
        _params["keyword"] = _SERIALIZER.query("keyword", keyword, "str")
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_create_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_get_request(critical_data_element_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_update_request(  # pylint: disable=name-too-long
    critical_data_element_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_delete_request(  # pylint: disable=name-too-long
    critical_data_element_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_critical_data_elements_list_relationships_request(  # pylint: disable=name-too-long
    critical_data_element_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}/relationships"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_create_relationship_request(  # pylint: disable=name-too-long
    critical_data_element_id: str, *, entity_type: Optional[Union[str, _models.EntityCategory]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}/relationships"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_delete_relationship_request(  # pylint: disable=name-too-long
    critical_data_element_id: str,
    *,
    entity_type: Optional[Union[str, _models.EntityCategory]] = None,
    entity_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/criticalDataElements/{criticalDataElementId}/relationships"
    path_format_arguments = {
        "criticalDataElementId": _SERIALIZER.url("critical_data_element_id", critical_data_element_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    if entity_id is not None:
        _params["entityId"] = _SERIALIZER.query("entity_id", entity_id, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_critical_data_elements_query_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_get_facets_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/facets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_critical_data_elements_count_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/criticalDataElements/query/count"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_list_request(
    *,
    include_extended_properties: bool,
    order_by: Optional[str] = None,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["includeExtendedProperties"] = _SERIALIZER.query(
        "include_extended_properties", include_extended_properties, "bool"
    )
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_query_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_get_by_id_request(
    data_asset_id: str, *, include_extended_properties: bool, include_lineage: bool, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets/{dataAssetId}"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["includeExtendedProperties"] = _SERIALIZER.query(
        "include_extended_properties", include_extended_properties, "bool"
    )
    _params["includeLineage"] = _SERIALIZER.query("include_lineage", include_lineage, "bool")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_update_request(data_asset_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets/{dataAssetId}"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_delete_by_id_request(data_asset_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/dataAssets/{dataAssetId}"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_data_assets_list_relationships_request(  # pylint: disable=name-too-long
    data_asset_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets/{dataAssetId}/relationships"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_create_relationship_request(  # pylint: disable=name-too-long
    data_asset_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataAssets/{dataAssetId}/relationships"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_assets_delete_relationship_request(  # pylint: disable=name-too-long
    data_asset_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/dataAssets/{dataAssetId}/relationships"
    path_format_arguments = {
        "dataAssetId": _SERIALIZER.url("data_asset_id", data_asset_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    _params["entityId"] = _SERIALIZER.query("entity_id", entity_id, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_data_products_list_request(
    *,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    domain_id: Optional[str] = None,
    order_by: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if domain_id is not None:
        _params["domainId"] = _SERIALIZER.query("domain_id", domain_id, "str")
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_query_request(*, data_product_owner: Optional[bool] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if data_product_owner is not None:
        _params["dataProductOwner"] = _SERIALIZER.query("data_product_owner", data_product_owner, "bool")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_get_facets_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/facets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_get_request(data_product_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/{dataProductId}"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_update_request(data_product_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/{dataProductId}"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_delete_request(data_product_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/dataProducts/{dataProductId}"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_data_products_list_relationships_request(  # pylint: disable=name-too-long
    data_product_id: str, *, entity_type: Optional[Union[str, _models.EntityCategory]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/{dataProductId}/relationships"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_create_relationship_request(  # pylint: disable=name-too-long
    data_product_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/{dataProductId}/relationships"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_products_delete_relationship_request(  # pylint: disable=name-too-long
    data_product_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/dataProducts/{dataProductId}/relationships"
    path_format_arguments = {
        "dataProductId": _SERIALIZER.url("data_product_id", data_product_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    _params["entityId"] = _SERIALIZER.query("entity_id", entity_id, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_data_products_count_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataProducts/query/count"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_business_domain_enumerate_request(
    *, skip_token: Optional[str] = None, write_only: Optional[bool] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/businessdomains"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip_token is not None:
        _params["$skipToken"] = _SERIALIZER.query("skip_token", skip_token, "str")
    if write_only is not None:
        _params["writeOnly"] = _SERIALIZER.query("write_only", write_only, "bool")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_business_domain_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/businessdomains"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_business_domain_update_request(domain_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/businessdomains/{domainId}"
    path_format_arguments = {
        "domainId": _SERIALIZER.url("domain_id", domain_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_business_domain_get_request(domain_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/businessdomains/{domainId}"
    path_format_arguments = {
        "domainId": _SERIALIZER.url("domain_id", domain_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_business_domain_delete_request(domain_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/businessdomains/{domainId}"
    path_format_arguments = {
        "domainId": _SERIALIZER.url("domain_id", domain_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_terms_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_list_request(
    *,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    domain_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    keyword: Optional[str] = None,
    depth: Optional[int] = None,
    order_by: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if domain_id is not None:
        _params["domainId"] = _SERIALIZER.query("domain_id", domain_id, "str")
    if parent_id is not None:
        _params["parentId"] = _SERIALIZER.query("parent_id", parent_id, "str")
    if keyword is not None:
        _params["keyword"] = _SERIALIZER.query("keyword", keyword, "str")
    if depth is not None:
        _params["depth"] = _SERIALIZER.query("depth", depth, "int")
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_update_request(term_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/{termId}"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_get_request(term_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/{termId}"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_delete_request(term_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/terms/{termId}"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_terms_query_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_get_facets_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/facets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_list_hierarchy_request(term_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/{termId}/hierarchies"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_add_related_entity_request(
    term_id: str, *, entity_type: Optional[Union[str, _models.EntityCategory]] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/{termId}/relationships"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_delete_related_request(
    term_id: str,
    *,
    entity_type: Optional[Union[str, _models.EntityCategory]] = None,
    relationship_type: Optional[Union[str, _models.TermRelationshipType]] = None,
    entity_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/terms/{termId}/relationships"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    if relationship_type is not None:
        _params["relationshipType"] = _SERIALIZER.query("relationship_type", relationship_type, "str")
    if entity_id is not None:
        _params["entityId"] = _SERIALIZER.query("entity_id", entity_id, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_terms_list_related_entities_request(  # pylint: disable=name-too-long
    term_id: str,
    *,
    entity_type: Optional[Union[str, _models.EntityCategory]] = None,
    relationship_type: Optional[Union[str, _models.TermRelationshipType]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/{termId}/relationships"
    path_format_arguments = {
        "termId": _SERIALIZER.url("term_id", term_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if entity_type is not None:
        _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    if relationship_type is not None:
        _params["relationshipType"] = _SERIALIZER.query("relationship_type", relationship_type, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_terms_count_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/terms/query/count"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_list_request(
    *,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    keyword: Optional[str] = None,
    domain_id: Optional[str] = None,
    order_by: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip is not None:
        _params["skip"] = _SERIALIZER.query("skip", skip, "int")
    if top is not None:
        _params["top"] = _SERIALIZER.query("top", top, "int")
    if keyword is not None:
        _params["keyword"] = _SERIALIZER.query("keyword", keyword, "str")
    if domain_id is not None:
        _params["domainId"] = _SERIALIZER.query("domain_id", domain_id, "str")
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_query_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_get_facets_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/facets"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_update_request(objective_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_delete_request(objective_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/objectives/{objectiveId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_okr_get_request(objective_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_list_key_results_request(objective_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}/keyResults"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_create_key_result_request(objective_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}/keyResults"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_get_key_result_request(objective_id: str, key_result_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}/keyResults/{keyResultId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
        "keyResultId": _SERIALIZER.url("key_result_id", key_result_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_update_key_result_request(objective_id: str, key_result_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/{objectiveId}/keyResults/{keyResultId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
        "keyResultId": _SERIALIZER.url("key_result_id", key_result_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_okr_delete_key_result_request(objective_id: str, key_result_id: str, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/objectives/{objectiveId}/keyResults/{keyResultId}"
    path_format_arguments = {
        "objectiveId": _SERIALIZER.url("objective_id", objective_id, "str"),
        "keyResultId": _SERIALIZER.url("key_result_id", key_result_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_okr_count_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/objectives/query/count"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_policies_list_request(*, skip_token: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/policies"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip_token is not None:
        _params["skipToken"] = _SERIALIZER.query("skip_token", skip_token, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_policies_update_request(policy_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/policies/{policyId}"
    path_format_arguments = {
        "policyId": _SERIALIZER.url("policy_id", policy_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_get_request(
    id: str,
    *,
    include_column_details: Optional[bool] = None,
    include_asset_details: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataColumns/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if include_column_details is not None:
        _params["includeColumnDetails"] = _SERIALIZER.query("include_column_details", include_column_details, "bool")
    if include_asset_details is not None:
        _params["includeAssetDetails"] = _SERIALIZER.query("include_asset_details", include_asset_details, "bool")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_ingest_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataColumns/ingest"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_query_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataColumns/query"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_list_related_entities_request(  # pylint: disable=name-too-long
    data_column_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataColumns/{dataColumnId}/relationships"
    path_format_arguments = {
        "dataColumnId": _SERIALIZER.url("data_column_id", data_column_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_add_related_entity_request(  # pylint: disable=name-too-long
    data_column_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/dataColumns/{dataColumnId}/relationships"
    path_format_arguments = {
        "dataColumnId": _SERIALIZER.url("data_column_id", data_column_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_data_columns_delete_related_request(  # pylint: disable=name-too-long
    data_column_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2026-03-20-preview"))
    # Construct URL
    _url = "/dataColumns/{dataColumnId}/relationships"
    path_format_arguments = {
        "dataColumnId": _SERIALIZER.url("data_column_id", data_column_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["entityType"] = _SERIALIZER.query("entity_type", entity_type, "str")
    _params["entityId"] = _SERIALIZER.query("entity_id", entity_id, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


class CriticalDataElementsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`critical_data_elements` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(
        self,
        *,
        domain_id: Optional[str] = None,
        keyword: Optional[str] = None,
        order_by: Optional[str] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.CriticalDataElement"]:
        """Searches and retrieves critical data elements based on domain, keyword, and other filters. Rate
        limit: 100 requests per 20-second window.

        :keyword domain_id: Whether to return minimal information for referred Domains. Default value
         is None.
        :paramtype domain_id: str
        :keyword keyword: Search keyword. Default value is None.
        :paramtype keyword: str
        :keyword order_by: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype order_by: str
        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :return: An iterator like instance of CriticalDataElement
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CriticalDataElement]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.CriticalDataElement]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_critical_data_elements_list_request(
                    domain_id=domain_id,
                    keyword=keyword,
                    order_by=order_by,
                    skip=skip,
                    top=top,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.CriticalDataElement],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create(
        self,
        critical_data_element: _models.CriticalDataElement,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Creates a new critical data element in the catalog. Rate limit: 200 requests per 20-second
        window.

        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: ~purviewunifiedcatalog.models.CriticalDataElement
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, critical_data_element: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Creates a new critical data element in the catalog. Rate limit: 200 requests per 20-second
        window.

        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, critical_data_element: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Creates a new critical data element in the catalog. Rate limit: 200 requests per 20-second
        window.

        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(
        self, critical_data_element: Union[_models.CriticalDataElement, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Creates a new critical data element in the catalog. Rate limit: 200 requests per 20-second
        window.

        :param critical_data_element: the critical data element to update. Is one of the following
         types: CriticalDataElement, JSON, IO[bytes] Required.
        :type critical_data_element: ~purviewunifiedcatalog.models.CriticalDataElement or JSON or
         IO[bytes]
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CriticalDataElement] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(critical_data_element, (IOBase, bytes)):
            _content = critical_data_element
        else:
            _content = json.dumps(critical_data_element, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_critical_data_elements_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CriticalDataElement, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get(self, critical_data_element_id: str, **kwargs: Any) -> _models.CriticalDataElement:
        """Searches and retrieves critical data elements based on Id. Rate limit: 1,500 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CriticalDataElement] = kwargs.pop("cls", None)

        _request = build_critical_data_elements_get_request(
            critical_data_element_id=critical_data_element_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CriticalDataElement, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self,
        critical_data_element_id: str,
        critical_data_element: _models.CriticalDataElement,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Updates an existing critical data element in the catalog. Rate limit: 150 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: ~purviewunifiedcatalog.models.CriticalDataElement
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        critical_data_element_id: str,
        critical_data_element: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Updates an existing critical data element in the catalog. Rate limit: 150 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        critical_data_element_id: str,
        critical_data_element: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Updates an existing critical data element in the catalog. Rate limit: 150 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param critical_data_element: the critical data element to update. Required.
        :type critical_data_element: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(
        self,
        critical_data_element_id: str,
        critical_data_element: Union[_models.CriticalDataElement, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.CriticalDataElement:
        """Updates an existing critical data element in the catalog. Rate limit: 150 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param critical_data_element: the critical data element to update. Is one of the following
         types: CriticalDataElement, JSON, IO[bytes] Required.
        :type critical_data_element: ~purviewunifiedcatalog.models.CriticalDataElement or JSON or
         IO[bytes]
        :return: CriticalDataElement. The CriticalDataElement is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CriticalDataElement
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CriticalDataElement] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(critical_data_element, (IOBase, bytes)):
            _content = critical_data_element
        else:
            _content = json.dumps(critical_data_element, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_critical_data_elements_update_request(
            critical_data_element_id=critical_data_element_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CriticalDataElement, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(  # pylint: disable=inconsistent-return-statements
        self, critical_data_element_id: str, **kwargs: Any
    ) -> None:
        """Deletes an existing critical data element in the catalog. Rate limit: 80 requests per 20-second
        window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_critical_data_elements_delete_request(
            critical_data_element_id=critical_data_element_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def list_relationships(
        self, critical_data_element_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
    ) -> ItemPaged["_models.CdeRelationship"]:
        """Lists relationships for the specified CDE and entity category. Rate limit: 1,500 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :keyword entity_type: The body associated with the critical data element output. Known values
         are: "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT",
         "CRITICALDATAELEMENT", "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE",
         "WORKFLOW", "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: An iterator like instance of CdeRelationship
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CdeRelationship]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.CdeRelationship]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_critical_data_elements_list_relationships_request(
                    critical_data_element_id=critical_data_element_id,
                    entity_type=entity_type,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.CdeRelationship],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create_relationship(
        self,
        critical_data_element_id: str,
        relationship: _models.DataElementProperties,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CdeRelationshipWithSystemData:
        """Creates a relationship between the specified CDE and another entity. Rate limit: 200 requests
        per 20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param relationship: The input properties for creating the relationship. Required.
        :type relationship: ~purviewunifiedcatalog.models.DataElementProperties
        :keyword entity_type: The type of entity for the relationship. Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CdeRelationshipWithSystemData. The CdeRelationshipWithSystemData is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CdeRelationshipWithSystemData
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        critical_data_element_id: str,
        relationship: JSON,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CdeRelationshipWithSystemData:
        """Creates a relationship between the specified CDE and another entity. Rate limit: 200 requests
        per 20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param relationship: The input properties for creating the relationship. Required.
        :type relationship: JSON
        :keyword entity_type: The type of entity for the relationship. Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CdeRelationshipWithSystemData. The CdeRelationshipWithSystemData is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CdeRelationshipWithSystemData
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        critical_data_element_id: str,
        relationship: IO[bytes],
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CdeRelationshipWithSystemData:
        """Creates a relationship between the specified CDE and another entity. Rate limit: 200 requests
        per 20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param relationship: The input properties for creating the relationship. Required.
        :type relationship: IO[bytes]
        :keyword entity_type: The type of entity for the relationship. Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CdeRelationshipWithSystemData. The CdeRelationshipWithSystemData is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CdeRelationshipWithSystemData
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create_relationship(
        self,
        critical_data_element_id: str,
        relationship: Union[_models.DataElementProperties, JSON, IO[bytes]],
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        **kwargs: Any
    ) -> _models.CdeRelationshipWithSystemData:
        """Creates a relationship between the specified CDE and another entity. Rate limit: 200 requests
        per 20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :param relationship: The input properties for creating the relationship. Is one of the
         following types: DataElementProperties, JSON, IO[bytes] Required.
        :type relationship: ~purviewunifiedcatalog.models.DataElementProperties or JSON or IO[bytes]
        :keyword entity_type: The type of entity for the relationship. Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: CdeRelationshipWithSystemData. The CdeRelationshipWithSystemData is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CdeRelationshipWithSystemData
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CdeRelationshipWithSystemData] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(relationship, (IOBase, bytes)):
            _content = relationship
        else:
            _content = json.dumps(relationship, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_critical_data_elements_create_relationship_request(
            critical_data_element_id=critical_data_element_id,
            entity_type=entity_type,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CdeRelationshipWithSystemData, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_relationship(  # pylint: disable=inconsistent-return-statements
        self,
        critical_data_element_id: str,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        entity_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a relationship between the CDE and the specified entity. Rate limit: 80 requests per
        20-second window.

        :param critical_data_element_id: The unique identifier of the critical data element. Required.
        :type critical_data_element_id: str
        :keyword entity_type: The type of entity for the relationship. Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword entity_id: The unique identifier of the related entity. Default value is None.
        :paramtype entity_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_critical_data_elements_delete_relationship_request(
            critical_data_element_id=critical_data_element_id,
            entity_type=entity_type,
            entity_id=entity_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def query(
        self, request: _models.CriticalDataElementQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.CriticalDataElement"]:
        """Queries critical data elements based on various criteria. Rate limit: 800 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.CriticalDataElementQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of CriticalDataElement
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CriticalDataElement]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.CriticalDataElement"]:
        """Queries critical data elements based on various criteria. Rate limit: 800 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of CriticalDataElement
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CriticalDataElement]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.CriticalDataElement"]:
        """Queries critical data elements based on various criteria. Rate limit: 800 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of CriticalDataElement
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CriticalDataElement]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self, request: Union[_models.CriticalDataElementQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> ItemPaged["_models.CriticalDataElement"]:
        """Queries critical data elements based on various criteria. Rate limit: 800 requests per
        20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         CriticalDataElementQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.CriticalDataElementQueryRequest or JSON or
         IO[bytes]
        :return: An iterator like instance of CriticalDataElement
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.CriticalDataElement]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.CriticalDataElement]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_critical_data_elements_query_request(
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.CriticalDataElement],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def get_facets(
        self, request: _models.CriticalDataElementFacetRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for critical data elements. Rate limit: 1,500 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.CriticalDataElementFacetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for critical data elements. Rate limit: 1,500 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for critical data elements. Rate limit: 1,500 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def get_facets(
        self, request: Union[_models.CriticalDataElementFacetRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for critical data elements. Rate limit: 1,500 requests per 20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         CriticalDataElementFacetRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.CriticalDataElementFacetRequest or JSON or
         IO[bytes]
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FacetsResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_critical_data_elements_get_facets_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.FacetsResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def count(
        self, request: _models.DuplicateQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate critical data elements by passing namekeyword. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(self, request: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.EntityCount:
        """Retrieves the count of duplicate critical data elements by passing namekeyword. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate critical data elements by passing namekeyword. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def count(
        self, request: Union[_models.DuplicateQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate critical data elements by passing namekeyword. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         DuplicateQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest or JSON or IO[bytes]
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EntityCount] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_critical_data_elements_count_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.EntityCount, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class DataAssetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`data_assets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(
        self,
        *,
        include_extended_properties: bool,
        order_by: Optional[str] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.DataAsset"]:
        """Lists data assets with optional ordering and pagination. Rate limit: 150 requests per 20-second
        window.

        :keyword include_extended_properties: Include extended properties in the response. Required.
        :paramtype include_extended_properties: bool
        :keyword order_by: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype order_by: str
        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :return: An iterator like instance of DataAsset
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAsset]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DataAsset]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_assets_list_request(
                    include_extended_properties=include_extended_properties,
                    order_by=order_by,
                    skip=skip,
                    top=top,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataAsset],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create(
        self, data_asset: _models.DataAssetRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataAsset:
        """Creates a new data asset. Rate limit: 500 requests per 20-second window.

        :param data_asset: The data asset payload. Required.
        :type data_asset: ~purviewunifiedcatalog.models.DataAssetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, data_asset: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.DataAsset:
        """Creates a new data asset. Rate limit: 500 requests per 20-second window.

        :param data_asset: The data asset payload. Required.
        :type data_asset: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, data_asset: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataAsset:
        """Creates a new data asset. Rate limit: 500 requests per 20-second window.

        :param data_asset: The data asset payload. Required.
        :type data_asset: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(self, data_asset: Union[_models.DataAssetRequest, JSON, IO[bytes]], **kwargs: Any) -> _models.DataAsset:
        """Creates a new data asset. Rate limit: 500 requests per 20-second window.

        :param data_asset: The data asset payload. Is one of the following types: DataAssetRequest,
         JSON, IO[bytes] Required.
        :type data_asset: ~purviewunifiedcatalog.models.DataAssetRequest or JSON or IO[bytes]
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataAsset] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(data_asset, (IOBase, bytes)):
            _content = data_asset
        else:
            _content = json.dumps(data_asset, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_assets_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataAsset, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def query(
        self, request: _models.DataAssetQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataAsset"]:
        """Retrieves data assets with filtered query inputs. Rate limit: 800 requests per 20-second
        window.

        :param request: The data asset payload. Required.
        :type request: ~purviewunifiedcatalog.models.DataAssetQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataAsset
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAsset]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataAsset"]:
        """Retrieves data assets with filtered query inputs. Rate limit: 800 requests per 20-second
        window.

        :param request: The data asset payload. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataAsset
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAsset]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataAsset"]:
        """Retrieves data assets with filtered query inputs. Rate limit: 800 requests per 20-second
        window.

        :param request: The data asset payload. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataAsset
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAsset]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self, request: Union[_models.DataAssetQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> ItemPaged["_models.DataAsset"]:
        """Retrieves data assets with filtered query inputs. Rate limit: 800 requests per 20-second
        window.

        :param request: The data asset payload. Is one of the following types: DataAssetQueryRequest,
         JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DataAssetQueryRequest or JSON or IO[bytes]
        :return: An iterator like instance of DataAsset
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAsset]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.DataAsset]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_assets_query_request(
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataAsset],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    def get_by_id(
        self, data_asset_id: str, *, include_extended_properties: bool, include_lineage: bool, **kwargs: Any
    ) -> _models.DataAssetWithLineage:
        """Retrieves a data asset by its unique identifier. Rate limit: 1,000 requests per 20-second
        window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :keyword include_extended_properties: Include extended properties in the response. Required.
        :paramtype include_extended_properties: bool
        :keyword include_lineage: Include lineage information in the response. Required.
        :paramtype include_lineage: bool
        :return: DataAssetWithLineage. The DataAssetWithLineage is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAssetWithLineage
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DataAssetWithLineage] = kwargs.pop("cls", None)

        _request = build_data_assets_get_by_id_request(
            data_asset_id=data_asset_id,
            include_extended_properties=include_extended_properties,
            include_lineage=include_lineage,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataAssetWithLineage, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self,
        data_asset_id: str,
        data_asset: _models.DataAssetRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataAsset:
        """Updates a data asset by its unique identifier. Rate limit: 350 requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param data_asset: Updated data asset payload. Required.
        :type data_asset: ~purviewunifiedcatalog.models.DataAssetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, data_asset_id: str, data_asset: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataAsset:
        """Updates a data asset by its unique identifier. Rate limit: 350 requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param data_asset: Updated data asset payload. Required.
        :type data_asset: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, data_asset_id: str, data_asset: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataAsset:
        """Updates a data asset by its unique identifier. Rate limit: 350 requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param data_asset: Updated data asset payload. Required.
        :type data_asset: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(
        self, data_asset_id: str, data_asset: Union[_models.DataAssetRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.DataAsset:
        """Updates a data asset by its unique identifier. Rate limit: 350 requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param data_asset: Updated data asset payload. Is one of the following types: DataAssetRequest,
         JSON, IO[bytes] Required.
        :type data_asset: ~purviewunifiedcatalog.models.DataAssetRequest or JSON or IO[bytes]
        :return: DataAsset. The DataAsset is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataAsset
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataAsset] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(data_asset, (IOBase, bytes)):
            _content = data_asset
        else:
            _content = json.dumps(data_asset, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_assets_update_request(
            data_asset_id=data_asset_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataAsset, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_by_id(self, data_asset_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes a data asset by its unique identifier. Rate limit: 80 requests per 20-second window.

        :param data_asset_id: The data asset identifier. Required.
        :type data_asset_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_data_assets_delete_by_id_request(
            data_asset_id=data_asset_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def list_relationships(
        self, data_asset_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
    ) -> ItemPaged["_models.DataAssetRelationship"]:
        """Lists relationships for a data asset filtered by entity category. Rate limit: 1,500 requests
        per 20-second window.

        :param data_asset_id: The data asset identifier. Required.
        :type data_asset_id: str
        :keyword entity_type: Required entity category to list relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: An iterator like instance of DataAssetRelationship
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataAssetRelationship]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DataAssetRelationship]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_assets_list_relationships_request(
                    data_asset_id=data_asset_id,
                    entity_type=entity_type,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataAssetRelationship],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create_relationship(
        self,
        data_asset_id: str,
        relationship: _models.DataAssetRelationship,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Relationship:
        """Creates a relationship between the specified data asset and another entity. Rate limit: 600
        requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param relationship: Relationship payload as JSON (required). Required.
        :type relationship: ~purviewunifiedcatalog.models.DataAssetRelationship
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Relationship. The Relationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Relationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        data_asset_id: str,
        relationship: JSON,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Relationship:
        """Creates a relationship between the specified data asset and another entity. Rate limit: 600
        requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param relationship: Relationship payload as JSON (required). Required.
        :type relationship: JSON
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Relationship. The Relationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Relationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        data_asset_id: str,
        relationship: IO[bytes],
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Relationship:
        """Creates a relationship between the specified data asset and another entity. Rate limit: 600
        requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param relationship: Relationship payload as JSON (required). Required.
        :type relationship: IO[bytes]
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Relationship. The Relationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Relationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create_relationship(
        self,
        data_asset_id: str,
        relationship: Union[_models.DataAssetRelationship, JSON, IO[bytes]],
        *,
        entity_type: Union[str, _models.EntityCategory],
        **kwargs: Any
    ) -> _models.Relationship:
        """Creates a relationship between the specified data asset and another entity. Rate limit: 600
        requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :param relationship: Relationship payload as JSON (required). Is one of the following types:
         DataAssetRelationship, JSON, IO[bytes] Required.
        :type relationship: ~purviewunifiedcatalog.models.DataAssetRelationship or JSON or IO[bytes]
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: Relationship. The Relationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Relationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Relationship] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(relationship, (IOBase, bytes)):
            _content = relationship
        else:
            _content = json.dumps(relationship, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_assets_create_relationship_request(
            data_asset_id=data_asset_id,
            entity_type=entity_type,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Relationship, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_relationship(  # pylint: disable=inconsistent-return-statements
        self, data_asset_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
    ) -> None:
        """Deletes relationships for a data asset. Rate limit: 80 requests per 20-second window.

        :param data_asset_id: The unique identifier of the data asset. Required.
        :type data_asset_id: str
        :keyword entity_type: Category of the related entity (required). Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword entity_id: Identifier of the related entity (required). Required.
        :paramtype entity_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_data_assets_delete_relationship_request(
            data_asset_id=data_asset_id,
            entity_type=entity_type,
            entity_id=entity_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class DataProductsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`data_products` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        domain_id: Optional[str] = None,
        order_by: Optional[str] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.DataProduct"]:
        """Lists data products with optional domain filter, sorting and pagination. Rate limit: 100
        requests per 20-second window.

        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :keyword domain_id: Optional domain identifier filter. Default value is None.
        :paramtype domain_id: str
        :keyword order_by: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype order_by: str
        :return: An iterator like instance of DataProduct
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProduct]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DataProduct]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_products_list_request(
                    skip=skip,
                    top=top,
                    domain_id=domain_id,
                    order_by=order_by,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataProduct],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create(
        self, data_product: _models.DataProduct, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataProduct:
        """Creates a new data product. Rate limit: 200 requests per 20-second window.

        :param data_product: The data product payload. Required.
        :type data_product: ~purviewunifiedcatalog.models.DataProduct
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, data_product: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataProduct:
        """Creates a new data product. Rate limit: 200 requests per 20-second window.

        :param data_product: The data product payload. Required.
        :type data_product: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, data_product: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataProduct:
        """Creates a new data product. Rate limit: 200 requests per 20-second window.

        :param data_product: The data product payload. Required.
        :type data_product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(self, data_product: Union[_models.DataProduct, JSON, IO[bytes]], **kwargs: Any) -> _models.DataProduct:
        """Creates a new data product. Rate limit: 200 requests per 20-second window.

        :param data_product: The data product payload. Is one of the following types: DataProduct,
         JSON, IO[bytes] Required.
        :type data_product: ~purviewunifiedcatalog.models.DataProduct or JSON or IO[bytes]
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataProduct] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(data_product, (IOBase, bytes)):
            _content = data_product
        else:
            _content = json.dumps(data_product, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_products_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def query(
        self,
        request: _models.DataProductQueryRequest,
        *,
        data_product_owner: Optional[bool] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> ItemPaged["_models.DataProduct"]:
        """Queries data products using the provided filter payload. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: ~purviewunifiedcatalog.models.DataProductQueryRequest
        :keyword data_product_owner: Optional flag to restrict results to owned data products. Default
         value is None.
        :paramtype data_product_owner: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataProduct
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProduct]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self,
        request: JSON,
        *,
        data_product_owner: Optional[bool] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> ItemPaged["_models.DataProduct"]:
        """Queries data products using the provided filter payload. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: JSON
        :keyword data_product_owner: Optional flag to restrict results to owned data products. Default
         value is None.
        :paramtype data_product_owner: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataProduct
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProduct]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self,
        request: IO[bytes],
        *,
        data_product_owner: Optional[bool] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> ItemPaged["_models.DataProduct"]:
        """Queries data products using the provided filter payload. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: IO[bytes]
        :keyword data_product_owner: Optional flag to restrict results to owned data products. Default
         value is None.
        :paramtype data_product_owner: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataProduct
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProduct]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self,
        request: Union[_models.DataProductQueryRequest, JSON, IO[bytes]],
        *,
        data_product_owner: Optional[bool] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.DataProduct"]:
        """Queries data products using the provided filter payload. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Is one of the following types:
         DataProductQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DataProductQueryRequest or JSON or IO[bytes]
        :keyword data_product_owner: Optional flag to restrict results to owned data products. Default
         value is None.
        :paramtype data_product_owner: bool
        :return: An iterator like instance of DataProduct
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProduct]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.DataProduct]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_products_query_request(
                    data_product_owner=data_product_owner,
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataProduct],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def get_facets(
        self, request: _models.DataProductFacetRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for data products based on the supplied facets request. Rate limit: 1,500
        requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: ~purviewunifiedcatalog.models.DataProductFacetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for data products based on the supplied facets request. Rate limit: 1,500
        requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for data products based on the supplied facets request. Rate limit: 1,500
        requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def get_facets(
        self, request: Union[_models.DataProductFacetRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for data products based on the supplied facets request. Rate limit: 1,500
        requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Is one of the following
         types: DataProductFacetRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DataProductFacetRequest or JSON or IO[bytes]
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FacetsResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_products_get_facets_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.FacetsResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get(self, data_product_id: str, **kwargs: Any) -> _models.DataProduct:
        """Retrieves a data product by its dataProductId. Rate limit: 1,500 requests per 20-second window.

        :param data_product_id: The unique identifier of the data product. Required.
        :type data_product_id: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DataProduct] = kwargs.pop("cls", None)

        _request = build_data_products_get_request(
            data_product_id=data_product_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self,
        data_product_id: str,
        data_product: _models.DataProduct,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataProduct:
        """Updates a data product by its DataProductId. Rate limit: 150 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param data_product: Updated data product payload. Required.
        :type data_product: ~purviewunifiedcatalog.models.DataProduct
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, data_product_id: str, data_product: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataProduct:
        """Updates a data product by its DataProductId. Rate limit: 150 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param data_product: Updated data product payload. Required.
        :type data_product: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, data_product_id: str, data_product: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataProduct:
        """Updates a data product by its DataProductId. Rate limit: 150 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param data_product: Updated data product payload. Required.
        :type data_product: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(
        self, data_product_id: str, data_product: Union[_models.DataProduct, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.DataProduct:
        """Updates a data product by its DataProductId. Rate limit: 150 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param data_product: Updated data product payload. Is one of the following types: DataProduct,
         JSON, IO[bytes] Required.
        :type data_product: ~purviewunifiedcatalog.models.DataProduct or JSON or IO[bytes]
        :return: DataProduct. The DataProduct is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProduct
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataProduct] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(data_product, (IOBase, bytes)):
            _content = data_product
        else:
            _content = json.dumps(data_product, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_products_update_request(
            data_product_id=data_product_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(self, data_product_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes a data product by its dataProductId. Rate limit: 80 requests per 20-second window.

        :param data_product_id: The unique identifier of the data product. Required.
        :type data_product_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_data_products_delete_request(
            data_product_id=data_product_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def list_relationships(
        self, data_product_id: str, *, entity_type: Optional[Union[str, _models.EntityCategory]] = None, **kwargs: Any
    ) -> ItemPaged["_models.DataProductRelationship"]:
        """Lists relationships for a data product filtered by entity category. Rate limit: 1,500 requests
        per 20-second window.

        :param data_product_id: The unique identifier of the data product. Required.
        :type data_product_id: str
        :keyword entity_type: Required entity category to list relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: An iterator like instance of DataProductRelationship
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataProductRelationship]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DataProductRelationship]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_products_list_relationships_request(
                    data_product_id=data_product_id,
                    entity_type=entity_type,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataProductRelationship],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create_relationship(
        self,
        data_product_id: str,
        relationship: _models.CriticalDataElementRelationshipRequest,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataProductRelationship:
        """Creates a relationship for a data product. Rate limit: 600 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param relationship: Relationship payload as JSON. Required.
        :type relationship: ~purviewunifiedcatalog.models.CriticalDataElementRelationshipRequest
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProductRelationship. The DataProductRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProductRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        data_product_id: str,
        relationship: JSON,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataProductRelationship:
        """Creates a relationship for a data product. Rate limit: 600 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param relationship: Relationship payload as JSON. Required.
        :type relationship: JSON
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProductRelationship. The DataProductRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProductRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_relationship(
        self,
        data_product_id: str,
        relationship: IO[bytes],
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataProductRelationship:
        """Creates a relationship for a data product. Rate limit: 600 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param relationship: Relationship payload as JSON. Required.
        :type relationship: IO[bytes]
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataProductRelationship. The DataProductRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProductRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create_relationship(
        self,
        data_product_id: str,
        relationship: Union[_models.CriticalDataElementRelationshipRequest, JSON, IO[bytes]],
        *,
        entity_type: Union[str, _models.EntityCategory],
        **kwargs: Any
    ) -> _models.DataProductRelationship:
        """Creates a relationship for a data product. Rate limit: 600 requests per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :param relationship: Relationship payload as JSON. Is one of the following types:
         CriticalDataElementRelationshipRequest, JSON, IO[bytes] Required.
        :type relationship: ~purviewunifiedcatalog.models.CriticalDataElementRelationshipRequest or
         JSON or IO[bytes]
        :keyword entity_type: Category of the entity to relate to (required). Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: DataProductRelationship. The DataProductRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataProductRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataProductRelationship] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(relationship, (IOBase, bytes)):
            _content = relationship
        else:
            _content = json.dumps(relationship, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_products_create_relationship_request(
            data_product_id=data_product_id,
            entity_type=entity_type,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataProductRelationship, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_relationship(  # pylint: disable=inconsistent-return-statements
        self, data_product_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
    ) -> None:
        """Deletes a relationship between the data product and a specified entity. Rate limit: 80 requests
        per 20-second window.

        :param data_product_id: The unique identifier of the  data product. Required.
        :type data_product_id: str
        :keyword entity_type: Category of the related entity (required). Known values are: "DOMAIN",
         "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword entity_id: Identifier of the related entity (required). Required.
        :paramtype entity_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_data_products_delete_relationship_request(
            data_product_id=data_product_id,
            entity_type=entity_type,
            entity_id=entity_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def count(
        self, request: _models.DuplicateQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate DataProduct by passing namekeyword. Rate limit: 200 requests
        per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(self, request: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.EntityCount:
        """Retrieves the count of duplicate DataProduct by passing namekeyword. Rate limit: 200 requests
        per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate DataProduct by passing namekeyword. Rate limit: 200 requests
        per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def count(
        self, request: Union[_models.DuplicateQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate DataProduct by passing namekeyword. Rate limit: 200 requests
        per 20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         DuplicateQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest or JSON or IO[bytes]
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EntityCount] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_products_count_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.EntityCount, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class BusinessDomainOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`business_domain` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def enumerate(
        self, *, skip_token: Optional[str] = None, write_only: Optional[bool] = None, **kwargs: Any
    ) -> ItemPaged["_models.Domain"]:
        """Enumerates business domains with optional continuation token and write-obligation filtering.
        Rate limit: 500 requests per 20-second window.

        :keyword skip_token: Optional continuation token for pagination. Default value is None.
        :paramtype skip_token: str
        :keyword write_only: writeOnly. Default value is None.
        :paramtype write_only: bool
        :return: An iterator like instance of Domain
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Domain]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.Domain]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_business_domain_enumerate_request(
                    skip_token=skip_token,
                    write_only=write_only,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.Domain],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create(
        self, domain: _models.Domain, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Domain:
        """Creates a new business domain. Rate limit: 200 requests per 20-second window.

        :param domain: Domain payload to create. Required.
        :type domain: ~purviewunifiedcatalog.models.Domain
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, domain: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Domain:
        """Creates a new business domain. Rate limit: 200 requests per 20-second window.

        :param domain: Domain payload to create. Required.
        :type domain: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, domain: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> _models.Domain:
        """Creates a new business domain. Rate limit: 200 requests per 20-second window.

        :param domain: Domain payload to create. Required.
        :type domain: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(self, domain: Union[_models.Domain, JSON, IO[bytes]], **kwargs: Any) -> _models.Domain:
        """Creates a new business domain. Rate limit: 200 requests per 20-second window.

        :param domain: Domain payload to create. Is one of the following types: Domain, JSON, IO[bytes]
         Required.
        :type domain: ~purviewunifiedcatalog.models.Domain or JSON or IO[bytes]
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Domain] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(domain, (IOBase, bytes)):
            _content = domain
        else:
            _content = json.dumps(domain, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_business_domain_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Domain, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self, domain_id: str, domain: _models.Domain, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Domain:
        """Updates an existing business domain. Rate limit: 150 requests per 20-second window.

        :param domain_id: The unique identifier of the data domain. Required.
        :type domain_id: str
        :param domain: Updated domain payload. Required.
        :type domain: ~purviewunifiedcatalog.models.Domain
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, domain_id: str, domain: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Domain:
        """Updates an existing business domain. Rate limit: 150 requests per 20-second window.

        :param domain_id: The unique identifier of the data domain. Required.
        :type domain_id: str
        :param domain: Updated domain payload. Required.
        :type domain: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, domain_id: str, domain: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Domain:
        """Updates an existing business domain. Rate limit: 150 requests per 20-second window.

        :param domain_id: The unique identifier of the data domain. Required.
        :type domain_id: str
        :param domain: Updated domain payload. Required.
        :type domain: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(self, domain_id: str, domain: Union[_models.Domain, JSON, IO[bytes]], **kwargs: Any) -> _models.Domain:
        """Updates an existing business domain. Rate limit: 150 requests per 20-second window.

        :param domain_id: The unique identifier of the data domain. Required.
        :type domain_id: str
        :param domain: Updated domain payload. Is one of the following types: Domain, JSON, IO[bytes]
         Required.
        :type domain: ~purviewunifiedcatalog.models.Domain or JSON or IO[bytes]
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Domain] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(domain, (IOBase, bytes)):
            _content = domain
        else:
            _content = json.dumps(domain, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_business_domain_update_request(
            domain_id=domain_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Domain, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get(self, domain_id: str, **kwargs: Any) -> _models.Domain:
        """Retrieves a business domain by identifier. Rate limit: 2,000 requests per 20-second window.

        :param domain_id: The unique identifier of the domain. Required.
        :type domain_id: str
        :return: Domain. The Domain is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Domain
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Domain] = kwargs.pop("cls", None)

        _request = build_business_domain_get_request(
            domain_id=domain_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Domain, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(self, domain_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes an existing business domain. Rate limit: 80 requests per 20-second window.

        :param domain_id: The unique identifier of the domain. Required.
        :type domain_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_business_domain_delete_request(
            domain_id=domain_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class TermsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`terms` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create(self, term: _models.Term, *, content_type: str = "application/json", **kwargs: Any) -> _models.Term:
        """Creates a new term in the catalog. Rate limit: 200 requests per 20-second window.

        :param term: Term payload. Required.
        :type term: ~purviewunifiedcatalog.models.Term
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, term: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Term:
        """Creates a new term in the catalog. Rate limit: 200 requests per 20-second window.

        :param term: Term payload. Required.
        :type term: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, term: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> _models.Term:
        """Creates a new term in the catalog. Rate limit: 200 requests per 20-second window.

        :param term: Term payload. Required.
        :type term: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(self, term: Union[_models.Term, JSON, IO[bytes]], **kwargs: Any) -> _models.Term:
        """Creates a new term in the catalog. Rate limit: 200 requests per 20-second window.

        :param term: Term payload. Is one of the following types: Term, JSON, IO[bytes] Required.
        :type term: ~purviewunifiedcatalog.models.Term or JSON or IO[bytes]
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Term] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(term, (IOBase, bytes)):
            _content = term
        else:
            _content = json.dumps(term, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_terms_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Term, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def list(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        domain_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        keyword: Optional[str] = None,
        depth: Optional[int] = None,
        order_by: Optional[str] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.Term"]:
        """Lists terms with optional domain/parent/keyword filters and pagination. Rate limit: 100
        requests per 20-second window.

        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :keyword domain_id: The unique identifier of the domain. Default value is None.
        :paramtype domain_id: str
        :keyword parent_id: The unique identifier of the parent term. Default value is None.
        :paramtype parent_id: str
        :keyword keyword: Search keyword. Default value is None.
        :paramtype keyword: str
        :keyword depth: The depth of the term. Default value is None.
        :paramtype depth: int
        :keyword order_by: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype order_by: str
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.Term]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_terms_list_request(
                    skip=skip,
                    top=top,
                    domain_id=domain_id,
                    parent_id=parent_id,
                    keyword=keyword,
                    depth=depth,
                    order_by=order_by,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.Term],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def update(
        self, term_id: str, term: _models.Term, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Term:
        """Updates an existing term. Rate limit: 150 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term: Updated term payload. Required.
        :type term: ~purviewunifiedcatalog.models.Term
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, term_id: str, term: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Term:
        """Updates an existing term. Rate limit: 150 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term: Updated term payload. Required.
        :type term: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, term_id: str, term: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Term:
        """Updates an existing term. Rate limit: 150 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term: Updated term payload. Required.
        :type term: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(self, term_id: str, term: Union[_models.Term, JSON, IO[bytes]], **kwargs: Any) -> _models.Term:
        """Updates an existing term. Rate limit: 150 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term: Updated term payload. Is one of the following types: Term, JSON, IO[bytes]
         Required.
        :type term: ~purviewunifiedcatalog.models.Term or JSON or IO[bytes]
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Term] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(term, (IOBase, bytes)):
            _content = term
        else:
            _content = json.dumps(term, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_terms_update_request(
            term_id=term_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Term, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get(self, term_id: str, **kwargs: Any) -> _models.Term:
        """Retrieves a single term by identifier. Rate limit: 1,500 requests per 20-second window.

        :param term_id: The unique identifier of the term. Required.
        :type term_id: str
        :return: Term. The Term is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.Term
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Term] = kwargs.pop("cls", None)

        _request = build_terms_get_request(
            term_id=term_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.Term, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(self, term_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes a term by its unique identifier. Rate limit: 80 requests per 20-second window.

        :param term_id: The unique identifier of the term. Required.
        :type term_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_terms_delete_request(
            term_id=term_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def query(
        self, request: _models.TermQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.Term"]:
        """Queries terms based on the provided request. Rate limit: 800 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.TermQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.Term"]:
        """Queries terms based on the provided request. Rate limit: 800 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.Term"]:
        """Queries terms based on the provided request. Rate limit: 800 requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self, request: Union[_models.TermQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> ItemPaged["_models.Term"]:
        """Queries terms based on the provided request. Rate limit: 800 requests per 20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         TermQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.TermQueryRequest or JSON or IO[bytes]
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.Term]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_terms_query_request(
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.Term],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def get_facets(
        self, request: _models.TermFacetRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for terms. Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: ~purviewunifiedcatalog.models.TermFacetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for terms. Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for terms. Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def get_facets(
        self, request: Union[_models.TermFacetRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves facets for terms. Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Is one of the following
         types: TermFacetRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.TermFacetRequest or JSON or IO[bytes]
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FacetsResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_terms_get_facets_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.FacetsResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def list_hierarchy(self, term_id: str, **kwargs: Any) -> ItemPaged["_models.Term"]:
        """Lists hierarchical terms under the specified term id. Rate limit: 200 requests per 20-second
        window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :return: An iterator like instance of Term
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.Term]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.Term]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_terms_list_hierarchy_request(
                    term_id=term_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.Term],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def add_related_entity(
        self,
        term_id: str,
        term_relation: _models.TermRelationship,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TermRelationship:
        """Adds a related entity to a term. Rate limit: 600 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term_relation: Relationship payload. Required.
        :type term_relation: ~purviewunifiedcatalog.models.TermRelationship
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TermRelationship. The TermRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.TermRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def add_related_entity(
        self,
        term_id: str,
        term_relation: JSON,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TermRelationship:
        """Adds a related entity to a term. Rate limit: 600 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term_relation: Relationship payload. Required.
        :type term_relation: JSON
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TermRelationship. The TermRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.TermRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def add_related_entity(
        self,
        term_id: str,
        term_relation: IO[bytes],
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TermRelationship:
        """Adds a related entity to a term. Rate limit: 600 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term_relation: Relationship payload. Required.
        :type term_relation: IO[bytes]
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TermRelationship. The TermRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.TermRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def add_related_entity(
        self,
        term_id: str,
        term_relation: Union[_models.TermRelationship, JSON, IO[bytes]],
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        **kwargs: Any
    ) -> _models.TermRelationship:
        """Adds a related entity to a term. Rate limit: 600 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :param term_relation: Relationship payload. Is one of the following types: TermRelationship,
         JSON, IO[bytes] Required.
        :type term_relation: ~purviewunifiedcatalog.models.TermRelationship or JSON or IO[bytes]
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: TermRelationship. The TermRelationship is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.TermRelationship
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TermRelationship] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(term_relation, (IOBase, bytes)):
            _content = term_relation
        else:
            _content = json.dumps(term_relation, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_terms_add_related_entity_request(
            term_id=term_id,
            entity_type=entity_type,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.TermRelationship, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_related(  # pylint: disable=inconsistent-return-statements
        self,
        term_id: str,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        relationship_type: Optional[Union[str, _models.TermRelationshipType]] = None,
        entity_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a related entity from a term. Rate limit: 80 requests per 20-second window.

        :param term_id: The unique identifier of the data term or Parent term identifier. Required.
        :type term_id: str
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword relationship_type: Optional relationship type. Known values are: "Related", "Synonym",
         and "Parent". Default value is None.
        :paramtype relationship_type: str or ~purviewunifiedcatalog.models.TermRelationshipType
        :keyword entity_id: Related entity identifier. Default value is None.
        :paramtype entity_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_terms_delete_related_request(
            term_id=term_id,
            entity_type=entity_type,
            relationship_type=relationship_type,
            entity_id=entity_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def list_related_entities(
        self,
        term_id: str,
        *,
        entity_type: Optional[Union[str, _models.EntityCategory]] = None,
        relationship_type: Optional[Union[str, _models.TermRelationshipType]] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.TermRelationship"]:
        """Lists related entities for a term by category and optional relationship type. Rate limit: 1,500
        requests per 20-second window.

        :param term_id: The unique identifier of the term. Required.
        :type term_id: str
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Default value is None.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword relationship_type: Optional relationship type. Known values are: "Related", "Synonym",
         and "Parent". Default value is None.
        :paramtype relationship_type: str or ~purviewunifiedcatalog.models.TermRelationshipType
        :return: An iterator like instance of TermRelationship
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.TermRelationship]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.TermRelationship]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_terms_list_related_entities_request(
                    term_id=term_id,
                    entity_type=entity_type,
                    relationship_type=relationship_type,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.TermRelationship],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def count(
        self, request: _models.DuplicateQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate Term by passing namekeyword. Rate limit: 200 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(self, request: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.EntityCount:
        """Retrieves the count of duplicate Term by passing namekeyword. Rate limit: 200 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate Term by passing namekeyword. Rate limit: 200 requests per
        20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def count(
        self, request: Union[_models.DuplicateQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate Term by passing namekeyword. Rate limit: 200 requests per
        20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         DuplicateQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateQueryRequest or JSON or IO[bytes]
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EntityCount] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_terms_count_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.EntityCount, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class OkrOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`okr` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        keyword: Optional[str] = None,
        domain_id: Optional[str] = None,
        order_by: Optional[str] = None,
        **kwargs: Any
    ) -> ItemPaged["_models.ObjectiveWithAdditionalProperties"]:
        """Lists objectives with optional filters, sorting and pagination. Rate limit: 100 requests per
        20-second window.

        :keyword skip: The number of result items to skip. Default value is None.
        :paramtype skip: int
        :keyword top: The number of result items to return. Default value is None.
        :paramtype top: int
        :keyword keyword: Optional search keyword to match objective definition. Default value is None.
        :paramtype keyword: str
        :keyword domain_id: Optional domain identifier filter. Default value is None.
        :paramtype domain_id: str
        :keyword order_by: Expressions that specify the order of returned results. Default value is
         None.
        :paramtype order_by: str
        :return: An iterator like instance of ObjectiveWithAdditionalProperties
        :rtype:
         ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.ObjectiveWithAdditionalProperties]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_okr_list_request(
                    skip=skip,
                    top=top,
                    keyword=keyword,
                    domain_id=domain_id,
                    order_by=order_by,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.ObjectiveWithAdditionalProperties],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create(
        self,
        objective: _models.ObjectiveWithAdditionalProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Creates a new objective (OKR). Rate limit: 200 requests per 20-second window.

        :param objective: The objective payload, including additional properties. Required.
        :type objective: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, objective: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Creates a new objective (OKR). Rate limit: 200 requests per 20-second window.

        :param objective: The objective payload, including additional properties. Required.
        :type objective: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, objective: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Creates a new objective (OKR). Rate limit: 200 requests per 20-second window.

        :param objective: The objective payload, including additional properties. Required.
        :type objective: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(
        self, objective: Union[_models.ObjectiveWithAdditionalProperties, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Creates a new objective (OKR). Rate limit: 200 requests per 20-second window.

        :param objective: The objective payload, including additional properties. Is one of the
         following types: ObjectiveWithAdditionalProperties, JSON, IO[bytes] Required.
        :type objective: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties or JSON or
         IO[bytes]
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ObjectiveWithAdditionalProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(objective, (IOBase, bytes)):
            _content = objective
        else:
            _content = json.dumps(objective, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.ObjectiveWithAdditionalProperties, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def query(
        self, request: _models.ObjectiveQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.ObjectiveWithAdditionalProperties"]:
        """Queries objectives (OKRs) based on specified criteria. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: ~purviewunifiedcatalog.models.ObjectiveQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of ObjectiveWithAdditionalProperties
        :rtype:
         ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.ObjectiveWithAdditionalProperties"]:
        """Queries objectives (OKRs) based on specified criteria. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of ObjectiveWithAdditionalProperties
        :rtype:
         ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.ObjectiveWithAdditionalProperties"]:
        """Queries objectives (OKRs) based on specified criteria. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of ObjectiveWithAdditionalProperties
        :rtype:
         ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self, request: Union[_models.ObjectiveQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> ItemPaged["_models.ObjectiveWithAdditionalProperties"]:
        """Queries objectives (OKRs) based on specified criteria. Rate limit: 800 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Is one of the following types:
         ObjectiveQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.ObjectiveQueryRequest or JSON or IO[bytes]
        :return: An iterator like instance of ObjectiveWithAdditionalProperties
        :rtype:
         ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.ObjectiveWithAdditionalProperties]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_okr_query_request(
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.ObjectiveWithAdditionalProperties],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def get_facets(
        self, request: _models.ObjectiveFacetRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves the facets for objectives (OKRs). Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: ~purviewunifiedcatalog.models.ObjectiveFacetRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves the facets for objectives (OKRs). Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def get_facets(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves the facets for objectives (OKRs). Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def get_facets(
        self, request: Union[_models.ObjectiveFacetRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FacetsResponse:
        """Retrieves the facets for objectives (OKRs). Rate limit: 1,500 requests per 20-second window.

        :param request: Facet request specifying which facets to compute. Is one of the following
         types: ObjectiveFacetRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.ObjectiveFacetRequest or JSON or IO[bytes]
        :return: FacetsResponse. The FacetsResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.FacetsResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FacetsResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_get_facets_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.FacetsResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self,
        objective_id: str,
        objective: _models.ObjectiveQueryAdditionalProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Updates an existing objective (OKR) by ID. Rate limit: 150 requests per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param objective: Updated objective payload. Required.
        :type objective: ~purviewunifiedcatalog.models.ObjectiveQueryAdditionalProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, objective_id: str, objective: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Updates an existing objective (OKR) by ID. Rate limit: 150 requests per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param objective: Updated objective payload. Required.
        :type objective: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, objective_id: str, objective: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Updates an existing objective (OKR) by ID. Rate limit: 150 requests per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param objective: Updated objective payload. Required.
        :type objective: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(
        self,
        objective_id: str,
        objective: Union[_models.ObjectiveQueryAdditionalProperties, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.ObjectiveWithAdditionalProperties:
        """Updates an existing objective (OKR) by ID. Rate limit: 150 requests per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param objective: Updated objective payload. Is one of the following types:
         ObjectiveQueryAdditionalProperties, JSON, IO[bytes] Required.
        :type objective: ~purviewunifiedcatalog.models.ObjectiveQueryAdditionalProperties or JSON or
         IO[bytes]
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ObjectiveWithAdditionalProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(objective, (IOBase, bytes)):
            _content = objective
        else:
            _content = json.dumps(objective, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_update_request(
            objective_id=objective_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.ObjectiveWithAdditionalProperties, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete(self, objective_id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Deletes an objective by identifier. Rate limit: 80 requests per 20-second window.

        :param objective_id: The unique identifier of the objective. Required.
        :type objective_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_okr_delete_request(
            objective_id=objective_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    def get(self, objective_id: str, **kwargs: Any) -> _models.ObjectiveWithAdditionalProperties:
        """Retrieves an objective by identifier. Rate limit: 1,500 requests per 20-second window.

        :param objective_id: The unique identifier of the objective. Required.
        :type objective_id: str
        :return: ObjectiveWithAdditionalProperties. The ObjectiveWithAdditionalProperties is compatible
         with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.ObjectiveWithAdditionalProperties
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ObjectiveWithAdditionalProperties] = kwargs.pop("cls", None)

        _request = build_okr_get_request(
            objective_id=objective_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.ObjectiveWithAdditionalProperties, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def list_key_results(self, objective_id: str, **kwargs: Any) -> ItemPaged["_models.KeyResult"]:
        """Lists key results for a given objective. Rate limit: 100 requests per 20-second window.

        :param objective_id: The unique identifier of the objective. Required.
        :type objective_id: str
        :return: An iterator like instance of KeyResult
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.KeyResult]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.KeyResult]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_okr_list_key_results_request(
                    objective_id=objective_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.KeyResult],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def create_key_result(
        self, objective_id: str, key_result: _models.KeyResult, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.KeyResult:
        """Creates a key result under the specified objective. Rate limit: 200 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result: Key result payload. Required.
        :type key_result: ~purviewunifiedcatalog.models.KeyResult
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: KeyResult. The KeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.KeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_key_result(
        self, objective_id: str, key_result: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.KeyResult:
        """Creates a key result under the specified objective. Rate limit: 200 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result: Key result payload. Required.
        :type key_result: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: KeyResult. The KeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.KeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_key_result(
        self, objective_id: str, key_result: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.KeyResult:
        """Creates a key result under the specified objective. Rate limit: 200 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result: Key result payload. Required.
        :type key_result: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: KeyResult. The KeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.KeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create_key_result(
        self, objective_id: str, key_result: Union[_models.KeyResult, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.KeyResult:
        """Creates a key result under the specified objective. Rate limit: 200 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result: Key result payload. Is one of the following types: KeyResult, JSON,
         IO[bytes] Required.
        :type key_result: ~purviewunifiedcatalog.models.KeyResult or JSON or IO[bytes]
        :return: KeyResult. The KeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.KeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.KeyResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(key_result, (IOBase, bytes)):
            _content = key_result
        else:
            _content = json.dumps(key_result, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_create_key_result_request(
            objective_id=objective_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.KeyResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def get_key_result(self, objective_id: str, key_result_id: str, **kwargs: Any) -> _models.KeyResult:
        """Retrieves a key result by its identifier under the specified objective. Rate limit: 1,500
        requests per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :return: KeyResult. The KeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.KeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.KeyResult] = kwargs.pop("cls", None)

        _request = build_okr_get_key_result_request(
            objective_id=objective_id,
            key_result_id=key_result_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.KeyResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update_key_result(
        self,
        objective_id: str,
        key_result_id: str,
        key_result: _models.CatalogModelKeyResult,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CatalogModelKeyResult:
        """Updates a key result under the specified objective. Rate limit: 150 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :param key_result: Updated key result payload. Required.
        :type key_result: ~purviewunifiedcatalog.models.CatalogModelKeyResult
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogModelKeyResult. The CatalogModelKeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogModelKeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_key_result(
        self,
        objective_id: str,
        key_result_id: str,
        key_result: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CatalogModelKeyResult:
        """Updates a key result under the specified objective. Rate limit: 150 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :param key_result: Updated key result payload. Required.
        :type key_result: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogModelKeyResult. The CatalogModelKeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogModelKeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_key_result(
        self,
        objective_id: str,
        key_result_id: str,
        key_result: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CatalogModelKeyResult:
        """Updates a key result under the specified objective. Rate limit: 150 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :param key_result: Updated key result payload. Required.
        :type key_result: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogModelKeyResult. The CatalogModelKeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogModelKeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update_key_result(
        self,
        objective_id: str,
        key_result_id: str,
        key_result: Union[_models.CatalogModelKeyResult, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.CatalogModelKeyResult:
        """Updates a key result under the specified objective. Rate limit: 150 requests per 20-second
        window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :param key_result: Updated key result payload. Is one of the following types:
         CatalogModelKeyResult, JSON, IO[bytes] Required.
        :type key_result: ~purviewunifiedcatalog.models.CatalogModelKeyResult or JSON or IO[bytes]
        :return: CatalogModelKeyResult. The CatalogModelKeyResult is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogModelKeyResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CatalogModelKeyResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(key_result, (IOBase, bytes)):
            _content = key_result
        else:
            _content = json.dumps(key_result, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_update_key_result_request(
            objective_id=objective_id,
            key_result_id=key_result_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CatalogModelKeyResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_key_result(  # pylint: disable=inconsistent-return-statements
        self, objective_id: str, key_result_id: str, **kwargs: Any
    ) -> None:
        """Deletes a key result by its identifier under the specified objective. Rate limit: 80 requests
        per 20-second window.

        :param objective_id: The unique identifier of the critical data objective. Required.
        :type objective_id: str
        :param key_result_id: The unique identifier of the key result (OKR). Required.
        :type key_result_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_okr_delete_key_result_request(
            objective_id=objective_id,
            key_result_id=key_result_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    def count(
        self, request: _models.DuplicateOkrQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate objectives/OKRs by passing definition. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateOkrQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(self, request: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.EntityCount:
        """Retrieves the count of duplicate objectives/OKRs by passing definition. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def count(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate objectives/OKRs by passing definition. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def count(
        self, request: Union[_models.DuplicateOkrQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.EntityCount:
        """Retrieves the count of duplicate objectives/OKRs by passing definition. Rate limit: 200
        requests per 20-second window.

        :param request: The request body containing query criteria. Is one of the following types:
         DuplicateOkrQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DuplicateOkrQueryRequest or JSON or IO[bytes]
        :return: EntityCount. The EntityCount is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.EntityCount
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.EntityCount] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_okr_count_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.EntityCount, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class PoliciesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`policies` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(self, *, skip_token: Optional[str] = None, **kwargs: Any) -> _models.CatalogResponse:
        """Lists policies with optional continuation token. Rate limit: 100 requests per 20-second window.

        :keyword skip_token: Optional continuation token. Default value is None.
        :paramtype skip_token: str
        :return: CatalogResponse. The CatalogResponse is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CatalogResponse] = kwargs.pop("cls", None)

        _request = build_policies_list_request(
            skip_token=skip_token,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CatalogResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update(
        self, policy_id: str, request: _models.CatalogValue, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatalogValue:
        """Updates a policy by its identifier. Rate limit: 200 requests per 20-second window.

        1. BusinessDomain - Governance Domain Owners, Governance Domain Readers
        2. Data Quality - Data Product Owners, Data Steward, Data Quality Readers, Data Quality
        Metadata Readers, Data Profile Stewards, Data Profile Readers
        3. Data Governance - Data Governance Administrators, Data Health Readers, Data Health Owners,
        Governance Domain Creators, Global Asset Curators, Global Catalog Readers.

        :param policy_id: The unique identifier of the policy. Required.
        :type policy_id: str
        :param request: Updated policy payload. Required.
        :type request: ~purviewunifiedcatalog.models.CatalogValue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogValue. The CatalogValue is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogValue
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, policy_id: str, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatalogValue:
        """Updates a policy by its identifier. Rate limit: 200 requests per 20-second window.

        1. BusinessDomain - Governance Domain Owners, Governance Domain Readers
        2. Data Quality - Data Product Owners, Data Steward, Data Quality Readers, Data Quality
        Metadata Readers, Data Profile Stewards, Data Profile Readers
        3. Data Governance - Data Governance Administrators, Data Health Readers, Data Health Owners,
        Governance Domain Creators, Global Asset Curators, Global Catalog Readers.

        :param policy_id: The unique identifier of the policy. Required.
        :type policy_id: str
        :param request: Updated policy payload. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogValue. The CatalogValue is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogValue
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, policy_id: str, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatalogValue:
        """Updates a policy by its identifier. Rate limit: 200 requests per 20-second window.

        1. BusinessDomain - Governance Domain Owners, Governance Domain Readers
        2. Data Quality - Data Product Owners, Data Steward, Data Quality Readers, Data Quality
        Metadata Readers, Data Profile Stewards, Data Profile Readers
        3. Data Governance - Data Governance Administrators, Data Health Readers, Data Health Owners,
        Governance Domain Creators, Global Asset Curators, Global Catalog Readers.

        :param policy_id: The unique identifier of the policy. Required.
        :type policy_id: str
        :param request: Updated policy payload. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatalogValue. The CatalogValue is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogValue
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update(
        self, policy_id: str, request: Union[_models.CatalogValue, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.CatalogValue:
        """Updates a policy by its identifier. Rate limit: 200 requests per 20-second window.

        1. BusinessDomain - Governance Domain Owners, Governance Domain Readers
        2. Data Quality - Data Product Owners, Data Steward, Data Quality Readers, Data Quality
        Metadata Readers, Data Profile Stewards, Data Profile Readers
        3. Data Governance - Data Governance Administrators, Data Health Readers, Data Health Owners,
        Governance Domain Creators, Global Asset Curators, Global Catalog Readers.

        :param policy_id: The unique identifier of the policy. Required.
        :type policy_id: str
        :param request: Updated policy payload. Is one of the following types: CatalogValue, JSON,
         IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.CatalogValue or JSON or IO[bytes]
        :return: CatalogValue. The CatalogValue is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.CatalogValue
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CatalogValue] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_policies_update_request(
            policy_id=policy_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.CatalogValue, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class DataColumnsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~purviewunifiedcatalog.PurviewUnifiedCatalogClient`'s
        :attr:`data_columns` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: PurviewUnifiedCatalogClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def get(
        self,
        id: str,
        *,
        include_column_details: Optional[bool] = None,
        include_asset_details: Optional[bool] = None,
        **kwargs: Any
    ) -> _models.DataColumn:
        """Retrieves a single data column by identifier. Rate limit: 1,500 requests per 20-second window.

        :param id: The unique identifier of the data column. Required.
        :type id: str
        :keyword include_column_details: Include extended properties in the response. Default value is
         None.
        :paramtype include_column_details: bool
        :keyword include_asset_details: Include extended properties in the response. Default value is
         None.
        :paramtype include_asset_details: bool
        :return: DataColumn. The DataColumn is compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumn
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.DataColumn] = kwargs.pop("cls", None)

        _request = build_data_columns_get_request(
            id=id,
            include_column_details=include_column_details,
            include_asset_details=include_asset_details,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataColumn, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def ingest(
        self, request: _models.IngestDataColumnBatchRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataColumnIngestResponse:
        """Ingests a data column. Rate limit: 200 requests per 20-second window.

        :param request: Data column payload. Required.
        :type request: ~purviewunifiedcatalog.models.IngestDataColumnBatchRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnIngestResponse. The DataColumnIngestResponse is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnIngestResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def ingest(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataColumnIngestResponse:
        """Ingests a data column. Rate limit: 200 requests per 20-second window.

        :param request: Data column payload. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnIngestResponse. The DataColumnIngestResponse is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnIngestResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def ingest(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.DataColumnIngestResponse:
        """Ingests a data column. Rate limit: 200 requests per 20-second window.

        :param request: Data column payload. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnIngestResponse. The DataColumnIngestResponse is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnIngestResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def ingest(
        self, request: Union[_models.IngestDataColumnBatchRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.DataColumnIngestResponse:
        """Ingests a data column. Rate limit: 200 requests per 20-second window.

        :param request: Data column payload. Is one of the following types:
         IngestDataColumnBatchRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.IngestDataColumnBatchRequest or JSON or IO[bytes]
        :return: DataColumnIngestResponse. The DataColumnIngestResponse is compatible with
         MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnIngestResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataColumnIngestResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_columns_ingest_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataColumnIngestResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def query(
        self, request: _models.DataColumnQueryRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataColumn"]:
        """Queries data columns based on specified criteria. Rate limit: 100 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: ~purviewunifiedcatalog.models.DataColumnQueryRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataColumn
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataColumn]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataColumn"]:
        """Queries data columns based on specified criteria. Rate limit: 100 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataColumn
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataColumn]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def query(
        self, request: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> ItemPaged["_models.DataColumn"]:
        """Queries data columns based on specified criteria. Rate limit: 100 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Required.
        :type request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of DataColumn
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataColumn]
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def query(
        self, request: Union[_models.DataColumnQueryRequest, JSON, IO[bytes]], **kwargs: Any
    ) -> ItemPaged["_models.DataColumn"]:
        """Queries data columns based on specified criteria. Rate limit: 100 requests per 20-second
        window.

        :param request: Query request containing filters and pagination. Is one of the following types:
         DataColumnQueryRequest, JSON, IO[bytes] Required.
        :type request: ~purviewunifiedcatalog.models.DataColumnQueryRequest or JSON or IO[bytes]
        :return: An iterator like instance of DataColumn
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataColumn]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[List[_models.DataColumn]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _content = json.dumps(request, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_columns_query_request(
                    content_type=content_type,
                    api_version=self._config.api_version,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataColumn],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    def list_related_entities(
        self, data_column_id: str, *, entity_type: Union[str, _models.EntityCategory], **kwargs: Any
    ) -> ItemPaged["_models.DataColumnRelationshipWrapper"]:
        """Lists related entities for a data column by category and optional relationship type. Rate
        limit: 1,500 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: An iterator like instance of DataColumnRelationshipWrapper
        :rtype: ~corehttp.paging.ItemPaged[~purviewunifiedcatalog.models.DataColumnRelationshipWrapper]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DataColumnRelationshipWrapper]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_data_columns_list_related_entities_request(
                    data_column_id=data_column_id,
                    entity_type=entity_type,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET",
                    urllib.parse.urljoin(next_link, _parsed_next_link.path),
                    headers=_headers,
                    params=_next_request_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(
                List[_models.DataColumnRelationshipWrapper],
                deserialized.get("value", []),
            )
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def add_related_entity(
        self,
        data_column_id: str,
        relationship: _models.DataColumnCreateRelationshipRequest,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataColumnCreateRelationshipResponse:
        """Adds a related entity to a data column. Rate limit: 600 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :param relationship: Relationship payload. Required.
        :type relationship: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipRequest
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnCreateRelationshipResponse. The DataColumnCreateRelationshipResponse is
         compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def add_related_entity(
        self,
        data_column_id: str,
        relationship: JSON,
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataColumnCreateRelationshipResponse:
        """Adds a related entity to a data column. Rate limit: 600 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :param relationship: Relationship payload. Required.
        :type relationship: JSON
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnCreateRelationshipResponse. The DataColumnCreateRelationshipResponse is
         compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def add_related_entity(
        self,
        data_column_id: str,
        relationship: IO[bytes],
        *,
        entity_type: Union[str, _models.EntityCategory],
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataColumnCreateRelationshipResponse:
        """Adds a related entity to a data column. Rate limit: 600 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :param relationship: Relationship payload. Required.
        :type relationship: IO[bytes]
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataColumnCreateRelationshipResponse. The DataColumnCreateRelationshipResponse is
         compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def add_related_entity(
        self,
        data_column_id: str,
        relationship: Union[_models.DataColumnCreateRelationshipRequest, JSON, IO[bytes]],
        *,
        entity_type: Union[str, _models.EntityCategory],
        **kwargs: Any
    ) -> _models.DataColumnCreateRelationshipResponse:
        """Adds a related entity to a data column. Rate limit: 600 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :param relationship: Relationship payload. Is one of the following types:
         DataColumnCreateRelationshipRequest, JSON, IO[bytes] Required.
        :type relationship: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipRequest or JSON
         or IO[bytes]
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :return: DataColumnCreateRelationshipResponse. The DataColumnCreateRelationshipResponse is
         compatible with MutableMapping
        :rtype: ~purviewunifiedcatalog.models.DataColumnCreateRelationshipResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataColumnCreateRelationshipResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(relationship, (IOBase, bytes)):
            _content = relationship
        else:
            _content = json.dumps(relationship, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_data_columns_add_related_entity_request(
            data_column_id=data_column_id,
            entity_type=entity_type,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _decompress = kwargs.pop("decompress", True)
        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes() if _decompress else response.iter_raw()
        else:
            deserialized = _deserialize(_models.DataColumnCreateRelationshipResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def delete_related(  # pylint: disable=inconsistent-return-statements
        self, data_column_id: str, *, entity_type: Union[str, _models.EntityCategory], entity_id: str, **kwargs: Any
    ) -> None:
        """Deletes a related entity from a data column. Rate limit: 80 requests per 20-second window.

        :param data_column_id: The unique identifier of the data column. Required.
        :type data_column_id: str
        :keyword entity_type: The type of entity to retrieve relationships for. Known values are:
         "DOMAIN", "DATAPRODUCT", "TERM", "DATAASSET", "OBJECTIVE", "KEYRESULT", "CRITICALDATAELEMENT",
         "DATACOLUMN", "CUSTOMMETADATA", "ATTRIBUTE", "ATTRIBUTEINSTANCE", "WORKFLOW",
         "CATALOGSNAPSHOT", and "WORKFLOWRUN". Required.
        :paramtype entity_type: str or ~purviewunifiedcatalog.models.EntityCategory
        :keyword entity_id: Related entity identifier. Required.
        :paramtype entity_id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_data_columns_delete_related_request(
            data_column_id=data_column_id,
            entity_type=entity_type,
            entity_id=entity_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
