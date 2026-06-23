# coding=utf-8

from typing import Any, Literal, TYPE_CHECKING

from corehttp.runtime import policies

from ._version import VERSION

if TYPE_CHECKING:
    from corehttp.credentials import TokenCredential


class PurviewUnifiedCatalogClientConfiguration:
    """Configuration for PurviewUnifiedCatalogClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

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
        endpoint: Literal["https://api.purview-service.microsoft.com/"] = kwargs.pop(
            "endpoint", "https://api.purview-service.microsoft.com/"
        )
        api_version: str = kwargs.pop("api_version", "2026-03-20-preview")

        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.endpoint = endpoint
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://purview.azure.net/.default"])
        kwargs.setdefault("sdk_moniker", "purviewunifiedcatalog/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(
                self.credential,
                *self.credential_scopes,
                auth_flows=[
                    {
                        "authorizationUrl": "https://login.microsoftonline.com/common/oauth2/authorize",
                        "scopes": [{"value": "https://purview.azure.net/.default"}],
                        "type": "implicit",
                    }
                ],
                **kwargs
            )
