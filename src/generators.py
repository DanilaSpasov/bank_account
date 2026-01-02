from random import random


def filter_by_currency(transactions: list, currency: str) -> list:
    """Функция, которая возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        currency_name = transaction['operationAmount']['currency']['name']
        if currency_name == currency:
            yield transaction

def transaction_descriptions(transactions: list) -> str:
    """Функция, которая принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, stop: int ) -> str:
    """ Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров."""
    if start > 9999999999999999:
        raise ValueError("start не может быть больше 16 цифр")
    if stop > 9999999999999999:
        raise ValueError("stop не может быть больше 16 цифр")
    card_number = random.randit(start,stop)
    card_number_str = str(f"{card_number:016d}")
    parts = [
            card_number_str[:4],
            card_number_str[4:8],
            card_number_str[8:12],
            card_number_str[12:16]
    ]
    yield ' '.join(parts)
