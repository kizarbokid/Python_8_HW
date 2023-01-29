import csv

# Считывание списка учеников из файла в список словарей
filename = 'Списки_учеников.csv'
students_list = list()
with open(filename, "r", newline="", encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        # ключ при импорте некрасивый, правим
        row['ФИО'] = row.pop('\ufeffФИО')
        students_list.append(row)

# Считывание успеваемости из файла в список словарей
filename = 'Успеваемость.csv'
progress_list = list()
discipline = str()
with open(filename, "r", newline="", encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        # ключ при импорте некрасивый, правим
        #row['ФИО'] = row.pop('\ufeffФИО') почему при первичном экспорте считывался ключ со служебными символами?
        # перевод строки оценок в список чисел
        row['Оценки'] = list(map(int, row['Оценки'].split(sep=',')))
        # Значение ключа "предмет" становится ключом, оценки ученика - значением к ключу
        discipline = row['Предмет']
        row[discipline] = row.pop('Оценки')
        # Ключ "Предмет" больше не нужен
        del row['Предмет']
        progress_list.append(row)

# объединение списков в "базу данных"
database = list()
for student in students_list:
    for marks in progress_list:
        if student['ФИО'] == marks['ФИО']:
            database.append(student | marks)
# for elem in database:
#    print(elem)

# Вывести список оценок учеников заданного класса по заданному предмету, с оценками (начать урок)
input_class = '7б'
# input('Введите класс: ').lower().strip().replace(' ','')
input_discipline = 'русский язык'
# input('Введите предмет: ').lower().strip()
print(
    f'Журнал успеваемости "{input_class}" класса по предмету "{input_discipline}": ')

filtered_students_list = list()
for elem in students_list:
    if elem['КЛАСС'] == input_class:
        filtered_students_list.append(elem['ФИО'])

# сортировка списка учеников
filtered_students_list = sorted(filtered_students_list)

# печать списка учеников определенного класса по алфавиту с оценками
for student_name in filtered_students_list:
    for elem in database:
        if student_name == elem['ФИО']:
            if input_discipline in elem:
                print(student_name, elem.get(input_discipline), sep='\t')

for index, student in enumerate(filtered_students_list, start=1):
    print(f'№ {index} - {student}')

n = 1
# int(input('Кого вызвать к доске? (Вводить порядковый номер): '))
student_name = filtered_students_list[n-1]
print("Отвечать будет", student_name)
mark = 5
# int(input('Оценка за ответ: '))

# Добавить оценку ученику
trigger = True
for i in range(len(database)):
    if database[i]['ФИО'] == student_name and input_discipline in database[i]:
        temp_list = list()
        trigger = False
        temp_list = database[i][input_discipline]
        temp_list.append(mark)
# Если в базе у данного ученика нет оценок по конкретному предмету, то добавтьь новую запись в БД
if trigger:
    marks = list()
    marks.append(mark)
    database.append(
        {'КЛАСС': input_class, 'ФИО': student_name, input_discipline: marks})

for elem in database:
    print(elem)


# печать списка учеников определенного класса по алфавиту с оценками
for student_name in filtered_students_list:
    for elem in database:
        if student_name == elem['ФИО']:
            if input_discipline in elem:
                print(student_name, elem.get(input_discipline), sep='\t')


# Разделить базу Данных, чтобы затем записать ее в файл
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

for elem in progress_list_export:
    print(elem)

    
filename = 'Успеваемость.csv'
 
with open(filename, "w", newline="",encoding='UTF-8') as file:
    columns = ['ФИО','Предмет','Оценки',]
    writer = csv.DictWriter(file, fieldnames=columns,delimiter=';')
    writer.writeheader()
    # запись нескольких строк
    writer.writerows(progress_list_export)