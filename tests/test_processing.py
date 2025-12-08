from src.processing import filter_by_state
from src.processing import sort_by_date
from tests.conftests import transaction_list


def test_filter_by_state_executed(transaction_list):
    """Проверяет корректность фильтрации транзакций по статусу 'EXECUTED'."""
    result = filter_by_state(transaction_list)
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected_result


def test_sort_by_date_descending(transaction_list):
    """Проверяет корректность сортировки транзакций по дате в порядке убывания."""
    result = sort_by_date(transaction_list)
    expected_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected_result


def test_sort_by_date_ascending(transaction_list):
    """Проверяет корректность сортировки транзакций по дате в порядке возрастания."""
    result = sort_by_date(transaction_list, reverse=False)
    expected_result = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected_result
