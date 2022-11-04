from os.path import exists
from csv_generator import create_csv
from csv_generator import write_csv
from xml_generator import write_xml
from html_generator import write_html



def get_record():
    record = []
    last_name = input('Введите фамилию: ')
    record.append(last_name)
    first_name = input('Введите имя: ')
    record.append(first_name)
    phone = int(input('Введите номер телефона: '))
    record.append(phone)
    comment = input('Введите комментарий: ')
    record.append(comment)
    return record

def button_click():
    record = get_record()

    path = 'phone_book.csv'
    valid = exists(path)
    if not valid:
        create_csv()
        write_csv(record)
    else:
        write_csv(record)
        
    write_xml(record)
    write_html(record)
