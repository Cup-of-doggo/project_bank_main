from unittest.mock import patch
from src.

@patch('requests.request')
def test_currency_rate(mock_get):
    mock_get.return_value.json.return_value = ['quotes']
    assert currency_rate() == "8221.37"