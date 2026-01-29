import json
from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import json_convertation


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([1, 2, 3]))
def test_valid_json_list(mock_open, mock_exists):
    """Проверяет, что файл существует, содержит валидный список"""
    mock_exists.return_value = True
    result = json_convertation("somefile.json")
    assert result == [1, 2, 3]
    mock_open.assert_called_once_with("somefile.json", "r", encoding="utf-8")


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1}]))
def test_valid_list_of_dicts(mock_open, mock_exists):
    """Проверяет, что файл содержит список словарей"""
    mock_exists.return_value = True
    result = json_convertation("somefile.json")
    assert result == [{"id": 1}]


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='{"invalid": "json}')
def test_invalid_json(mock_open, mock_exists):
    """Проверяет, что файл содержит некорректный JSON"""
    mock_exists.return_value = True
    result = json_convertation("somefile.json")
    assert result == []


@patch("os.path.exists")
def test_file_not_exists(mock_exists):
    """Проверяет, что файл не существует, возвращается пустой список"""
    mock_exists.return_value = False
    result = json_convertation("nonexistent.json")
    assert result == []


@patch("os.path.exists")
@patch("builtins.open", side_effect=OSError("Permission denied"))
def test_os_error_on_open(mock_open, mock_exists):
    """Ошибка при открытии файла — возвращается пустой список"""
    mock_exists.return_value = True
    result = json_convertation("somefile.json")
    assert result == []
