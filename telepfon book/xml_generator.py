

def write_xml(data):
    xml = '<xml>\n'
    xml += '    <first_name = "Фамилия">{}</first_name>\n'\
        .format(data[0])
    xml += '    <second_name = "Имя">{}</second_name>\n'\
        .format(data[1])
    xml += '    <phone = "Телефон">{}</phone>\n'\
        .format(data[2])
    xml += '    <comment = "Комментарий">{}</comment>\n'\
        .format(data[3])
    xml += '</xml>\n'

    with open('phone_book.xml', 'a', encoding = 'utf-8') as xml_file:
        xml_file.write(xml)
    
    return xml



