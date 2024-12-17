import random
import nest_asyncio
nest_asyncio.apply()

import asyncio
async def async_random_number_generator(count, delay):
    """Асинхронный генератор случайных чисел."""
    for _ in range(count):
        await asyncio.sleep(delay)
        yield random.randint(1, 100)

async def main():
    # Создаем несколько задач для генерации случайных чисел параллельно
    tasks = [
        asyncio.create_task(consume_numbers(1, 5, 1)),
        asyncio.create_task(consume_numbers(2, 5, 1.5)),
        asyncio.create_task(consume_numbers(3, 5, 2))
    ]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)

async def consume_numbers(task_id, count, delay):
    """Функция для потребления чисел из генератора."""
    async for number in async_random_number_generator(count, delay):
        print(f"Task {task_id}: {number}")

# Запуск основного цикла событий
if __name__ == "__main__":
    asyncio.run(main())