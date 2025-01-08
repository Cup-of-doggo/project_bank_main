def top(data: list[dict],payment: int ):
    """возвращает топ 5 транзакций по сумме платежа"""
    transaction = []
    for data_dicts in data:
        if data_dicts.get('Сумма операции') == payment and len(transaction) < 5:
            transaction.append(data_dicts)
    return transaction
