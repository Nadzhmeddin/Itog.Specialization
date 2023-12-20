from datetime import date
import datetime
import os

def show_notes(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        
        for note in data:
            print(note, end ='')

    input('\nНажмите любую кнопку')

def add_note(file_name):
    os.system('CLS')
    noteDate = str(datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'))
    with open(file_name, 'a', encoding='utf-8') as file:
        res =''
        res += input('Введите идентификатор заметки id: ') + '. '
        res += input('Введите заголовок заметки: ') + ': '
        res += input('Введите тело заметки: ') + ', '
        res += ('Дата создания: ') + noteDate + ';'
        file.write('\n' + res)

    input("Заметка успешно сохранена. Нажмите любую кнопку для возврата")

def search_note(file_name):
    os.system('CLS')
    current_note = input("Введите заголовок заметки: ")

    with open(file_name, 'r', encoding='utf-8') as file:
        notes = file.readlines()
        for note in notes:
            if current_note in note:
                print(note)
                break
        else :
            print("С такими данными заметка не найдена!")

    input("Нажмите любую кнопку")
   
def edit_note(file_name):
    os.system("cls")
    with open(file_name, 'r', encoding='utf-8') as file:
        note = sorted(file.readlines())
        print(note)

        numberNote = int(input("Введите номер строки заметки для изменения данных: "))
        print(note[numberNote - 1].rstrip().split(","))
        if numberNote != 0:
            newIdNote = input("Введите новый ID заметки: ")
            newHeadingNote = input("Введите новый заголовок для заметки: ")
            newBodyNote = input("Введите тело заметки: ")
            note[numberNote - 1] = (newIdNote + "," + newHeadingNote + "," + newBodyNote + "\n")
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write("".join(note))
                print("\nДанные заметки изменены!")
        else:
            return

    input("Нажмите любую кнопку")


def delete_note(file_name):
    os.system('CLS')
    
    current_note = int(input("Введите номер строки для удаления: ")) -1 

    with open(file_name, 'r', encoding='utf-8') as file: 
        note = file.read()
        print(note)
        notes = note.split("\n")
        del_notes = notes[current_note]
        notes.pop(current_note)
        print(f"Заметка удалена {del_notes}\n")
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("\n".join(notes))
                
    input("Нажмите любую кнопку")


def drawing():
    print("Добро пожаловать в приложение Заметки.\n Выберите действие: ")
    print('1 - Показать заметки из справочника')
    print('2 - Добавить заметку в справочник')
    print('3 - Поиск заметки из справочника')
    print('4 - Удалить заметку из справочника')
    print('5 - Изменить данные заметки')
    print('6 - Выход из приложения')

def main (file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Введите номер от 1 до 6: "))

        if user_choice == 1 :
            show_notes(file_name)
        elif user_choice == 2:
            add_note(file_name)
        elif user_choice == 3:
            search_note(file_name)
        elif user_choice == 4:
            delete_note(file_name)
        elif user_choice == 5:
            edit_note(file_name)
        elif user_choice == 6:
            print("Уже уходишь? Пока! Возвращайся!")
            return
        

main('test.csv')
