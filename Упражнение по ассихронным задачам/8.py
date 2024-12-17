import os
import random
import nest_asyncio
nest_asyncio.apply()

import asyncio
async def worker(task_id, delay):
    print(f"Task {task_id} started")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed")

async def main():
    # Создаем список задач
    tasks = [
        worker(1, 2),
        worker(2, 3),
        worker(3, 1)
    ]

    # Запускаем задачи параллельно и ждем их завершения
    await asyncio.gather(*tasks)

# Запускаем главный цикл событий
asyncio.run(main())