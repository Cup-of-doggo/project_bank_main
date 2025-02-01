from src.filters import top
from tests.test_cards import dataframe


def test_top():
    assert top(dataframe) ==[{
            "date": '04.01.2018 14:05:08',
            "amount": -1065.9,
            "category": 'Супермаркеты',
            "description": 'Пятёрочка'
        },{
            "date": '04.01.2018 14:05:08',
            "amount": -1065.9,
            "category": 'Супермаркеты',
            "description": 'Пятёрочка'
        },{
            "date": '04.01.2018 14:05:08',
            "amount": -1065.9,
            "category": 'Супермаркеты',
            "description": 'Пятёрочка'
        },{
            "date": '04.01.2018 14:05:08',
            "amount": -1065.9,
            "category": 'Супермаркеты',
            "description": 'Пятёрочка'
        }]