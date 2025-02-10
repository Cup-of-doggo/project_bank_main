from src.cards import get_cards

import pandas as pd


data = {'Дата операции': '04.01.2018 14:05:08', 'Дата платежа': '06.01.2018',
                        'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -1065.9,
                        'Валюта операции': 'RUB', 'Сумма платежа': -1065.9, 'Валюта платежа': 'RUB',
                        'Кэшбэк': 'nan', 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Пятёрочка',
                        'Бонусы (включая кэшбэк)': 21, 'Округление на инвесткопилку': 0,
                        'Сумма операции с округлением': 1065.9}

dataframe = pd.DataFrame(data=data, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])

def test_get_cards():
    assert get_cards(dataframe) == [{'last_digits': '*7197',
                                     'total_spent': -14922.600000000002,
                                     'cashback': 'nannannannannannannannannannannannannannan'}]
