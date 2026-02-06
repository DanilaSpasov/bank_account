import os

import requests
from dotenv import load_dotenv


def transaction_amount(transaction_list: list) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""
    for transaction in transaction_list:
        from_currency = transaction["operationAmount"]["currency"]["code"]
        if from_currency == "RUB":
            return transaction["operationAmount"]["amount"]
        else:
            amount = transaction["operationAmount"]["amount"]
            to_currency = "RUB"
            load_dotenv()
            API_KEY = os.getenv("API_KEY")

            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

            payload = {}
            headers = {"apikey": API_KEY}
            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code == 200:
                result = response.json()
                converted_amount = result["result"]
                return converted_amount
            else:
                raise Exception(f"Ошибка API: {response.status_code}, {response.text}")
