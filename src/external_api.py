import os

import requests
from dotenv import load_dotenv



def transaction_amount(transaction_list:list) -> float:
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


trns = [{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]
print(transaction_amount(trns))


