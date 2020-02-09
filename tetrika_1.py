import string

def file_read(path):
    """
    Чтение файла.
    :param path: Путь и название
    :return: Текст
    """
    with open(path, 'r') as f:
        file = f.read()
    return file

def file_sortead(text):
    """
    Сортировка имен по в лексикографическом порядке.
    :param text: Текст
    :return: Список отсортированных имен (list)
    """
    file = text.lstrip('"')
    file = file.rstrip('"')
    list_names = sorted(file.split('","'))
    return list_names

def abc_create_dict():
    """
    Создание словаря и нумерацию каждой буквы в словаре.
    :return: Словарь (dict) {'буква': номер буквы в словаре}. Пример {'A': 1, 'B': 2, ... {n}: n}
    """
    letters = string.ascii_uppercase
    ABC_dict = {}
    for i in range(26):
        ABC_dict.update({ letters[i] : i+1 })
    return ABC_dict

def abc_summ_in_name(list_names):
    """
    Расчет суммы порядковых номеров букв.
    :param list_names: Список имен (list)
    :return: Словарь (dict) {'имя': сумма}. Пример {'ABE': 8, 'ABEL': 20, ... }
    """
    ABC_summ = {}
    dict_ABC = abc_create_dict()
    for name in list_names:
        summ_letters = 0
        for letter in name:
            for key, value in dict_ABC.items():
                if key == letter:
                    summ_letters += value
        ABC_summ.update({name : summ_letters})
    return ABC_summ

def abc_multiply(summ_letters):
    """
    Умножить алфавитную сумму каждого имени на порядковый номер имени
    в отсортированном списке (индексация начинается с 1).
    :param summ_letters: Словарь с именами и суммами порядковых
    номеров букв. Пример {'AARON': 49, 'ABBEY': 35, ... }
    :return: Список (list)
    """
    ABC_multiply = []
    index = 1
    for value in summ_letters.values():
        sum_value = value * index
        ABC_multiply.append(sum_value)
        index += 1
    return ABC_multiply

def amount_of_works(multiply_index_and_summ):
    """
    Сумма произведений всех имен.
    :param multiply_index_and_summ: Список (list)
    :return: Сумму (int)
    """
    return sum(multiply_index_and_summ)

if __name__ == '__main__':
    # Путь и название
    path = 'names.txt'

    sorted_names = file_sortead(file_read(path))
    summ_letters = abc_summ_in_name(sorted_names)
    multiply_index_and_summ = abc_multiply(summ_letters)
    amount_of_works(multiply_index_and_summ)
    print('1)', sorted_names)
    print('2)', summ_letters)
    print('3)', multiply_index_and_summ)
    print('4)', amount_of_works(multiply_index_and_summ))