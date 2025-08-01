#!/usr/bin/env python3
"""
This module contains a coroutine that uses async comprehension
to collect random numbers from an async generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator.

    Returns:
        List[float]: List of 10 random numbers between 0 and 10
    """
    return [i async for i in async_generator()]
