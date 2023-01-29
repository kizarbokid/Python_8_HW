import model
import view
import csv
from random import randrange


def start():
    user_input=0
    while user_input in [0,1,2,3,4,5]:
        view.main_menu()
        user_input=view.int_input(view.show_menu_message())
        match user_input:

            case 1: #Подключиться к файлу
                students_list = model.read_students_from_file()
                progress_list = model.read_progress_from_file()
                database = model.create_database(students_list, progress_list)
                view.successfully_read_message()

            case 2: #Начать урок
                this_class = '6а'
                # input('Введите класс: ').lower().strip().replace(' ','')
                input_discipline = 'история'
                # input('Введите предмет: ').lower().strip()
                print(
                    f'Журнал успеваемости "{this_class}" класса по предмету "{input_discipline}": ')
                filtered_students_list = filter_list_of_students(students_list, this_class)
                print_students_with_marks(filtered_students_list, database, input_discipline)
                print_numbered_list(filtered_students_list)
                n = randrange(1, 6)
                # int(input('Кого вызвать к доске? (Вводить порядковый номер): '))
                student_name = filtered_students_list[n-1]
                print("Отвечать будет", student_name)
                mark = randrange(2, 6)
                # int(input('Оценка за ответ: '))
                write_mark(database, this_class, student_name, input_discipline, mark)
                print_students_with_marks(filtered_students_list, database, input_discipline)

            case 3: #Посмотреть поименный список класса
                this_class = '6а'
                # input('Введите класс: ').lower().strip().replace(' ','')
                filtered_students_list = filter_list_of_students(students_list, this_class)
                print(f'Список "{this_class}" класса:')
                print_numbered_list(filtered_students_list)

            case 4: #Посмотреть оценки по предмету определенного класса
                this_class = '6а'
                # input('Введите класс: ').lower().strip().replace(' ','')
                input_discipline = 'история'
                # input('Введите предмет: ').lower().strip()
                print(
                    f'Журнал успеваемости "{this_class}" класса по предмету "{input_discipline}": ')
                filtered_students_list = filter_list_of_students(students_list, this_class)
                print_students_with_marks(filtered_students_list, database, input_discipline)

            case 5: #Записать в файл
                model.write_to_file(database)
                view.successfully_write_message()
    else:
        view.goodbye_message()   
        





# сортировка и фильтрация списка студентов определенного класса
def filter_list_of_students(students_list: list, input_class: str):
    sorted_students_list = list()
    for elem in students_list:
        if elem['КЛАСС'] == input_class:
            sorted_students_list.append(elem['ФИО'])
    # сортировка списка учеников
    sorted_students_list = sorted(sorted_students_list)
    return sorted_students_list


# печать списка учеников определенного класса по алфавиту с оценками
def print_students_with_marks(students_list: list, database: list, discipline: str):
    for student_name in students_list:
        for elem in database:
            if student_name == elem['ФИО']:
                if discipline in elem:
                    print(student_name, elem.get(discipline), sep='\t')


def print_numbered_list(students_list: list):
    for index, student in enumerate(students_list, start=1):
        print(f'№ {index} - {student}')


# Добавить оценку ученику
def write_mark(database: list, input_class: str, student_name: str, discipline: str, mark: int):
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





