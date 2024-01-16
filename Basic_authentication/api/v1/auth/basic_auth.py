#!/usr/bin/env python3
"""Module of Basic_auth
"""
from .auth import Auth


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
