import functools
from datetime import datetime
from typing import Optional



def log(filename: Optional[str] = None):
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
