#!/usr/bin/env python3
"""Ejecuta múltiples tareas asíncronas usando task_wait_random y
devuelve sus resultados en orden de finalización."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Ejecuta task_wait_random n veces con max_delay.
    Devuelve la lista de retardos en orden ascendente
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
