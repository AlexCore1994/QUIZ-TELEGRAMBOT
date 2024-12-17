import os
import random
import nest_asyncio
nest_asyncio.apply()

import asyncio
async def find_files(directory, file_extension):
    """Асинхронно ищет файлы с заданным расширением в указанном каталоге."""
    loop = asyncio.get_event_loop()
    files = await loop.run_in_executor(None, lambda: [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files
        if file.endswith(file_extension)
    ])
    return files

async def main():
    directory = '/path/to/your/directory'
    file_extension = '.txt'

    print(f"Поиск файлов с расширением {file_extension} в каталоге {directory}...")
    files = await find_files(directory, file_extension)

    if files:
        print(f"Найдено {len(files)} файлов:")
        for file in files:
            print(file)
    else:
        print("Файлы не найдены.")

# Запуск асинхронной программы
if __name__ == '__main__':
    asyncio.run(main())