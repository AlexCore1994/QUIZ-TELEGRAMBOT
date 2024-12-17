import os
import random
import nest_asyncio
nest_asyncio.apply()

import asyncio
class AsyncCounter:
    def __init__(self, initial=0):
        self._value = initial
        self._lock = asyncio.Lock()

    async def increment(self):
        async with self._lock:
            self._value += 1
            print(f"Incremented: {self._value}")

    async def decrement(self):
        async with self._lock:
            self._value -= 1
            print(f"Decremented: {self._value}")

    async def get_value(self):
        async with self._lock:
            return self._value

async def worker(counter, increments, decrements):
    for _ in range(increments):
        await counter.increment()
    for _ in range(decrements):
        await counter.decrement()

async def main():
    counter = AsyncCounter()

    # Создаем несколько задач, которые будут работать с одним и тем же счетчиком
    tasks = [
        worker(counter, 5, 3),
        worker(counter, 2, 4),
        worker(counter, 3, 3)
    ]

    await asyncio.gather(*tasks)

    final_value = await counter.get_value()
    print(f"Final counter value: {final_value}")

# Запуск основного цикла событий
asyncio.run(main())