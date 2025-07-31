#!/usr/bin/env python3
"""
This module contains a function similar to wait_n but using task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n tasks using task_wait_random and return
    delays in ascending order.

    Args:
        n (int): Number of tasks to create
        max_delay (int): Maximum delay for each task

    Returns:
        List[float]: List of all delays in ascending order
        without using sort()
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
