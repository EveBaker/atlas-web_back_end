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
        return False


def  authorization_header(self, request=None) -> str:
    """Gets authorization header from the request"""
    return None


def current_user(self, request=None) -> TypeVar('User'):
    """Gets user from request"""
    return None