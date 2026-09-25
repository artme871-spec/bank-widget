import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        }
    ]


def test_filter_by_currency(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    assert next(usd_gen)["id"] == 939719570
    assert next(usd_gen)["id"] == 142264268
    with pytest.raises(StopIteration):
        next(usd_gen)


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    assert next(desc_gen) == "Перевод организации"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод со счета на счет"


@pytest.mark.parametrize("start, end, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

