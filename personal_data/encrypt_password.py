#!/usr/bin/env python3
"""encrypt passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with salt using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
