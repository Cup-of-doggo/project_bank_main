from datetime import datetime
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
    elif 18 <= int(current_time.hour) < 0:
        return "Добрый вечер"
    else:
        return "Добрый вечер"
