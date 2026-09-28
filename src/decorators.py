import functools
import sys
from typing import Any, Callable, Optional, TextIO, TypeVar, cast

# Создаем переменную типа для сохранения сигнатуры оборачиваемых функций
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Декоратор, который логирует начало, конец, результат или ошибку выполнения функции.

    Логи выводятся в файл (если задан filename) или в консоль (sys.stdout).
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Явно указываем mypy, что это объект для записи текста (TextIO)
            target_output: TextIO

            if filename:
                target_output = open(filename, "a", encoding="utf-8")
            else:
                target_output = sys.stdout

            try:
                # Пытаемся выполнить функцию
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                target_output.write(log_message)
                return result
            except Exception as e:
                # Если произошла ошибка, логируем её тип и входные параметры
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                target_output.write(log_message)
                raise e
            finally:
                # Если открывали файл, обязательно его закрываем
                if filename:
                    target_output.close()

        return cast(F, wrapper)

    return decorator
