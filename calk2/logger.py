def data_log(data, endline):

    with open('log.csv', 'a') as file:
        file.write('{}'.format(data))
        if endline == 2:
           file.write(' \n') 
        elif endline == 1:
            file.write(' ')