import pytest

from src.filter import process_bank_search, process_bank_operations


@pytest.fixture
def test_data_process_bank_search():
    test_data = [
        {
            "id": 1,
            "description": "Перевод организации"
        },
        {
            "id": 2,
            "description": "Оплата услуг"
        },
        {
            "id": 3,
            "description": "перевод на карту"
        },
        {
            "id": 4,
            "description": "Пополнение счёта"
        },
        {
            "id": 5
            # Нет поля description
        }
    ]
    return test_data

@pytest.fixture
def test_data_process_bank_operations():
    return [
        {
            "id": 1,
            "description": "Перевод организации"
        },
        {
            "id": 2,
            "description": "Оплата услуг"
        },
        {
            "id": 3,
            "description": "Перевод на карту"
        },
        {
            "id": 4,
            "description": "Пополнение счёта"
        },
        {
            "id": 5
            # Нет поля description
        }
    ]


@pytest.mark.parametrize("search_term, expected_ids", [
    ("Оплата", [2]),
    ("перевод", [1, 3]),
    ("карт", [3]),
    ("Пополнение", [4]),
    ("", [1, 2, 3, 4]),  # пустая строка — все с description
])
def test_basic_search_cases_search(test_data_process_bank_search, search_term, expected_ids):
    """Проверяет основные сценарии поиска."""
    result = process_bank_search(test_data_process_bank_search, search_term)
    result_ids = [op["id"] for op in result]
    assert sorted(result_ids) == sorted(expected_ids)

def test_no_matches_search(test_data_process_bank_search):
    """Проверяет отсутствие совпадений."""
    result = process_bank_search(test_data_process_bank_search, "Покупка")
    assert len(result) == 0
    assert result == []

def test_empty_data_search():
    """Проверяет пустой список данных."""
    result = process_bank_search([], "Перевод")
    assert len(result) == 0
    assert result == []

def test_missing_description_field_search(test_data_process_bank_search):
    """Проверяет обработку операций без поля description."""
    result = process_bank_search(test_data_process_bank_search, "Пополнение")
    assert len(result) == 1
    assert result[0]["id"] == 4

def test_regex_end_of_string_search(test_data_process_bank_search):
    """Проверяет регулярное выражение: конец строки."""
    result = process_bank_search(test_data_process_bank_search, r"услуг$")
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_case_insensitivity_search(test_data_process_bank_search):
    """Проверяет нечувствительность к регистру."""
    result1 = process_bank_search(test_data_process_bank_search, "перевод")
    result2 = process_bank_search(test_data_process_bank_search, "ПЕРЕВОД")
    result3 = process_bank_search(test_data_process_bank_search, "Перевод")

    assert len(result1) == len(result2) == len(result3) == 2
    ids1 = sorted([op["id"] for op in result1])
    ids2 = sorted([op["id"] for op in result2])
    ids3 = sorted([op["id"] for op in result3])
    assert ids1 == ids2 == ids3

def test_empty_data_operations():
    result = process_bank_operations(
        [],
        ["Перевод", "Оплата"]
    )

    assert result == {
        "Перевод": 0,
        "Оплата": 0
    }
def test_missing_description_field_operations(test_data_process_bank_operations):
    result = process_bank_operations(test_data_process_bank_operations,
        ["Перевод", "Оплата", "Пополнение"]
    )

    assert result == {
        "Перевод": 2,
        "Оплата": 1,
        "Пополнение": 1
    }

def test_multiple_categories_operations(test_data_process_bank_operations):
    result = process_bank_operations(test_data_process_bank_operations,
        ["Перевод", "Оплата", "Пополнение", "Покупка"]
    )

    assert result == {
        "Перевод": 2,
        "Оплата": 1,
        "Пополнение": 1,
        "Покупка": 0
    }