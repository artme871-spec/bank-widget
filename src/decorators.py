import functools
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует начало, конец, результат или ошибку выполнения функции.

    Логи выводятся в файл (если задан filename) или в консоль (sys.stdout).
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Определяем, куда писать логи
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

        return wrapper
    return decorator
