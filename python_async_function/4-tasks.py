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
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    for delay in delays:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)

    return sorted_delays
