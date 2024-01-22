#!/usr/bin/env python3
"""
manage the API authentification
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage the API authentification"""
    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """checks if the path needs authentication"""
        if path is None or not exclude_paths:
            return True

        """Ensures path ends with /"""
        path = path if path.endswith('/') else path + '/'

        """Checks if path is in exclude_paths"""
        for exclude_paths in exclude_paths:
            if path == exclude_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Gets authorization header from the request"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets user from request"""
        return None
