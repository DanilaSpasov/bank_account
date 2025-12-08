import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567812345678, "1234 56** **** 5678"),
    (1111222233334444, "1111 22** **** 4444"),
])
def test_get_mask_card_number(card_number, expected):
    """Тестирует маскировку номера карты (параметризованный)."""
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    (73654108430135874305, "**4305"),
    (12345, "**2345"),
    (11111111111111111111, "**1111")
])
def test_get_mask_account(account_number, expected):
    """Тестирует маскировку номера счета (параметризованный)."""
    assert get_mask_account(account_number) == expected