from freezegun import freeze_time

from src.utils import greetings, category_spending


@freeze_time('2025.01.01')
def test_greetings():
    greetings()
    assert "Доброй ночи"


data =  [{'Дата операции': '22.09.2018 21:35:08', 'Дата платежа': '23.09.2018',
          'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -55.98, 'Валюта операции': 'RUB',
          'Сумма платежа': -55.98, 'Валюта платежа': 'RUB', 'Кэшбэк': 'nan', 'Категория': 'Супермаркеты',
          'MCC': 5411.0, 'Описание': 'Дикси', 'Бонусы (включая кэшбэк)': 1, 'Округление на инвесткопилку': 0,
          'Сумма операции с округлением': 55.98}]
category = 'Супермаркеты'
data_date = '21/12/2018'


def test_category_spending():
    category_spending(data, category, data_date)
    assert data