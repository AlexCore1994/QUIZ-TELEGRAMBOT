import nest_asyncio
nest_asyncio.apply()

import asyncio
async def calculate(expression):
    try:
        # Используем eval для вычисления выражения
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

async def main():
    print("Асинхронный калькулятор. Введите 'exit' для выхода.")
    while True:
        expression = input("Введите математическое выражение: ")
        if expression.lower() == 'exit':
            break
        await calculate(expression)

# Запуск основного цикла
asyncio.run(main())