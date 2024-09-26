"""card_number = input()
account_number = input()"""


"""def get_musk_card_numbers(card_number: str) -> str:
    return f"{card_number[:4]}{card_number[4:6]}** *** {card_number[12:]}"


def get_mask_account_number(account_number: str) -> str:
    return f"**{account_number[-4:]}"


print(get_musk_card_numbers("7000792289606361"))
print(get_mask_account_number("73654108430135874305"))"""




from dulwich.porcelain import symbolic_ref
from scr.mask import get_mask_account, get_mask_card_number
from test.test1 import get_mask_account_number


def mask_account_card(type_and_number: str) -> str:
    text_result = ""
    digit_result = ""
    digit_count = 0  # исправлено имя переменной
    for symbol in type_and_number:
        if symbol.isalpha():
            text_result += symbol
        elif symbol.isdigit():  # исправлено условие для цифр
            digit_count += 1
            digit_result += symbol
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


def get_date(date_str: str) -> str:  # перенесена функция на уровень, чтобы не была вложенной без необходимости
    date_slice = date_str[0:10].split("-")
    return ".".join(date_slice[::1])


