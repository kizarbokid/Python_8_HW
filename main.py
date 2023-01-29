import csv
from random import randrange

# Считывание списка учеников из файла в список словарей
def read_from_file(filename:str):
    students_list = list()
    with open(filename, "r", newline="", encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # ключ при импорте некрасивый, правим
            row['ФИО'] = row.pop('\ufeffФИО')
            students_list.append(row)
    return students_list


# Считывание успеваемости из файла в список словарей
def read_progress_from_file(filename:str):
    progress_list = list()
    discipline = str()
    with open(filename, "r", newline="", encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # ключ при импорте некрасивый, правим
            #row['ФИО'] = row.pop('\ufeffФИО') #служебные символы появляются всякий раз, когда вручную правишь файл
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
def create_database(students_list,progress_list):
    database = list()
    for student in students_list:
        for marks in progress_list:
            if student['ФИО'] == marks['ФИО']:
                database.append(student | marks)
    return database


#сортировка и фильтрация списка студентов определенного класса
def filter_list_of_students(students_list:list,input_class:str):
    sorted_students_list = list()
    for elem in students_list:
        if elem['КЛАСС'] == input_class:
            sorted_students_list.append(elem['ФИО'])
    # сортировка списка учеников
    sorted_students_list = sorted(sorted_students_list)
    return sorted_students_list


# печать списка учеников определенного класса по алфавиту с оценками
def print_students_with_marks(students_list:list,database:list,discipline:str):
    for student_name in filtered_students_list:
        for elem in database:
            if student_name == elem['ФИО']:
                if discipline in elem:
                    print(student_name, elem.get(discipline), sep='\t')


def print_numbered_list(students_list:list):
    for index, student in enumerate(filtered_students_list, start=1):
        print(f'№ {index} - {student}')


# Добавить оценку ученику
def write_mark(database:list,input_class:str,student_name:str,discipline:str,mark:int):
    trigger = True
    for i in range(len(database)):
        if database[i]['ФИО'] == student_name and discipline in database[i]:
            temp_list = list()
            trigger = False
            temp_list = database[i][discipline]
            temp_list.append(mark)
    # Если в базе у данного ученика нет оценок по конкретному предмету, то добавтьь новую запись в БД
    if trigger:
        marks = list()
        marks.append(mark)
        database.append(
            {'КЛАСС': input_class, 'ФИО': student_name, discipline: marks})


# Разделить базу Данных, чтобы затем записать ее в файл
def dividing_db(database:list):
    progress_list_export = list()
    my_list=list()
    this_row = dict()
    for elem in database:
        # Склеиваем Zip'ом ключи и значения в список кортежей
        my_list=list(zip(elem.keys(),elem.values()))
        # в словарь записываем построчно
        this_row = {my_list[1][0]: my_list[1][1], 'Предмет': my_list[2][0], 'Оценки': ','.join(map(str,my_list[2][1]))}
        progress_list_export.append(this_row)
        # очистить словарь
        this_row.clear
    return progress_list_export


# Записать Успеваемость в Файл
def write_to_file(filename:str,database:list):
    progress_list_new=dividing_db(database)
    with open(filename, "w", newline="",encoding='UTF-8') as file:
        columns = ['ФИО','Предмет','Оценки',]
        writer = csv.DictWriter(file, fieldnames=columns,delimiter=';')
        writer.writeheader()
        # запись нескольких строк
        writer.writerows(progress_list_new)


students_file = 'Списки_учеников.csv'
students_list=read_from_file(students_file)
progress_file = 'Успеваемость.csv'
progress_list=read_progress_from_file(progress_file)
database=create_database(students_list,progress_list)
this_class = '6а'
#input('Введите класс: ').lower().strip().replace(' ','')
input_discipline = 'история'
#input('Введите предмет: ').lower().strip()
print(f'Журнал успеваемости "{this_class}" класса по предмету "{input_discipline}": ')
filtered_students_list=filter_list_of_students(students_list,this_class)
print_students_with_marks(filtered_students_list,database,input_discipline)
print_numbered_list(filtered_students_list)
n = randrange(1,6)
#int(input('Кого вызвать к доске? (Вводить порядковый номер): '))
student_name = filtered_students_list[n-1]
print("Отвечать будет", student_name)
mark = randrange(2,6)
#int(input('Оценка за ответ: '))
write_mark(database,this_class,student_name,input_discipline,mark)
print_students_with_marks(filtered_students_list,database,input_discipline)
write_to_file(progress_file,database)