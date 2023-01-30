import controller

def main_menu():
    print('','-----Список команд----',
    '1 - Подключиться к БД',
    '2 - Провести урок',
    '3 - Посмотреть поименный список учеников класса',
    '4 - Посмотреть успеваемость по предмету учеников класса',
    '5 - Записать базу БД',
    '6 - ВЫХОД',
    '----------------------',
    sep='\n')

def show_menu_message():
    return 'Выберите пункт меню: '

def show_class_message():
    return 'Введите класс [Доступен 6А и 7Б]: '

def show_discipline_message():
    return 'Введите предмет: [Доступно "математика", "русский язык", "история"] '

def goodbye_message():
    print('До свидания!')

def int_input(message='Введите число: '):
    return int(input(message))

def char_input(message='Введите символ(ы): '):
    return input(message)

def successfully_read_message():
    print('Подключение к БД произведено успешно!')

def successfully_write_message():
    print('Обновление БД произведено успешно!')

def progress_journal_message(this_class:str,discipline:str):
    print(f'Журнал успеваемости "{this_class}" класса по предмету "{discipline}": ')

def list_of_class_message(this_class:str):
    print(f'Список "{this_class}" класса:')

def who_will_answer_message(name):
    print(f'Отвечать будет {name}!')

def who_will_answer():
    return int_input('Кто будет отвечать? [Вводить порядковый номер]: ')

def state_mark():
    return int_input('Введите оценку: ')

# печать списка учеников определенного класса по алфавиту с оценками
def print_students_with_marks(students_list: list, database: list, discipline: str):
    for student_name in students_list:
        for elem in database:
            if student_name == elem['ФИО']:
                if discipline in elem:
                    print(student_name, elem.get(discipline), sep='\t')

# печать нумерованного списка учеников
def print_numbered_list(students_list: list):
    for index, student in enumerate(students_list, start=1):
        print(f'№ {index} - {student}')
