#!/usr/bin/env python3
"""Crea y devuelve una tarea asíncrona (asyncio.Task)
que ejecuta wait_random(max_delay)."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Crea y retorna un asyncio.Task que ejecuta
    wait_random(max_delay).
    '''
    return asyncio.create_task(wait_random(max_delay))
