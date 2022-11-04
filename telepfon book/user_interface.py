from controller import button_click as bc
from print_phonebook import print_phonebook as pp

print()
print('Это телефонный справочник, импортирующий записи в .csv, .xml и .html форматы. Для начала работы нажмите Enter')
input()


while True:
    print()
    user_input = input('Желаете внести запись в телефоную книгу? Нажмите 1. \n'
'Желаете посмотреть существующие записи? Нажмите 2. \n'
'Желаете выйти из программы? Нажмите <Enter> \n >>> ')
    if user_input == '1':
        bc()
    elif user_input == '2':
        pp()
    else:
        print()
        print('Спасибо за использование программы!')
        break


print()


