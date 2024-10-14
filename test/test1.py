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
