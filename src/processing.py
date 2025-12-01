def filter_by_state(unsorted_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция для сортировки списка словарей по ключам "EXECUTED" или "CANCELED"(по умолчанию по ключу "EXECUTED").
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    sorted_list = []
    for user in unsorted_list:
        if user["state"] == state:
            sorted_list.append(user)
    return sorted_list


def sort_by_date(date_list: list[dict], reverse: bool = True) -> list[dict]:
    """Функция для сортировки списка словарей по дате(по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""

    date_list_sorted = sorted(date_list, key=lambda x: x["date"], reverse=reverse)
    return date_list_sorted
