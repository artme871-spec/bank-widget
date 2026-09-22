from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Принимает строку с названием и номером карты/счета и маскирует её."""
    if not info:
        return ""

    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Конвертирует строку даты из формата ISO в формат ДД.ММ.ГГГГ."""
    if not date_str:
        return ""

    parsed_date = datetime.fromisoformat(date_str)

    return parsed_date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
