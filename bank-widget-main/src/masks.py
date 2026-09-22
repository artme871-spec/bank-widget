def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты."""
    if not card_number.isdigit() or len(card_number) != 16:
        return "Неверный формат карты"

    part1 = card_number[:4]
    part2 = card_number[4:6]
    part4 = card_number[12:]

    return f"{part1} {part2}** **** {part4}"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера банковского счета."""
    if not account_number.isdigit() or len(account_number) < 4:
        return "Неверный формат счета"

    return f"**{account_number[-4:]}"
