from __future__ import annotations

import base64
import time
import uuid
from pathlib import Path

import jwt
import requests
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from .config import Settings


def get_kerberos_session() -> requests.Session:
    """Stub for getting a Kerberos session."""
    return requests.Session()


def _base64url(data: bytes) -> str:
    """Encode data to base64url."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def _load_pem_private_key(path: Path) -> RSAPrivateKey:
    """Load a PEM private key from a file."""
    with open(path, "rb") as key_file:
        key = serialization.load_pem_private_key(key_file.read(), password=None)
    if not isinstance(key, RSAPrivateKey):
        raise TypeError("Expected an RSA private key")
    return key


def _load_pem_certificate(path: Path) -> x509.Certificate:
    """Load a PEM certificate from a file."""
    with open(path, "rb") as cert_file:
        return x509.load_pem_x509_certificate(cert_file.read())


def get_client_assertion(
    settings: Settings,
    private_key_path: Path,
    certificate_path: Path,
    validity_seconds: int = 600,
) -> str:
    """Get a client assertion for authentication."""
    private_key = _load_pem_private_key(private_key_path)
    certificate = _load_pem_certificate(certificate_path)
    x5t = _base64url(certificate.fingerprint(hashes.SHA1()))
    now = int(time.time())

    payload = {
        "iss": settings.client_id,
        "sub": settings.client_id,
        "aud": settings.token_url,
        "exp": now + validity_seconds,
        "nbf": now,
        "jti": str(uuid.uuid4()),
    }

    headers = {
        "typ": "JWT",
        "alg": "RS256",
        "x5t": x5t,
    }

    return jwt.encode(payload, private_key, headers=headers, algorithm="RS256")


def get_access_token(settings: Settings, client_assertion: str) -> dict:
    """Get an access token for the client assertion."""
    payload = {
        "tenant": settings.tenant_id,
        "client_id": settings.client_id,
        "resource": settings.resource,
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion,
        "grant_type": "client_credentials",
    }
    response = requests.post(
        url=settings.token_url,
        data=payload,
    )
    response.raise_for_status()
    return response.json()
