from unittest.mock import patch

from src.user_settings_json import currency_rate, stocks_cost


@patch('requests.request')
def test_currency_rate(mock_get):
    mock_get.return_value.json.return_value = {"quotes": "8221.37"}
    assert currency_rate() == "8221.37"

@patch('requests.request')
def test_stocks_cost(mock_get):
    mock_get.return_value.json.return_value = {}
    assert stocks_cost('AAPL') == {}