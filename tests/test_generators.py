import random

import pytest

from tests.conftests import transaction_generators_list
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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

def test_transaction_descriptions_single_transaction():
    """Проверка на одну транзакцию в небольшом списке с одним словарем."""
    transactions = [{"description": "Одно описание"}]
    gen = transaction_descriptions(transactions)
    assert list(gen) == ["Одно описание"]

def test_transaction_descriptions_all(transaction_generators_list):
    """Проверяет несколько транзакций — все описания возвращаются."""
    test = transaction_descriptions(transaction_generators_list)
    result = list(test)
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert result == expected

def test_transaction_descriptions_empty():
    """Проверяет пустой список — пустой итератор."""
    gen = transaction_descriptions([])
    result = list(gen)
    assert result == []


def test_transaction_descriptions_next(transaction_generators_list):
    """Проверка поведения генератора на next()."""
    test = transaction_descriptions(transaction_generators_list)
    assert next(test) == "Перевод организации"
    assert next(test) == "Перевод со счета на счет"
    remaining = list(test)
    assert remaining == [
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

def test_card_number_generator_min():
    """Проверка минимальное значение диапазона (0000 0000 0000 0001)."""
    test = card_number_generator(1, 1)
    card = next(test)
    assert card == "0000 0000 0000 0001"

def test_card_number_generator_max():
    """Тест: максимальное возможное значение (9999...9999)."""
    gen = card_number_generator(9999999999999999, 9999999999999999)
    card = next(gen)
    assert card == "9999 9999 9999 9999"

def test_card_number_generator_random():
    """Проверка заданного значения диапазона (0000 0000 0000 0012)."""
    test = card_number_generator(12, 12)
    card = next(test)
    assert card == "0000 0000 0000 0012"

def test_card_number_generator_single_value():
    """Проверка на start == stop, чтобы получился всегда один и тот же номер."""
    value = 1234567890123456
    gen = card_number_generator(value, value)
    card = next(gen)
    assert card == "1234 5678 9012 3456"

#def test_start_greater_than_stop():
#    """Проверка start > stop, что вызовет ValueError."""
#    with pytest.raises(ValueError, match="start должен быть <= stop"):
#        card_number_generator(100, 50)


