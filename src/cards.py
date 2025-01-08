from src.file_reader import excel_reader


def card_number_reader(data:dict):
    """возвращает последние 4 цифры номера карты"""
    return data.get('Номер карты')


def expenses_sum(data: list[dict]) -> int:
    """возвращает сумму расходов"""
    expenses = []
    expense_sum = 0
    for data_dicts in data:
        if data_dicts.get('Сумма операции') < 0:
            expenses.append(data_dicts.get('Сумма операции'))
        for expense in expenses:
            expense_sum -= expense
    return expense_sum


def cashback(data: list[dict]):
    """возвращает кэшбек"""
    buyings = []
    cashback = 0
    for data_dicts in data:
        if data_dicts.get('Категория') != "переводы":
            buyings.append(data_dicts.get('Сумма операции'))
        for expense in buyings:
            cashback = int(expense / 100) + int(expense / 100 * (-2))
    return cashback
