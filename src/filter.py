import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(search, re.IGNORECASE)
    result = [
        operation for operation in data if "description" in operation and pattern.search(operation["description"])
    ]
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    category_counts = {category: 0 for category in categories}
    for operation in data:
        if "description" not in operation:
            continue
        description = operation["description"]
        for category in categories:
            if category in description:
                category_counts[category] += 1
    return category_counts
