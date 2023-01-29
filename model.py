import csv

import controller



# Считывание списка учеников из файла в список словарей
def read_students_from_file(filename='Списки_учеников.csv'):
    students_list = list()
    with open(filename, "r", newline="", encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # ключ при импорте некрасивый, правим
            row['ФИО'] = row.pop('\ufeffФИО')
            students_list.append(row)
    return students_list


# Считывание успеваемости из файла в список словарей
def read_progress_from_file(filename='Успеваемость.csv'):
    progress_list = list()
    discipline = str()
    with open(filename, "r", newline="", encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # ключ при импорте некрасивый, правим
            # row['ФИО'] = row.pop('\ufeffФИО') #служебные символы появляются всякий раз, когда вручную правишь файл
            # перевод строки оценок в список чисел
            row['Оценки'] = list(map(int, row['Оценки'].split(sep=',')))
            # Значение ключа "предмет" становится ключом, оценки ученика - значением к ключу
            discipline = row['Предмет']
            row[discipline] = row.pop('Оценки')
            # Ключ "Предмет" больше не нужен
            del row['Предмет']
            progress_list.append(row)
    return progress_list


# объединение списков в "базу данных"
def create_database(students_list, progress_list):
    database = list()
    for student in students_list:
        for marks in progress_list:
            if student['ФИО'] == marks['ФИО']:
                database.append(student | marks)
    return database


# Разделить базу Данных, чтобы затем записать ее в файл
def dividing_db(database: list):
    progress_list_export = list()
    my_list = list()
    this_row = dict()
    for elem in database:
        # Склеиваем Zip'ом ключи и значения в список кортежей
        my_list = list(zip(elem.keys(), elem.values()))
        # в словарь записываем построчно
        this_row = {my_list[1][0]: my_list[1][1], 'Предмет': my_list[2]
                    [0], 'Оценки': ','.join(map(str, my_list[2][1]))}
        progress_list_export.append(this_row)
        # очистить словарь
        this_row.clear
    return progress_list_export
    

# Записать Успеваемость в Файл
def write_to_file(database: list,filename='Успеваемость.csv'):
    progress_list_new = dividing_db(database)
    with open(filename, "w", newline="", encoding='UTF-8') as file:
        columns = ['ФИО', 'Предмет', 'Оценки',]
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        writer.writeheader()
        # запись нескольких строк
        writer.writerows(progress_list_new)