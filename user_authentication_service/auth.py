#!/usr/bin/env python3
"""
    Encrypt a string
"""
import bcrypt
from user import User
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user"""
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user


def valid_login(self, email: str, password: str) -> bool:
    """Check if the provided credentials are valid."""
    try:
        user = self._db.find_user_by(email=email)
    except Exception:
        return False

    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return True
    return False


def _hash_password(password: str) -> bytes:
    """hashes a pass for storing"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
