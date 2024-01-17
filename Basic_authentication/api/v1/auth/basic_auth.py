#!/usr/bin/env python3
"""Module of Basic_auth
"""
from .auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return the Base64 part of the Authorization header."""
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the decoded value of a Base64 string."""
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
