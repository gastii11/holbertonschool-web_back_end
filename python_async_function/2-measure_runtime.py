#!/usr/bin/env python3
"""Medir el tiempo promedio de ejecución de funciones asíncronas en Python"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Ejecuta wait_n y mide el tiempo'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
