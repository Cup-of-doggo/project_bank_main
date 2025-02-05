import os
import requests
from dotenv import load_dotenv


load_dotenv()


def currency_rate_usd():
    """возвращает актуальный курс валют"""
    url = 'https://api.apilayer.com/exchangerates_data/convert'
    API_KEY = os.getenv('API_KEY')
    headers = {'apikey': API_KEY}
    params = {
        'to': 'RUB',
        'from': 'USD',
        'amount': 1,
    }
    response = requests.request("GET", url, params=params, headers=headers)
    return response.json()['result']


def currency_rate_eur():
    """возвращает актуальный курс валют"""
    url = 'https://api.apilayer.com/exchangerates_data/convert'
    API_KEY = os.getenv('API_KEY')
    headers = {'apikey': API_KEY}
    params = {
        'to': 'RUB',
        'from': 'EUR',
        'amount': 1,
    }
    response = requests.request("GET", url, params=params, headers=headers)
    return response.json()['result']


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
    return response.json()['Global Quote']['05. price']
