# Импортируем функции из utils
from utils import get_inf, get_filtered_state, get_last_values, get_formatted_inf


def main():
    inf = get_inf('operations.json')
    count_last_values = 5

    state = get_filtered_state(inf)
    last_values = get_last_values(state, count_last_values)
    formatted_inf = get_formatted_inf(last_values)

    # Вывод последних операций
    print("Последние операции:")
    for i in formatted_inf:
        print(i, end='\n\n')


if __name__ == "__main__":
    main()
