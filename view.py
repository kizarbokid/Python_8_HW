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


