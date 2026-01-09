import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from tests.conftests import transaction_generators_list


def test_filter_by_currency_usd(transaction_generators_list):
    """Проверка фильтрации транзакций по валюте USD: ожидается 3 элемента с валютой "USD"."""
    result = list(filter_by_currency(transaction_generators_list, "USD"))
    assert len(result) == 3
    for currency_name in result:
        assert currency_name["operationAmount"]["currency"]["name"] == "USD"


def test_filter_by_currency_rub(transaction_generators_list):
    """Проверка фильтрации транзакций по валюте руб.: ожидается 2 элемента с валютой "руб."."""
    result = list(filter_by_currency(transaction_generators_list, "руб."))
    assert len(result) == 2
    for currency_name in result:
        assert currency_name["operationAmount"]["currency"]["name"] == "руб."


def test_filter_by_currency_eur(transaction_generators_list):
    """Проверка фильтрации транзакций по валюте EUR: ожидается пустой список (нет транзакций в EUR)."""
    result = list(filter_by_currency(transaction_generators_list, "EUR"))
    assert result == []


def test_transaction_descriptions_single_transaction_():
    """Проверка на одну транзакцию в небольшом списке с одним словарем."""
    transactions = [{"description": "Одно описание"}]
    gen = transaction_descriptions(transactions)
    assert list(gen) == ["Одно описание"]


@pytest.mark.parametrize(
    "transactions,expected",
    [
        ([{"description": "Одно описание"}], ["Одно описание"]),
        ([{"description": "Первый"}, {"description": "Второй"}], ["Первый", "Второй"]),
        ([], []),  # Пустой список
        ([{"description": ""}], [""]),
    ],
)
def test_transaction_descriptions_different_transactions(transactions, expected):
    """
    Проверка генератора transaction_descriptions на различных наборах транзакций.

    Тестируемые сценарии:
    - Одна транзакция с обычным описанием
    - Несколько транзакций с разными описаниями
    - Пустой список транзакций
    - Транзакция с пустым описанием
    """
    gen = transaction_descriptions(transactions)
    assert list(gen) == expected


def test_transaction_descriptions_all(transaction_generators_list):
    """Проверяет несколько транзакций — все описания возвращаются."""
    gen = transaction_descriptions(transaction_generators_list)
    result = list(gen)
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_empty():
    """Проверяет пустой список — пустой итератор."""
    gen = transaction_descriptions([])
    result = list(gen)
    assert result == []


def test_transaction_descriptions_next(transaction_generators_list):
    """Проверка поведения генератора на next()."""
    gen = transaction_descriptions(transaction_generators_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    remaining = list(gen)
    assert remaining == ["Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]


def test_card_number_generator_min():
    """Проверка минимальное значение диапазона (0000 0000 0000 0001)."""
    gen = card_number_generator(1, 1)
    card = next(gen)
    assert card == "0000 0000 0000 0001"


def test_card_number_generator_max():
    """Тест: максимальное возможное значение (9999...9999)."""
    gen = card_number_generator(9999999999999999, 9999999999999999)
    card = next(gen)
    assert card == "9999 9999 9999 9999"


def test_card_number_generator_random():
    """Проверка заданного значения диапазона (0000 0000 0000 0012)."""
    gen = card_number_generator(12, 12)
    card = next(gen)
    assert card == "0000 0000 0000 0012"


def test_card_number_generator_single_value():
    """Проверка на start == stop, чтобы получился всегда один и тот же номер."""
    value = 1234567890123456
    gen = card_number_generator(value, value)
    card = next(gen)
    assert card == "1234 5678 9012 3456"


def test_card_number_generator_start_greater_than_stop():
    """Проверка start > stop, что вызовет ValueError."""
    with pytest.raises(ValueError, match="start должен быть <= stop"):
        gen = card_number_generator(100, 50)
        next(gen)


def test_card_number_generator_start_greater_than_max():
    """Проверка start больше, чем 16-значное."""
    with pytest.raises(ValueError, match="start не может быть больше 16 цифр"):
        gen = card_number_generator(10000000000000000, 1)
        next(gen)


def test_card_number_generator_stop_greater_than_max():
    """Проверка start больше, чем 16-значное."""
    with pytest.raises(ValueError, match="stop не может быть больше 16 цифр"):
        gen = card_number_generator(1, 10000000000000000)
        next(gen)


def test_card_number_generator_multiple_calls():
    """Проверка, что генератор можно вызвать несколько раз."""
    gen = card_number_generator(1000, 1005)
    cards = [next(gen) for _ in range(3)]
    assert len(cards) == 3
