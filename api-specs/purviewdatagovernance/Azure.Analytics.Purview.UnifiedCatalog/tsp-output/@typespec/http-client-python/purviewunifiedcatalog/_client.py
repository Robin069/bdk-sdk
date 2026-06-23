# coding=utf-8

from copy import deepcopy
import sys
from typing import Any, TYPE_CHECKING

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import PurviewUnifiedCatalogClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .operations import (
    BusinessDomainOperations,
    CriticalDataElementsOperations,
    DataAssetsOperations,
    DataColumnsOperations,
    DataProductsOperations,
    OkrOperations,
    PoliciesOperations,
    TermsOperations,
)

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self  # type: ignore

if TYPE_CHECKING:
    from corehttp.credentials import TokenCredential


class PurviewUnifiedCatalogClient:  # pylint: disable=too-many-instance-attributes
    """Creates a data plane client for Purview Unified Catalog.

    :ivar critical_data_elements: CriticalDataElementsOperations operations
    :vartype critical_data_elements:
     purviewunifiedcatalog.operations.CriticalDataElementsOperations
    :ivar data_assets: DataAssetsOperations operations
    :vartype data_assets: purviewunifiedcatalog.operations.DataAssetsOperations
    :ivar data_products: DataProductsOperations operations
    :vartype data_products: purviewunifiedcatalog.operations.DataProductsOperations
    :ivar business_domain: BusinessDomainOperations operations
    :vartype business_domain: purviewunifiedcatalog.operations.BusinessDomainOperations
    :ivar terms: TermsOperations operations
    :vartype terms: purviewunifiedcatalog.operations.TermsOperations
    :ivar okr: OkrOperations operations
    :vartype okr: purviewunifiedcatalog.operations.OkrOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: purviewunifiedcatalog.operations.PoliciesOperations
    :ivar data_columns: DataColumnsOperations operations
    :vartype data_columns: purviewunifiedcatalog.operations.DataColumnsOperations
    :param credential: Credential used to authenticate requests to the service. Required.
    :type credential: ~corehttp.credentials.TokenCredential
    :keyword endpoint: The endpoint of the Purview Unified Catalog service. Example:
     `https://api.purview-service.microsoft.com/ <https://api.purview-service.microsoft.com/>`_.
     Required. Note that overriding this default value may result in unsupported behavior.
    :paramtype endpoint: str
    :keyword api_version: The API version to use for this operation. Known values are
     "2026-03-20-preview" and None. Default value is None. If not set, the operation's default API
     version will be used. Note that overriding this default value may result in unsupported
     behavior.
    :paramtype api_version: str
    """

    def __init__(self, credential: "TokenCredential", **kwargs: Any) -> None:
        _endpoint = "{endpoint}/datagovernance/catalog"
        self._config = PurviewUnifiedCatalogClientConfiguration(credential=credential, **kwargs)

        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.critical_data_elements = CriticalDataElementsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_assets = DataAssetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_products = DataProductsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.business_domain = BusinessDomainOperations(self._client, self._config, self._serialize, self._deserialize)
        self.terms = TermsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.okr = OkrOperations(self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_columns = DataColumnsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
