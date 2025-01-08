from unittest.mock import patch
from src.file_reader import excel_reader


@patch('pandas.read_excel')
def test_excel_reader(mock_read):
    mock_read.return_value.to_dict.return_value = []
    assert excel_reader(mock_read) == []