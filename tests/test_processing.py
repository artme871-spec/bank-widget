"""Тесты для модуля src.processing."""

import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты функции filter_by_state."""

    def test_default_state_executed(self, operations: list[dict]) -> None:
        """По умолчанию отбираются только операции со state='EXECUTED'."""
        result = filter_by_state(operations)
        assert result == [
            {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]

    @pytest.mark.parametrize(
        "state, expected_ids",
        [
            ("EXECUTED", [1, 3]),
            ("CANCELED", [2]),
            ("PENDING", [4]),
            ("UNKNOWN_STATE", []),
        ],
    )
    def test_filter_by_various_states(
        self, operations: list[dict], state: str, expected_ids: list[int]
    ) -> None:
        """Функция корректно фильтрует список по разным значениям state."""
        result = filter_by_state(operations, state)
        assert [operation["id"] for operation in result] == expected_ids

    def test_no_matching_state_returns_empty_list(self, operations_no_executed: list[dict]) -> None:
        """Если операций с искомым state нет, возвращается пустой список."""
        assert filter_by_state(operations_no_executed, "EXECUTED") == []

    def test_empty_operations_list(self, empty_operations: list[dict]) -> None:
        """Пустой список операций на входе дает пустой список на выходе."""
        assert filter_by_state(empty_operations) == []

    def test_does_not_mutate_original_list(self, operations: list[dict]) -> None:
        """Исходный список операций не изменяется после фильтрации."""
        original_length = len(operations)
        filter_by_state(operations, "CANCELED")
        assert len(operations) == original_length


class TestSortByDate:
    """Тесты функции sort_by_date."""

    def test_sort_descending_by_default(self, operations: list[dict]) -> None:
        """По умолчанию операции сортируются от новых к старым."""
        result = sort_by_date(operations)
        dates = [operation["date"] for operation in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, operations: list[dict]) -> None:
        """При reverse=False операции сортируются от старых к новым."""
        result = sort_by_date(operations, reverse=False)
        dates = [operation["date"] for operation in result]
        assert dates == sorted(dates)

    def test_sort_with_equal_dates(self, operations_same_date: list[dict]) -> None:
        """Операции с одинаковыми датами сохраняют относительный порядок и корректно сортируются."""
        result = sort_by_date(operations_same_date)
        assert [operation["id"] for operation in result] == [1, 2]

    def test_sort_does_not_mutate_original_list(self, operations: list[dict]) -> None:
        """Исходный список операций не изменяется после сортировки."""
        original_order = [operation["id"] for operation in operations]
        sort_by_date(operations)
        assert [operation["id"] for operation in operations] == original_order

    def test_empty_operations_list(self, empty_operations: list[dict]) -> None:
        """Пустой список операций на входе дает пустой список на выходе."""
        assert sort_by_date(empty_operations) == []

    def test_missing_date_key_raises(self) -> None:
        """Операция без ключа 'date' вызывает исключение KeyError."""
        with pytest.raises(KeyError):
            sort_by_date([{"id": 1, "state": "EXECUTED"}])
