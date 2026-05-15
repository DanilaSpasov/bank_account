import re


def process_bank_search(data:list[dict], search:str)-> list[dict]:
    pattern = re.compile(search, re.IGNORECASE)
    result = [
        operation for operation in data
        if 'description' in operation and pattern.search(operation['description'])
    ]
    return result

