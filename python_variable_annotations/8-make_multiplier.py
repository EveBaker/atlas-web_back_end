#!/usr/bin/env python3
"""making multiplier"""

def make_multiplier(multiplier: float):
    """multiplier"""
    def inner_function(number: float) -> float:
        """function"""
        return number * multiplier
    
    return inner_function