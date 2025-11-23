from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    number_list = account_card_number.split()
    name, number = number_list[:-1], number_list[-1]
    number = int(number)
    name = " ".join(name)
    if name == "Счет":
        return str(name) + " " + get_mask_account(number)
    else:
        return str(name) + " " + get_mask_card_number(number)