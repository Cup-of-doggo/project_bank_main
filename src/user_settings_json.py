import os
import requests
from dotenv import load_dotenv


load_dotenv()


def currency_rate():
    """возвращает актуальный курс валют"""
    url = 'https://api.apilayer.com/exchangerates_data/convert'
    headers = {'apikey': '3SpTa2DEN4SwRs6x46G8LiigAOQqON6C'}
    params = {
        'to': 'RUB',
        'from': 'USD',
        'amount': 1,
    }
    response = requests.request("GET", url, params=params, headers=headers)
    return response.json()


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
