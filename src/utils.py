from datetime import datetime
from typing import Optional
import datetime


def greetings():
    """приветствие"""
    current_time = datetime.datetime.now()

    if 0 <= int(current_time.hour) < 6:
        return "Доброй ночи"
    elif 6 <= int(current_time.hour) < 12:
        return "Доброе утро"
    elif 12 <= int(current_time.hour) < 18:
        return "Добрый день"
    else:
        18 <= int(current_time.hour) < 0
        return "Добрый вечер"


def category_spending(data: list[dict], category: str, date: Optional[str] = None):
    """возвращает список отфильтрованный по тратам по категории"""
    if date:
        current_date = datetime.datetime.strptime(date, "%d/%m/%Y") if date else datetime.today()
    else:
        current_date = datetime.datetime.now()
    start_date = current_date - datetime.timedelta(days=90)
    filtered_data = [
        transaction for transaction in data
        if transaction['Категория'] == category and
           start_date <= datetime.datetime.strptime(transaction['Дата операции'], "%d.%m.%Y %H:%M:%S") <= current_date
    ]
    return filtered_data
