from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """Функция Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером."""
    number_list = account_card_number.split()
    name, number = number_list[:-1], number_list[-1]
    number = int(number)
    name = " ".join(name)
    if name == "Счет":
        masked_account_card = f"{name} {get_mask_account(number)}"
    else:
        masked_account_card = f"{name} {get_mask_card_number(number)}"
    return masked_account_card


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате "Y-m-dTH:M:S.f"
    и возвращает строку с датой в формате "d.m.Y"."""

    date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_format.strftime("%d.%m.%Y")
