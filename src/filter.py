import re


def process_bank_search(data:list[dict], search:str)-> list[dict]:
    pattern = re.compile(search, re.IGNORECASE)
    result = [
        operation for operation in data
        if 'description' in operation and pattern.search(operation['description'])
    ]
    return result

def process_bank_operations(data: list[dict], categories: list) -> dict:
    category_counts = {category: 0 for category in categories}
    for operation in data:
        if 'description' not in operation:
            continue
        description = operation['description']
        for category in categories:
            if category in description:
                category_counts[category] += 1
    return category_counts
