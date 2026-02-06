import json
import logging
import os


def json_convertation(file_path) -> list:
    """функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.exists(file_path):
        logger.warning("Путь к файлу не найден, возвращается пустой список.")
        return []
    try:
        logger.info("Возвращение списка словарей с данными о финансовых транзакциях.")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []
