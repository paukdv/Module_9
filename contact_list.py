
# Словник контактів
contacts = {'Pavlo': '0699999999',
                  'Ruslan': '078888887',
                  'Stefaniya': '4532221111'
}

# Парсер команд
def parse_command(string):
    command_in_string = string.split(' ')
    return command_in_string

# Вітання
def hello_users(string=None):
    print('How can I help you?')

# Додавання нового контакту
def add_contact(string):
    name = parse_command(string)[1]
    number = parse_command(string)[2]
    contacts[name] = number

# Функція зміни наявного контакту
def change_contact(string):
    name = parse_command(string)[1]
    number = parse_command(string)[2]
    contacts[name] = number

# Функція виводу номеру телефона 
def print_phone(string):
    name = parse_command(string)[1]
    print(contacts[name])

# Функція виводу всіх контактів
def show_all():
    for name, number in contacts.items():
        print(name, number)

# Словник команд
command_dict = {
    'hello': hello_users,
    'add': add_contact,
    'change': change_contact,
    'phone': print_phone,
    'show all': show_all
}

# Декоратор для обробки помилок вводу
def input_error(func):
    def wrapper():
        while True:
            try:
                func()
                break
            except KeyError:
                print('Your command is not from the list: "hello", "add", "change" "phone", "good bye", "exit", "close".')
                continue
            except IndexError:
                print('Command should be entered from the list, followed by a space, and then the user"s name and(or) phone number')
                continue
            except ValueError:
                print('Give me a name and/or a phone number please')
                continue
    return wrapper

# Основна функція, що взаємодіє з користувачем
@input_error
def main():
    while True:
        string = input('Please enter your command: ')
        key_command = parse_command(string)[0].lower()
        if string.lower() in ["close", "exit", "good bye"]:
            print('Goodbye!')
            break
        elif key_command == 'show' and parse_command(string)[1].lower() == 'all':
            command_dict['show all']()
        else:
            command_dict[key_command](string)

if __name__ == '__main__':
    main()