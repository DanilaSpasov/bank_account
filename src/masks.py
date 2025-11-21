def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами."""
    card_number_str = str(card_number)
    masked = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]

    return masked


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки."""
    account_number_str = str(account_number)
    mask = "**" + account_number_str[-4:]

    return mask
