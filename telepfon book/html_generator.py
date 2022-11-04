
def write_html(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head><meta charset="UTF-8"></head>\n  <body>\n'
    html += '    <p {}>Фамилия: {}</p>\n'\
        .format(style, data[0])
    html += '    <p {}>Имя: {}</p>\n'\
        .format(style, data[1])
    html += '    <p {}>Телефон: {}</p>\n'\
        .format(style, data[2])
    html += '    <p {}>Комментарий: {}</p>\n'\
        .format(style, data[3])
    html += '===============================================\n\n'
    html += '  </body>\n</html>'
    
    with open('phone_book.html', 'a', encoding = 'utf-8') as html_file:
        html_file.write(html)

    return html



