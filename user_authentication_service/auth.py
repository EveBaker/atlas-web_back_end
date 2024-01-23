#!/usr/bin/env python3
"""
    Encrypt a string
"""
import bcrypt

def _hash_password(password: str) -> bytes:
    """hashes a pass for storing"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
