from unittest.mock import patch

from src.user_settings_json import currency_rate_usd,currency_rate_eur, stocks_cost


@patch('requests.request')
def test_currency_rate(mock_get):
    mock_get.return_value.json.return_value = {"result": 8221.37}
    assert currency_rate_usd() == 8221.37

@patch('requests.request')
def test_stocks_cost(mock_get):
    mock_get.return_value.json.return_value = {'Global Quote':{'05. price':1}}
    assert stocks_cost('AAPL') == 1