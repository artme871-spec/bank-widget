from typing import Iterator, List, Dict, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте с помощью yield."""
    for transaction in transactions:
        # Безопасно достаем код валюты из вложенного словаря
        op_amount = transaction.get("operationAmount", {})
        curr_code = op_amount.get("currency", {}).get("code")

        if curr_code == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Поочередно возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, end + 1):
        # Превращаем число в 16-значную строку с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем строку по 4 цифры через пробел
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted_card
