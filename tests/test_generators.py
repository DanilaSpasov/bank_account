from tests.conftests import transaction_generators_list
from src.generators import filter_by_currency


def test_filter_by_currency_usd(transaction_generators_list):
    result = list(filter_by_currency(transaction_generators_list, "USD"))
    assert len(result) == 3
    for currency_name in result:
        assert currency_name["operationAmount"]["currency"]["name"] == "USD"

def test_filter_by_currency_rub(transaction_generators_list):
    result = list(filter_by_currency(transaction_generators_list, "руб."))
    assert len(result) == 2
    for currency_name in result:
        assert currency_name["operationAmount"]["currency"]["name"] == "руб."

def test_filter_by_currency_eur(transaction_generators_list):
    result = list(filter_by_currency(transaction_generators_list, "EUR"))
    assert result == []

