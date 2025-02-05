from datetime import timedelta

import pandas as pd
from win32ctypes.pywin32.pywintypes import datetime

from src.cards import card_number_reader, expenses_sum, cashback
from src.file_reader import excel_reader
from src.filters import top
from src.user_settings_json import stocks_cost, currency_rate_eur, currency_rate_usd
from src.utils import greetings


df = excel_reader('operations.xlsx')


def main(dataframe):
    """основная функция отвечающая за главную страницу"""
    main = []
    start_date = datetime.today() - timedelta(days=10)
    end_date = datetime.today()
    dataframe_date = pd.to_datetime(dataframe['Дата операции'])
    filtered_df = dataframe[(dataframe_date >= start_date) & (dataframe_date <= end_date)]
    sorted_df = filtered_df.sort_values(by='Дата операции')
    for _, row in dataframe[card_number_reader(sorted_df),expenses_sum(sorted_df),cashback(sorted_df)].iterrows():
        card_info = {
            "last_digits": row[card_number_reader(sorted_df)],
            "total_spent": row[expenses_sum(sorted_df)],
            "cashback": row[cashback(sorted_df)]
        }
    main.append({
        "greeting":greetings(),
        "cards": card_info
    })
    main.append({
        "top_transactions": top(sorted_df),
        "currency_rates": [currency_rate_eur(),currency_rate_usd()],
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
    })
    return main

print(main(df))