import re


def simple_search(dataframe, user_input = input('Введите слова для поиска: ').capitalize()):
    """Ищет транзакиию по ключевому слову"""
    founded_string = []
    regex = re.compile(user_input, re.IGNORECASE)
    if regex.match:
        founded_string.append(dataframe[user_input])
        return founded_string
    else:
        return 'ничего не найдено'
