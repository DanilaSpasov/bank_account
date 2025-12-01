def filter_by_state(unsorted_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция для сортировки списка словарей по ключам "EXECUTED" или "CANCELED"(по умолчанию по ключу "EXECUTED").
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    sorted_list = []
    for user in unsorted_list:
        if user["state"] == state:
            sorted_list.append(user)
    return sorted_list
