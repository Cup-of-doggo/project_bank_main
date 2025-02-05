import os
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional


def log(filename=None):
    """выводит имя функции и тип ошибки(при наличии) в файл(или консоль, если файл не указан)"""
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if filename is None:
                    print(f'{func.__name__} все ок \nРезультат: {result}')
                elif filename is not None:
                    with open(os.path.abspath(filename), "a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} все ок \nРезультат: {result}')
                return result

            except Exception as err:

                if filename is None:
                    return print(f'{func.__name__} Ошибка {err}\nВходные параметры {args}, {kwargs}')
                elif filename is not None:
                    with open(os.path.abspath(filename), "a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} Ошибка {err}\nВходные параметры {args}, {kwargs}')

        return wrapper
    return inner


def category_spending(data: list[dict], category: str, date: Optional[str] = None):
    """возвращает список отфильтрованный по тратам по категории"""
    if date:
        current_date = datetime.strptime(date, "%d/%m/%Y") if date else datetime.today()
    else:
        current_date = datetime.now()
    start_date = current_date - timedelta(days=90)
    filtered_data = [
        transaction for transaction in data
        if transaction['Категория'] == category and
           start_date <= datetime.strptime(transaction['Дата операции'], "%d.%m.%Y %H:%M:%S") <= current_date
    ]
    return filtered_data