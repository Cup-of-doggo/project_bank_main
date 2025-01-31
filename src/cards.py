def card_number_reader(dataframe):
    """возвращает последние 4 цифры номера карты"""
    return dataframe['Номер карты'].drop_duplicates()


def expenses_sum(dataframe):
    """возвращает сумму расходов"""
    expenses = []
    expense_sum = 0
    for data in dataframe['Сумма операции']:
        if data < 0:
            expenses.append(data)
    for expense in expenses:
        expense_sum -= expense
    return expense_sum


def cashback(dataframe):
    """возвращает кэшбек"""
    buyings = []
    cashback = 0
    for data in dataframe['Категория']:
        if data != 'Переводы' and data != 'Пополнения':
            buyings.append(dataframe['Сумма операции'])
    for expense in buyings:
          cashback = expense / 100 + expense / 100 * (-2)
    return cashback
