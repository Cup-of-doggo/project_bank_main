from unittest.mock import patch

import pytest

from src.services import simple_search

@pytest.fixture
def test_list_dict():
    return [{}]

@patch("input")
def test_simple_search(mock_input,test_list_dict):
    mock_input.return_value = 'something'

    assert  simple_search(test_list_dict,mock_input) == [{}]