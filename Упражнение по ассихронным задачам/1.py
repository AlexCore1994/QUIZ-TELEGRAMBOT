import nest_asyncio
nest_asyncio.apply()

import asyncio
from playwright.async_api import async_playwright

async def print_message_every_second(duration):
    start_time = asyncio.get_event_loop().time()
    while True:
        current_time = asyncio.get_event_loop().time()
        elapsed_time = current_time - start_time
        if elapsed_time >= duration:
            break
        print("Сообщение каждую секунду")
        await asyncio.sleep(1)

async def main():
    await print_message_every_second(10)

# Запуск основного цикла событий
asyncio.run(main())