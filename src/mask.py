"""card_number = input()
account_number = input()"""


def get_musk_card_numbers(card_number: str) -> str:
    """Функция, которая принимает номер карты и маскирует ее"""
    return f"{card_number[:4]}{card_number[4:6]}** ***{card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета и маскирует ее"""
    return f"**{account_number[-4:]}"


"""print(get_musk_card_numbers("7000792289606361"))
print(get_mask_account("73654108430135874305"))"""
