
def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item["state"] == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'date'
    по умолчанию список фильтруется по убыванию.
    """

    return sorted(data, key=lambda x: x["date"], reverse=reverse)


# Пример использования
list_of_dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filtered_list_of_dicts = filter_by_state(list_of_dicts)
filtered_list_of_dicts_date = sort_by_date(list_of_dicts)
print(filtered_list_of_dicts)
print(filtered_list_of_dicts_date)
