#!/usr/bin/env python3
"""making multiplier"""

def make_multiplier(multiplier: float):
    def inner_function(number: float) -> float:
        return number * multiplier
    
    return inner_function