# Импортируем json и datetime
import json
from datetime import datetime


def get_inf(inf):
    """
    Получает список операций,
    возвращает список в формате
    json
    """
    with open(inf, encoding="UTF-8") as file:
        operations = json.load(file)
    return operations


def get_filtered_state(inf):
    """
    Фильтрует список операций
    по статусу
    """
    state = []
    for i in inf:
        if "state" in i and i["state"] == "EXECUTED":
            state.append(i)
    return state


def get_last_values(inf, count_last_values):
    """
    Возвращает пять
    последних выполненных операций
    """
    inf = sorted(inf, key=lambda i: i["date"], reverse=True)
    inf = inf[:count_last_values]
    return inf


def get_formatted_inf(inf):
    """
    Форматирует операции в нужный формат
    """
    formatted_inf = []
    for i in inf:
        date = datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        try:
            sender = i["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        except KeyError:
            from_info = "Данные"
            from_bill = "отсутствуют"
        recipient = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operation_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"

        formatted_inf.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient} 
{operation_amount}""")

    return formatted_inf
