from __future__ import annotations

import time
from pathlib import Path

import requests

from .auth import get_kerberos_session, get_client_assertion, get_access_token
from .config import Settings


class PurviewSession:
    """Lazily-authenticating transport session for the Purview API.

    Authentication is deferred until the first request.  On a 401 response
    the token is forcibly refreshed and the request retried once.
    """

    def __init__(
        self,
        settings: Settings,
        private_key_path: Path,
        certificate_path: Path,
    ) -> None:
        self.settings = settings
        self.private_key_path = private_key_path
        self.certificate_path = certificate_path
        self._access_token: str | None = None
        self._expires_at: float | None = None
        self._http_session: requests.Session | None = None

    # ------------------------------------------------------------------
    # Authentication (lazy)
    # ------------------------------------------------------------------

    def _authenticate(self) -> None:
        assertion = get_client_assertion(
            self.settings, self.private_key_path, self.certificate_path
        )
        token_data = get_access_token(self.settings, assertion)
        self._access_token = token_data["access_token"]
        self._expires_at = float(token_data["expires_on"])

    def _check_expired(self) -> bool:
        if self._expires_at is None:
            return True
        return time.time() > self._expires_at

    def _ensure_authenticated(self) -> None:
        if self._access_token is None or self._check_expired():
            self._authenticate()

    # ------------------------------------------------------------------
    # Transport
    # ------------------------------------------------------------------

    def request(
        self,
        method: str,
        base_path: str,
        path: str,
        api_version: str,
        *,
        json: dict | None = None,
        params: dict | None = None,
    ) -> dict | None:
        """Issue an HTTP request with lazy authentication.

        Returns parsed JSON, or ``None`` for empty (204) responses.
        """
        self._ensure_authenticated()

        url = f"{self.settings.endpoint}{base_path}{path}"
        merged_params: dict[str, str] = {"api-version": api_version}
        if params:
            merged_params.update(params)

        if self._http_session is None:
            self._http_session = get_kerberos_session()

        response = self._http_session.request(
            method,
            url,
            params=merged_params,
            json=json,
            headers={"Authorization": f"Bearer {self._access_token}"},
        )

        if response.status_code == 401:
            self._authenticate()  # force refresh
            response = self._http_session.request(
                method,
                url,
                params=merged_params,
                json=json,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )

        response.raise_for_status()

        if response.status_code == 204 or not response.content:
            return None
        return response.json()
