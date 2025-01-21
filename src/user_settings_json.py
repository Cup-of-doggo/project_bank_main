import os
import requests
from dotenv import load_dotenv


load_dotenv()


def currency_rate():
    """возвращает актуальный курс валют"""
    url = "https://api.exchangerate.host/live?access_key=734d4d474e3b78dc4f151803f5bf6d20"
    access_key = os.getenv('API_KEY')
    headers = {"access_key": access_key,
     "callback": "CALLBACK_FUNCTION",
     "source": "RUB",
     "currencies": "USD,AUD,CAD,PLN,MXN",
     "format": "1"}
    response = requests.request("GET", url, headers=headers)
    return response.json()['quotes']


def stocks_cost(ticker):
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

print(currency_rate())