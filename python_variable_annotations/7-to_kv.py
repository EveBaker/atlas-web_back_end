#!/usr/bin/env python3

"""tuple"""

from typing import Union, Tuple

def tp_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple and string"""
    return (k, float(v ** 2))
