"""Тесты для модуля src.masks."""

import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты функции get_mask_card_number."""

    def test_valid_card_number(self, valid_card_number: str) -> None:
        """Корректный 16-значный номер карты маскируется в нужном формате."""
        assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("9999999999999999", "9999 99** **** 9999"),
        ],
    )
    def test_various_valid_card_numbers(self, card_number: str, expected: str) -> None:
        """Функция корректно маскирует разные валидные номера карт."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "card_number",
        [
            "700079228960636",  # 15 цифр — короче нормы
            "70007922896063611",  # 17 цифр — длиннее нормы
            "",  # пустая строка
        ],
    )
    def test_invalid_length(self, card_number: str) -> None:
        """Номера карты неверной длины считаются некорректными."""
        assert get_mask_card_number(card_number) == "Неверный формат карты"

    @pytest.mark.parametrize(
        "card_number",
        [
            "700079228960636a",  # содержит букву
            "7000-7922-8960-6361",  # содержит дефисы
            "7000 7922 8960 6361",  # содержит пробелы
            "abcdefghijklmnop",  # только буквы
        ],
    )
    def test_non_digit_input(self, card_number: str) -> None:
        """Номера карты, содержащие не только цифры, считаются некорректными."""
        assert get_mask_card_number(card_number) == "Неверный формат карты"

    def test_missing_card_number(self) -> None:
        """Отсутствующий (пустой) номер карты обрабатывается корректно."""
        assert get_mask_card_number("") == "Неверный формат карты"


class TestGetMaskAccount:
    """Тесты функции get_mask_account."""

    def test_valid_account_number(self, valid_account_number: str) -> None:
        """Корректный номер счета маскируется в нужном формате."""
        assert get_mask_account(valid_account_number) == "**4305"

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("1234", "**1234"),
            ("00001234", "**1234"),
            ("9999999999", "**9999"),
        ],
    )
    def test_various_valid_account_numbers(self, account_number: str, expected: str) -> None:
        """Функция корректно маскирует счета разной длины и формата."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "account_number",
        [
            "123",  # 3 цифры — короче ожидаемой длины
            "1",  # одна цифра
            "",  # пустая строка
        ],
    )
    def test_account_shorter_than_expected(self, account_number: str) -> None:
        """Номера счетов короче 4 цифр считаются некорректными."""
        assert get_mask_account(account_number) == "Неверный формат счета"

    @pytest.mark.parametrize(
        "account_number",
        [
            "12a4",
            "account123",
            "1234 5678",
        ],
    )
    def test_non_digit_input(self, account_number: str) -> None:
        """Номера счетов, содержащие не только цифры, считаются некорректными."""
        assert get_mask_account(account_number) == "Неверный формат счета"