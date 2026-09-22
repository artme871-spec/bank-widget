"""Общие фикстуры для тестов проекта."""

import pytest


@pytest.fixture
def valid_card_number() -> str:
    """Валидный 16-значный номер карты."""
    return "7000792289606361"


@pytest.fixture
def valid_account_number() -> str:
    """Валидный номер банковского счета."""
    return "73654108430135874305"


@pytest.fixture
def operations() -> list[dict]:
    """Список словарей с данными об операциях: разные state и date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "state": "PENDING", "date": "2020-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def operations_no_executed() -> list[dict]:
    """Список операций, где ни одна не имеет state=EXECUTED."""
    return [
        {"id": 1, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_same_date() -> list[dict]:
    """Список операций с одинаковой датой."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def empty_operations() -> list[dict]:
    """Пустой список операций."""
    return []