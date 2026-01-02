from random import random


def filter_by_currency(transactions: list, currency: str) -> list:
    for transaction in transactions:
        currency_name = transaction['operationAmount']['currency']['name']
        if currency_name == currency:
            yield transaction

def transaction_descriptions(transactions: list):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(card_number) -> str:
    card_number = random.randit(1,9999999999999999)
    card_number_str = str(f"{card_number:016d})
    parts = [
            card_number_str[:4],
            card_number_str[4:8],
            card_number_str[8:12],
            card_number_str[12:16]
    ]
        yield ' '.join(parts)
