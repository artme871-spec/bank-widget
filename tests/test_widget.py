"""Тесты для модуля src.widget."""

import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты функции mask_account_card."""

    @pytest.mark.parametrize(
        "info, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
            ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ],
    )
    def test_card_type_is_masked_as_card(self, info: str, expected: str) -> None:
        """Строки с типом карты маскируются через get_mask_card_number."""
        assert mask_account_card(info) == expected

    @pytest.mark.parametrize(
        "info, expected",
        [
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счет 1234", "Счет **1234"),
        ],
    )
    def test_account_type_is_masked_as_account(self, info: str, expected: str) -> None:
        """Строки со словом 'Счет' маскируются через get_mask_account."""
        assert mask_account_card(info) == expected

    def test_empty_string_returns_empty(self) -> None:
        """Пустая строка на входе возвращает пустую строку."""
        assert mask_account_card("") == ""

    def test_invalid_card_number_in_info(self) -> None:
        """Некорректный номер карты внутри строки приводит к сообщению об ошибке формата."""
        assert mask_account_card("Visa 123") == "Visa Неверный формат карты"


class TestGetDate:
    """Тесты функции get_date."""

    @pytest.mark.parametrize(
        "date_str, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2018-06-30", "30.06.2018"),
            ("2000-01-01", "01.01.2000"),
        ],
    )
    def test_various_valid_dates(self, date_str: str, expected: str) -> None:
        """Функция корректно конвертирует разные валидные ISO-даты."""
        assert get_date(date_str) == expected

    def test_missing_date_returns_empty(self) -> None:
        """Отсутствующая (пустая) дата обрабатывается корректно."""
        assert get_date("") == ""

    def test_invalid_date_format_raises(self) -> None:
        """Некорректный формат даты вызывает исключение ValueError."""
        with pytest.raises(ValueError):
            get_date("not-a-date")