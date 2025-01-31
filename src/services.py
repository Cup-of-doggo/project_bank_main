from src.file_reader import excel_reader


def simple_search(dataframe):
    """Ищет транзакиию по ключевому слову"""
    user_input = str(input('Введите слова для поиска: '))
    founded_string = []
    if user_input in dataframe['Категория'].values or user_input in dataframe['Описание'].values:
        founded_string.append('')
    return founded_string

print(simple_search(excel_reader('operations.xlsx')))