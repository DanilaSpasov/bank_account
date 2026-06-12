import pandas as pd


def read_csv(file_path) -> list:
    """Функция, которая считывает финансовые операции из .csv файла."""
    try:
        df = pd.read_csv(file_path, encoding="utf-8", sep=";")
        csv_dict = df.to_dict("records")
        return csv_dict
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def read_xlsx(file_path) -> list:
    """Функция, которая считывает финансовые операции из .xlsx файла."""
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        xlsx_dict = df.to_dict("records")
        return xlsx_dict
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_path}': {e}")
        return []
