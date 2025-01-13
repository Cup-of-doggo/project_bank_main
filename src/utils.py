from datetime import datetime
from typing import Optional
import datetime
import pandas as pd


def greetings():
    """приветствие"""
    current_time = datetime.now()

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
    filtred_data = []
    delta = datetime.timedelta(days=90)

    if date is None:
        start_date = datetime.datetime.today() - delta
        end_date = datetime.datetime.today()

        date_to_use = pd.date_range(
            min(start_date, end_date),
            max(start_date, end_date)
            ).strftime('%d.%m.%Y').tolist()

        for data_inf in data:
            if data_inf['Категория'] == category:
                if data_inf['Дата операции'][0:11] in date_to_use:
                    filtred_data.append(data_inf)
        return filtred_data
    else:
        date_object = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        start_date = date_object - delta
        end_date = date_object

        date_to_use = pd.date_range(
            min(start_date, end_date),
            max(start_date, end_date)
        ).strftime('%d.%m.%Y').tolist()

        for data_inf in data:
            if data_inf['Категория'] == category:
                   if data_inf['Дата операции'][0:11] == date_to_use[0]:
                        filtred_data.append(data_inf)
        return filtred_data
