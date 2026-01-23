import json
import os


def json_convertation(file_path) -> list:
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []

            return data

    except json.JSONDecodeError:
        return []
