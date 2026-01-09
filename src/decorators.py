import functools
from datetime import datetime
from typing import Optional


def log(filename: Optional[str] = None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    Логирование включает имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            error = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error = e
                end_time = datetime.now()
                log_msg = (
                    f"{func.__name__} -> ОШИБКА!\n"
                    f"Тип ошибки: {type(error).__name__}\n"
                    f"Сообщение: {error}\n"
                    f"Вводные данные функции: {args}, {kwargs}\n"
                    f"Время ошибки - {end_time}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)
                raise
            end_time = datetime.now()
            duration = end_time - start_time
            if error is None:
                log_msg = (
                    f"{func.__name__} -> OK\n"
                    f"Время начала работы функции - {start_time}, время окончания выполнения функции - {end_time})\n"
                    f"Длительность выполнения функции - {duration}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)
            return result

        return wrapper

    return decorator
