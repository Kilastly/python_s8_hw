def input_last_name():
    return input('Введите фамилию: ').title()

def input_first_name():
    return input('Введите имя: ').title()

def input_middle_name():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите телефон: ')

def input_address():
    return input('Введите адрес: ').title()

def creat_row():
    last_name = input_last_name()
    first_name = input_first_name()
    middle_name = input_middle_name()
    phone = input_phone()
    address = input_address()
    return f'{last_name} {first_name} {middle_name}: {phone}\n{address}\n\n'

def add_row():
    # with open('data.txt', 'a', encoding= 'utf8') as file:
    #     file.write(creat_row())
    contact_str = creat_row()
    with open('data.txt', 'a', encoding= 'utf8') as file:
        file.write(contact_str)

def print_data():
    # with open('data.txt', 'r', encoding= 'utf8') as file:
    #    print(file.read())
    with open('data.txt', 'r', encoding= 'utf8') as file:
        data_str = file.read()

    contacts_list = data_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):

        print(n, contact)
        # print(*contact)

def search_contact():
    print('Поиск:\n'
            '1. по фамилии\n'
            '2. по имени\n'
            '3. по отчеству\n'
            '4. по телефону\n'
            '5. по адресу'
            )
    var = input('Выберите вариан поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        var = input('Ошибка! Выберите вариан поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по телефону\n'
        '5. по адресу'
            )
    i_var = int(var) - 1
 
    serch = input('введите данные для поиска: ').title()
    with open('data.txt', 'r', encoding= 'utf8') as file:
        data_str = file.read()

    contacts_list = data_str.rstrip().split('\n\n')
    # print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if serch in  lst_contact[i_var]:

            print(str_contact)
    



def ui():
    with open('data.txt', 'a', encoding= 'utf8'):
        pass
    var = None
    while var != 4:
        print('Список возможных действий:\n'
            '1. Добавить контакт\n'
            '2. Показать все контакты\n'
            '3. Поиск контакта\n'
            '4. Выход'
            )
        print()
        var = input('Введите номер необходимого действия: ')
        while var not in ('1', '2', '3', '4'):
            var = input('Ошибка! Введите номер необходимого действия:\n'
                '1. Добавить контакт\n'
                '2. Показать все контакты\n'
                '3. Поиск контакта\n'
                '4. Выход\n'
                )
        print()
        match var:
            case '1':
                add_row()
            case '2':
                print_data()
            case '3':
                search_contact()
            case '4':
                print('До новых встреч!')
                break
        print()



if __name__ == '__main__':
    ui()