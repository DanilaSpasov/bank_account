from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.external_api import transaction_amount


@patch("os.getenv")
def test_rub_transaction(mock_getenv):
    """Проверяет, что транзакция в RUB возвращает сумму без конвертации."""
    mock_getenv.return_value = "dummy_api_key"
    transaction_list = [{"operationAmount": {"amount": 1000.0, "currency": {"code": "RUB"}}}]

    result = transaction_amount(transaction_list)
    assert result == 1000.0


@patch("os.getenv")
@patch("requests.request")
def test_usd_to_rub_success(mock_request, mock_getenv):
    """Проверяет, что конвертация USD -> RUB (успешный API-ответ)."""
    mock_getenv.return_value = "test_api_key"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 90.5}
    mock_request.return_value = mock_response

    transaction_list = [{"operationAmount": {"amount": 1.0, "currency": {"code": "USD"}}}]

    result = transaction_amount(transaction_list)
    assert result == 90.5


@patch("os.getenv")
@patch("requests.request")
def test_api_error(mock_request, mock_getenv):
    """Проверяет обработку ошибки API (неуспешный статус)."""
    mock_getenv.return_value = "test_api_key"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 55.0}
    mock_request.return_value = mock_response

    transaction_list = [{"operationAmount": {"amount": 1.0, "currency": {"code": "EUR"}}}]

    result = transaction_amount(transaction_list)
    assert result == 55.0


@patch("os.getenv")
@patch("requests.request")
def test_missing_api_key(mock_request, mock_getenv):
    """Проверяет отсутствие API_KEY в окружении и ответ API с ошибкой 401."""
    mock_getenv.return_value = None
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.text = '{"message":"No API key found in request"}'
    mock_request.return_value = mock_response

    transaction_list = [{"operationAmount": {"amount": 1.0, "currency": {"code": "GBP"}}}]

    try:
        transaction_amount(transaction_list)
    except Exception as e:
        assert str(e) == 'Ошибка API: 401, {"message":"No API key found in request"}'


@patch("os.getenv")
def test_missing_currency_code(mock_getenv):
    """Проверяет, что отсутствует поле currency.code."""
    mock_getenv.return_value = "dummy"

    transaction_list = [{"operationAmount": {"amount": 100.0}}]

    with pytest.raises(KeyError):
        transaction_amount(transaction_list)
