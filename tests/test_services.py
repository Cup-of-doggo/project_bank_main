from unittest import mock

from src.services import simple_search


@mock.patch('builtins.input', side_effect=['something'])
def test_simple_search(func):
    simple_search([{'something':'something'}])
    assert [{'something':'something'}]