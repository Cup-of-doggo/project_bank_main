import re


def simple_search(dataframe, user_input = input('Введите слова для поиска: ').capitalize()):
    """Ищет транзакиию по ключевому слову"""
    founded_string = []
    regex = re.compile(user_input, re.IGNORECASE)
    for _, row in dataframe.iterrows():
        for value in row:
            if regex.search(str(value)):
                founded_string.append(row.to_dict())
                break
    if len(founded_string) == 0:
        return 'Ничего не найдено'
    else:
        return founded_string