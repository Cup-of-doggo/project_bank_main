from datetime import datetime
from typing import Optional
import datetime

from src.file_reader import excel_reader


def greetings():
    """приветствие"""
    current_time = datetime.datetime.now()

    if 00 <= current_time.hour < 6:
        greeting = "Доброй ночи"
    elif 6 <= current_time.hour < 12:
        greeting = "Доброе утро"
    elif 12 <= current_time.hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_time.hour < 00:
        greeting = "Добрый вечер"

    return greeting


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
