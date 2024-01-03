#!/usr/bin/env python3
"""making multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function."""
    def multiplier_function(number: float) -> float:
        return number * multiplier

    return multiplier_function
