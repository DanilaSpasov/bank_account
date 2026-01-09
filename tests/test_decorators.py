import pytest

from src.decorators import log


def test_log_decorator_success(capsys):
    """Проверка на успешное деление и работу декоратора"""

    @log()
    def divide(a, b):
        return a / b

    result = divide(10, 2)
    assert result == 5.0

    captured = capsys.readouterr()
    output = captured.out

    assert "divide -> OK" in output
    assert "Время начала работы функции -" in output
    assert "Длительность выполнения функции -" in output


def test_log_decorator_zero_division(capsys):
    """Проверка декоратора на деление на ноль (ожидается исключение)."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    output = captured.out

    assert "divide -> ОШИБКА!" in output
    assert "Тип ошибки: ZeroDivisionError" in output
    assert "Сообщение: division by zero" in output
    assert "Вводные данные функции: (10, 0)" in output


def test_log_decorator_type_error(capsys):
    """Проверка на передачу некорректных типов (например, строка вместо числа)."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(TypeError):
        divide("10", 2)

    captured = capsys.readouterr()
    output = captured.out

    assert "divide -> ОШИБКА!" in output
    assert "Тип ошибки: TypeError" in output
    assert "Сообщение:" in output
    assert "Вводные данные функции: ('10', 2)" in output


def test_log_decorator_negative_numbers(capsys):
    """Проверка на деление отрицательных чисел (граничный случай)."""

    @log()
    def divide(a, b):
        return a / b

    result = divide(-10, -2)
    assert result == 5.0  # (-10) / (-2) = 5

    captured = capsys.readouterr()
    output = captured.out

    assert "divide -> OK" in output
    assert "Время начала работы функции -" in output
    assert "Длительность выполнения функции -" in output


def test_log_decorator_log_to_file_success(tmp_path, capsys):
    """Проверка записи успешного лога в файл (filename указан).
    Используем tmp_path для создания временного файла."""
    log_file = tmp_path / "test_log.txt"
    log_file_path = str(log_file)

    @log(filename=log_file_path)
    def divide(a, b):
        return a / b

    result = divide(8, 4)
    assert result == 2.0

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""

    with open(log_file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    assert "divide -> OK" in file_content
    assert "Время начала работы функции -" in file_content
    assert "Длительность выполнения функции -" in file_content


def test_log_decorator_log_to_file_fail(tmp_path, capsys):
    """Проверка записи лога с вызовом ошибки в файл (filename указан).
    Используем tmp_path для создания временного файла."""
    log_file = tmp_path / "test_log.txt"
    log_file_path = str(log_file)

    @log(filename=log_file_path)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    with open(log_file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    assert "divide -> ОШИБКА!" in file_content
    assert "Тип ошибки: ZeroDivisionError" in file_content
    assert "Сообщение: division by zero" in file_content
    assert "Вводные данные функции: (5, 0)" in file_content
