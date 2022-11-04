

def print_phonebook():
    with open('phone_book.csv', 'r', encoding = 'utf-8') as pb:
        my_str = pb.read()

    my_str = my_str.replace('\n', ';')
    my_str = my_str.split(';')
    my_str.pop()

    for i in range(4, len(my_str), 4):
        print()
        print(f'{my_str[0]}: {my_str[i]}')
        print(f'{my_str[1]}: {my_str[i + 1]}')
        print(f'{my_str[2]}: {my_str[i + 2]}')
        print(f'{my_str[3]}: {my_str[i + 3]}')
        


    