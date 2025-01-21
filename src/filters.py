def top(data: list[dict]):
    """возвращает топ 5 транзакций по сумме платежа"""
    transaction = []
    for data_dicts in data:
        if len(transaction) < 5:
            transaction.append(data_dicts)
    return transaction
