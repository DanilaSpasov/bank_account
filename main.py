from src.file_reader import read_csv, read_xlsx
from src.filter import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from src.utils import json_convertation


def main():
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    user_answer = int(input("Введите число от 1 до 3: "))

    if user_answer == 1:
        print("Для обработки выбран JSON-файл")
        transactions = json_convertation("data/operations.json")

    elif user_answer == 2:
        print("Для обработки выбран CSV-файл")
        transactions = read_csv("data/transactions.csv")

    elif user_answer == 3:
        print("Для обработки выбран XLSX-файл")
        transactions = read_xlsx("data/transactions_excel.xlsx")

    else:
        print("Некорректный выбор")
        return

    # Фильтрация по статусу
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные статусы:
EXECUTED, CANCELED, PENDING""")

        user_status = input(
            "Введите EXECUTED, CANCELED или PENDING: "
        ).upper()

        if user_status in ("EXECUTED", "CANCELED", "PENDING"):
            transactions = filter_by_state(transactions, user_status)
            print(f"Операции отфильтрованы по статусу: {user_status}")
            break
        else:
            print(f"Статус операции {user_status} недоступен.")

    # Сортировка по дате
    user_filter_date = input(
        "Отсортировать операции по дате? Да/Нет: "
    ).lower()

    if user_filter_date == "да":
        user_filter_grade = input(
            "По возрастанию или по убыванию? "
        ).lower()

        reverse = user_filter_grade == "по убыванию"

        transactions = sort_by_date(transactions, reverse)


    user_filter_rubles = input(
        "Выводить только рублевые транзакции? Да/Нет: "
    ).lower()

    if user_filter_rubles == "да":
        transactions = filter_by_currency(transactions, "руб.")


    user_filter_word = input(
        "Отфильтровать список транзакций по слову в описании? Да/Нет: "
    ).lower()

    if user_filter_word == "да":
        word = input("Введите слово для поиска: ").lower()

        transactions = process_bank_search(transactions, word)

    transactions = list(transactions)

    # Итоговый вывод
    print("\nРаспечатываю итоговый список транзакций...\n")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    for transaction in transactions:
        date = transaction.get("date", "").replace("Z", "")

        if "." not in date:
            date += ".000000"

        formatted_date = get_date(date)

        from_account = transaction.get("from")
        to_account = transaction.get("to")

        if isinstance(from_account, str):
            account_info = (
                f"{mask_account_card(from_account)} -> "
                f"{mask_account_card(to_account)}"
            )
        else:
            account_info = mask_account_card(to_account)

        if "operationAmount" in transaction:
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
        else:
            amount = transaction["amount"]
            currency = transaction["currency_name"]

        print(f"{formatted_date} {transaction['description']}")
        print(account_info)
        print(f"Сумма: {amount} {currency}")
        print()


if __name__ == "__main__":
    main()
