"""card_number = input()
account_number = input()"""


""" def get_musk_card_numbers(card_number: str) -> str:
    return f"{card_number[:4]}{card_number[4:6]}** *** {card_number[12:]}"


def get_mask_account_number(account_number: str) -> str:
    return f"**{account_number[-4:]}"


print(get_musk_card_numbers("7000792289606361"))
print(get_mask_account_number("73654108430135874305")) """


from datetime import datetime

def get_date(date_string):
    # Пробуем распарсить входную строку в разные форматы
    for fmt in ("%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            # Преобразуем строку в объект datetime
            date_obj = datetime.strptime(date_string, fmt)
            # Возвращаем дату в нужном формате
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            continue
    return "Неверный формат даты"

print(get_date("12.12.1222 "))