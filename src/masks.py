import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами."""
    logger.info("Создание маски номера карты")
    card_number_str = str(card_number)
    masked = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]

    return masked


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки."""
    logger.info("Создание маски номера карты")
    account_number_str = str(account_number)
    mask = "**" + account_number_str[-4:]

    return mask
