from unittest.mock import patch

import pandas as pd

from src.file_reader import read_csv
from src.file_reader import read_xlsx
from tests.conftests import test_data_file_reader


@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv, test_data_file_reader):
    """Проверяет вызов первой транзакции из тестовых данных при обработке .csv файла"""
    mock_df = pd.DataFrame(test_data_file_reader)
    mock_read_csv.return_value = mock_df

    result = read_csv("test.csv")

    assert isinstance(result, list)
    assert len(result) == len(test_data_file_reader)

    first_entry = result[0]
    assert first_entry["id"] == "650703"
    assert first_entry["amount"] == 16210
    assert first_entry["currency_code"] == "PEN"


@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_read_csv_file_not_found(mock_read_csv):
    """Проверяет вызов ошибки file not found при обработке .csv файла"""
    result = read_csv("missing.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_xlsx_success(mock_read_excel, test_data_file_reader):
    """Проверяет вызов первой транзакции из тестовых данных при обработке .xlsx файла"""
    mock_df = pd.DataFrame(test_data_file_reader)
    mock_read_excel.return_value = mock_df

    result = read_xlsx("test.xlsx")

    assert isinstance(result, list)
    assert len(result) == 2

    first_entry = result[0]
    assert first_entry["id"] == "650703"
    assert first_entry["amount"] == 16210
    assert first_entry["currency_code"] == "PEN"


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_read_xlsx_file_not_found(mock_read_excel):
    """Проверяет вызов ошибки file not found при обработке .xlsx файла"""
    result = read_xlsx("missing.xlsx")
    assert result == []


@patch("pandas.read_excel", side_effect=Exception("Ошибка"))
def test_read_xlsx_other_exception(mock_read_excel):
    """Проверяет вызов другой ошибки при обработке .xlsx файла"""
    result = read_xlsx("error.xlsx")
    assert result == []
