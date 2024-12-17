import nest_asyncio
nest_asyncio.apply()

import asyncio
async def task(name, duration):
    try:
        print(f"Task {name} started, will take {duration} seconds.")
        await asyncio.sleep(duration)
        if duration > 2:
            raise ValueError(f"Task {name} encountered an error due to long duration.")
        print(f"Task {name} completed successfully.")
    except Exception as e:
        print(f"Task {name} failed with error: {e}")

async def main():
    # Создаем список задач
    tasks = [
        task("A", 1),
        task("B", 3),
        task("C", 2)
    ]

    # Запускаем задачи параллельно и ждем их завершения
    await asyncio.gather(*tasks)

# Запускаем основной цикл 
asyncio.run(main())