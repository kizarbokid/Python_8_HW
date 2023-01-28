import csv

filename='Списки_учеников.csv'
students_list=list()
with open(filename, "r", newline="",encoding='UTF-8') as file:
    reader = csv.DictReader(file,delimiter=';')
    for row in reader:
        row['ФИО']=row.pop('\ufeffФИО') # ключ при импорте некрасивый, правим
        students_list.append(row)

filename='Успеваемость.csv'
progress_list=list()
with open(filename, "r", newline="",encoding='UTF-8') as file:
    reader = csv.DictReader(file,delimiter=';')
    for row in reader:
        row['Ученик']=row.pop('\ufeffУченик') # ключ при импорте некрасивый, правим
        row['Оценки']=list(map(int,row['Оценки'].split(sep=','))) # перевод строки оценок в список чисел
        progress_list.append(row)

for elem in students_list:
        print(elem['ФИО'],elem['КЛАСС'],sep='\t')
    
