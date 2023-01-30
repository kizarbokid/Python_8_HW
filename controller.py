import model
import view


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
                this_class = view.char_input(view.show_class_message()).lower().strip().replace(' ','')
                input_discipline = view.char_input(view.show_discipline_message()).lower().strip()
                view.progress_journal_message(this_class,input_discipline)
                filtered_students_list = model.filter_list_of_students(students_list, this_class)
                view.print_students_with_marks(filtered_students_list, database, input_discipline)
                view.list_of_class_message(this_class)
                view.print_numbered_list(filtered_students_list)
                n = view.who_will_answer()
                student_name = filtered_students_list[n-1]
                view.who_will_answer_message(student_name)
                mark = view.state_mark()
                model.write_mark(database, this_class, student_name, input_discipline, mark)
                view.print_students_with_marks(filtered_students_list, database, input_discipline)

            case 3: #Посмотреть поименный список класса
                this_class = view.char_input(view.show_class_message()).lower().strip().replace(' ','')
                filtered_students_list = model.filter_list_of_students(students_list, this_class)
                view.list_of_class_message(this_class)
                view.print_numbered_list(filtered_students_list)

            case 4: #Посмотреть оценки по предмету определенного класса
                this_class = view.char_input(view.show_class_message()).lower().strip().replace(' ','')
                input_discipline = view.char_input(view.show_discipline_message()).lower().strip()
                view.progress_journal_message(this_class,input_discipline)
                filtered_students_list = model.filter_list_of_students(students_list, this_class)
                view.print_students_with_marks(filtered_students_list, database, input_discipline)

            case 5: #Записать в файл
                model.write_to_file(database)
                view.successfully_write_message()
    else:
        view.goodbye_message()   