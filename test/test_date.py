import pytest
from widget import get_date


def test_valid_date():
    assert get_date("2023-10-05") == "05.10.2023"
    assert get_date("2000-01-01") == "01.01.2000"


def test_empty_date():
    assert get_date("") == ""


def test_garbage_date():
    assert get_date("garbage") == ".ga.garb"


def test_partial_date():
    assert get_date("2023-10") == ".10.2023"
    assert get_date("2023") == "..2023"


def test_invalid_date():
    # Здесь мы ожидаем, что функция выбросит исключение
    with pytest.raises(IndexError):
        get_date("invalid-date")


if __name__ == "__main__":
    pytest.main()
