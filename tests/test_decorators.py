import pytest
from src.decorators import log


@log()
def add_numbers(x: int, y: int) -> int:
    """Тестовая функция для успешного сложения."""
    return x + y


@log()
def divide_numbers(x: int, y: int) -> float:
    """Тестовая функция для деления (может вызывать ZeroDivisionError)."""
    return x / y


def test_log_console_success(capsys):
    """Проверка логирования успешного выполнения функции в консоль."""
    result = add_numbers(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add_numbers ok\n" in captured.out


def test_log_console_error(capsys):
    """Проверка логирования ошибки функции в консоль."""
    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0)
    captured = capsys.readouterr()
    assert "divide_numbers error: ZeroDivisionError. Inputs: (1, 0), {}\n" in captured.out


def test_log_file_success(tmp_path):
    """Проверка логирования успешного выполнения в файл."""
    log_file = tmp_path / "test_success.log"

    @log(filename=str(log_file))
    def sample_func():
        return "hello"

    sample_func()
    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "sample_func ok\n" in log_content


def test_log_file_error(tmp_path):
    """Проверка логирования ошибки в файл."""
    log_file = tmp_path / "test_error.log"

    @log(filename=str(log_file))
    def sample_error_func(value):
        return value / 0

    with pytest.raises(ZeroDivisionError):
        sample_error_func(10)

    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "sample_error_func error: ZeroDivisionError. Inputs: (10,), {}\n" in log_content
