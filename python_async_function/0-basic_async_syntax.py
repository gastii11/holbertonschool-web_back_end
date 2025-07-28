#!/usr/bin/env python3
'''
Escribe una corrutina asíncrona que tome un argumento entero
(max_delay, con un valor predeterminado de 10) llamado wait_random que
espere un retraso aleatorio entre 0 y max_delay (incluido y valor flotante)
segundos y finalmente lo devuelva.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Retornará un delay aleatorio'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
