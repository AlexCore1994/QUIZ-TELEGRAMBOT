import os
import random
import nest_asyncio
nest_asyncio.apply()

import asyncio
class AsyncCache:
    def __init__(self):
        self._cache = {}
        self._lock = asyncio.Lock()

    async def set(self, key, value):
        async with self._lock:
            self._cache[key] = value
            print(f"Set {key} = {value}")

    async def get(self, key):
        async with self._lock:
            value = self._cache.get(key, None)
            print(f"Get {key} = {value}")
            return value

# Функция для тестирования работы кэша
async def test_cache():
    cache = AsyncCache()

    # Создаем несколько задач для параллельного выполнения
    await asyncio.gather(
        cache.set('a', 1),
        cache.set('b', 2),
        cache.get('a'),
        cache.get('b'),
        cache.get('c')  # Попытка получить несуществующий ключ
    )

# Запуск теста
asyncio.run(test_cache())