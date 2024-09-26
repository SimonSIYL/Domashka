"""from dulwich.porcelain import symbolic_ref
from scr.mask import get_mask_account, get_mask_card_number

from test.test1 import get_mask_account_number


def mask_account_card(type_and_number: str)-> str:
    text_result = ""
    digit_result = ""
    didit_count = 0
    for symbol in type_and_number:
        if symbol.isalpha():
            text_result += symbol
        elif symbol.isalpha():
            digit_count += 1
            digit_result += symbol
    if digit_count > 16 :
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"

    print()

    def get_date(date_str: str) -> str:
        date_slice = date_str[0:10].split("-")
        return ".".join(date_slice[::1])"""

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
