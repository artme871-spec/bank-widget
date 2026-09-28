from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Отфильтровывает список операций по значению ключа state.

    Args:
        operations: Список словарей с данными о банковских операциях.
            Каждый словарь должен содержать ключ "state".
        state: Значение ключа "state", по которому нужно отфильтровать
            операции. По умолчанию "EXECUTED".

    Returns:
        Новый список словарей, содержащий только те операции, у которых
        значение ключа "state" равно переданному аргументу state.

    Example:
        >>> ops = [
        ...     {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ...     {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ... ]
        >>> filter_by_state(ops)
        [{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
        >>> filter_by_state(ops, "CANCELED")
        [{'id': 2, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список операций по значению ключа date.

    Args:
        operations: Список словарей с данными о банковских операциях.
            Каждый словарь должен содержать ключ "date" со строкой
            в формате ISO 8601 (например, "2019-07-03T18:35:29.512364").
        reverse: Порядок сортировки. True — от новых операций к старым
            (по убыванию даты), False — от старых к новым (по возрастанию
            даты). По умолчанию True.

    Returns:
        Новый список словарей, отсортированный по дате. Исходный список
        не изменяется.

    Example:
        >>> ops = [
        ...     {"id": 1, "date": "2018-06-30"},
        ...     {"id": 2, "date": "2019-07-03"},
        ... ]
        >>> sort_by_date(ops)
        [{'id': 2, 'date': '2019-07-03'}, {'id': 1, 'date': '2018-06-30'}]
        >>> sort_by_date(ops, reverse=False)
        [{'id': 1, 'date': '2018-06-30'}, {'id': 2, 'date': '2019-07-03'}]
    """
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
