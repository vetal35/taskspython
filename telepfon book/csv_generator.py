

def create_csv():
    file = 'phone_book.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Телефон;Описание\n')
        
        
def write_csv (data):
    file = 'phone_book.csv'
    with open (file, 'a', encoding = 'utf-8') as csv_file:
        csv_file.write(f'{data[0]};{data[1]};{data[2]};{data[3]}\n')




