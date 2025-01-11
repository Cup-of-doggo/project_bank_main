import os
import requests
from dotenv import load_dotenv
from ticker.ticker import company

load_dotenv()


def currency_rate():
    """возвращает актуальный курс валют"""
    url = os.getenv('URL')
    access_key = os.getenv('API_KEY')
    headers = {"access_key": access_key,
     "callback": "CALLBACK_FUNCTION",
     "source": "RUB",
     "currencies": "USD,AUD,CAD,PLN,MXN",
     "format": "1"}
    response = requests.request("GET", url, headers=headers)
    return response.json()['quotes']


def stocks_cost(ticker = company):
    """Возвращает стоимость акций"""
    url = "https://www.alphavantage.co/query"
    api_key = os.getenv('API_KEY_2')
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": api_key
    }
    response = requests.request("GET", url, params=params)
    return response.json()
