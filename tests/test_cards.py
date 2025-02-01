from src.cards import card_number_reader, expenses_sum, cashback
from src.file_reader import excel_reader
import pandas as pd


data = {'Дата операции': '04.01.2018 14:05:08', 'Дата платежа': '06.01.2018',
                        'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -1065.9,
                        'Валюта операции': 'RUB', 'Сумма платежа': -1065.9, 'Валюта платежа': 'RUB',
                        'Кэшбэк': 'nan', 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Пятёрочка',
                        'Бонусы (включая кэшбэк)': 21, 'Округление на инвесткопилку': 0,
                        'Сумма операции с округлением': 1065.9}

dataframe = pd.DataFrame(data=data, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])


def test_card_number_reader():
    card_number_reader(dataframe)
    assert '*7197'


def test_expenses_sum():
    expenses_sum(excel_reader("operations.xlsx"))
    assert 27774243135.545387


def test_cashback():
    cashback(dataframe)
    assert 11