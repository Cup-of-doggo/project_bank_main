from src.cards import card_number_reader, expenses_sum, cashback
from src.filters import top
from src.user_settings_json import currency_rate, stocks_cost
from src.utils import greetings


def main(dataframe):
    """основная функция отвечающая за главную страницу"""
    {
        "greeting":greetings(),
        "cards": [
            {
                "last_digits": card_number_reader(dataframe),
                "total_spent": expenses_sum(dataframe),
                "cashback": cashback(dataframe)
            },
            {
                "last_digits": card_number_reader(dataframe),
                "total_spent": expenses_sum(dataframe),
                "cashback": cashback(dataframe)
            }
                  ],
        "top_transactions": top(dataframe),
        "currency_rates": currency_rate(),
        "stock_prices": [
            {
                "stock": "AAPL",
                "price": stocks_cost("AAPL")
            },
            {
                "stock": "AMZN",
                "price": stocks_cost("AMZN")
            },
            {
                "stock": "GOOGL",
                "price": stocks_cost("GOOGL")
            },
            {
                "stock": "MSFT",
                "price": stocks_cost("MSFT")
            },
            {
                "stock": "TSLA",
                "price": stocks_cost("TSLA")
            }
        ]
    }
