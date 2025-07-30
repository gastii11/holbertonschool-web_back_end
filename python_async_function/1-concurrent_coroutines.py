#!/usr/bin/env python3
'''
Función asíncrona que ejecuta múltiples llamadas a wait_random
y devuelve los retardos en orden ascendente sin usar sort().
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Ejecutamos todas las tareas y las procesamos conforme terminan
    '''
    delays = []
    for task in asyncio.as_completed([wait_random(max_delay)
                                      for _ in range(n)]):
        delay = await task
        delays.append(delay)
    return delays
