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



def get_mask_card_numbers(card_number: str) -> str:
    # Пример маскировки номеров карт, заменяя все символы на "X", кроме последних 4-х цифр.
    mask_length = len(card_number) - 4
    return "X" * mask_length + card_number[-4:]

from mask import get_mask_account

def mask_account_card(card: str) -> str:
    """Функция маскировки банковских карт и счетов"""
    if card == "":
        return ""
    elif "Счет" in card:
        return f"{card[:5]}**{card[-4:]}"
    else:
        return f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_date(date: str) -> str:
    """Функция переводит записанную дату в короткий читаемый вариант"""
    if date == "":
        return ""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Classic 6831982476737658"))
print((mask_account_card("Visa Gold 5999414228426353")))

def get_date(date_string):
    # Разделяем строку по символу 'T' и берем первую часть
    date_part = date_string.split("T")[0]
    # Разделяем дату по символу '-'
    year, month, day = date_part.split("-")
    # Формируем строку в нужном формате
    return f"{day}.{month}.{year}"

date_input = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_input)
print(formatted_date)


"""def get_mask_card_number(card_number: str) -> str:
    # Маскируем все, кроме последних 4 цифр
    if len(card_number) > 4:
        return "*" * (len(card_number) - 4) + card_number[-4:]
    return card_number


def get_mask_account(account_number: str) -> str:
    # Маскируем все, кроме последних 4 цифр
    if len(account_number) > 4:
        return "*" * (len(account_number) - 4) + account_number[-4:]
    return account_number


def mask_account_card(account_info):
    if "Visa" in account_info or "Maestro" in account_info:
        # Извлечение номера карты
        card_number = account_info.split()[-1]
        return account_info.replace(card_number, get_mask_card_number(card_number))
    elif "Счет" в account_info:
        # Извлечение номера счета
        account_number = account_info.split()[-1]
        return account_info.replace(account_number, get_mask_account(account_number))
    else:
        return "Неверный формат ввода"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Classic 6831982476737658"))
print((mask_account_card("Visa Gold 5999414228426353")))


def get_date(date_string):
    # Разделяем строку по символу 'T' и берем первую часть
    date_part = date_string.split("T")[0]
    # Разделяем дату по символу '-'
    year, month, day = date_part.split("-")
    # Формируем строку в нужном формате
    return f"{day}.{month}.{year}"


date_input = "2024-03-11T02:26:18.671407"
formatted_date = get_date(date_input)
print(formatted_date) """