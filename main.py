
from typing import Optional

import pandas as pd
from win32ctypes.pywin32.pywintypes import datetime

from src.cards import get_cards
from src.file_reader import excel_reader
from src.filters import top
from src.user_settings_json import stocks_cost, currency_rate_eur, currency_rate_usd
from src.utils import greetings


df = excel_reader('operations.xlsx')


def main(dataframe, date: Optional[str] = None):
    """основная функция отвечающая за главную страницу"""
    main_list = []

    if date is None:
        start_date = datetime.today().strftime("%Y-%m-01 00:00:00")
        end_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    else:
        start_date = datetime.strptime(date,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-01 00:00:00")
        end_date = date

    dataframe['Дата операции']  = pd.to_datetime(dataframe['Дата операции'], dayfirst=True)
    filtered_df = dataframe[(dataframe['Дата операции'] >= start_date) & (dataframe['Дата операции'] <= end_date)]
    sorted_df = filtered_df.sort_values(by='Дата операции')

    main_list.append({
        "greeting":greetings(),
        "cards": get_cards(sorted_df)
    })
    main_list.append({
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
    return main_list

print(main(df,'2021-12-31 16:44:00'))