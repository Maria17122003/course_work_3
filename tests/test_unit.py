import pytest
from utils import *


def test_get_inf(test_inf):
    """
    Тест функции
    get_inf
    """
    assert len(get_inf(test_inf)) > 0


def test_get_filtered_state(test_inf):
    """
    Тест функции
    get_filtered_state
    """
    assert len(get_filtered_state(get_inf(test_inf))) == 85


def test_get_last_values(test_inf):
    """
    Тест функции
    get_last_values
    """
    inf = get_last_values(get_filtered_state(get_inf(test_inf)), 5)
    assert len(inf) == 5
    assert inf[0]['date'] == '2019-12-08T22:46:21.935582'


def test_get_formatted_inf(test_inf):
    """
    Тест функции
    get_formatted_inf
    """
    formatted_inf = get_formatted_inf(get_last_values(get_filtered_state(get_inf(test_inf)), 5))
    assert formatted_inf == ['08.12.2019 Открытие вклада\nДанные отсутствуют -> Счет **5907 \n41096.24 USD',
     '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655 \n48150.39 USD',
     '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869 \n30153.72 руб.',
     '13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** 9794 -> Счет **8125 \n62814.53 руб.',
     '05.11.2019 Открытие вклада\nДанные отсутствуют -> Счет **8381 \n21344.35 руб.']
