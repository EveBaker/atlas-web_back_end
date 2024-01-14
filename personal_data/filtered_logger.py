#!/usr/bin/env python3
from typing import List
import re
"""module for filtered logger"""


def filter_datum(fields: List[str], redaction: str, message: str,
                separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+", f"{field}={redaction}", message)
    return message
