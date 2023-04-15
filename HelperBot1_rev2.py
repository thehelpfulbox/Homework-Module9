"""
- Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error.
- Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name", "Give me name and phone please" и т.п.
- Декоратор input_error должен обрабатывать исключения, которые возникают в функциях-handler (KeyError, ValueError, IndexError) и возвращать соответствующий ответ пользователю.
+ Логика команд реализована в отдельных функциях и эти функции принимают на вход одну или несколько строк и возвращают строку.
? Вся логика взаимодействия с пользователем реализована в функции main, все print и input происходят только там.
"""

from sys import exit


def end():
    print("Good bye!")
    return exit()


contacts = {'Raymod': '9929143792',
            'Aldend': '9299417329',
            'Dalend': '2994919273'
            }


def input_error(func):  # Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error.
    # "Enter user name", "Give me name and phone please" и т.п.
    # Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name", "Give me name and phone please" и т.п.
    # Декоратор input_error должен обрабатывать исключения, которые возникают в функциях-handler (KeyError, ValueError, IndexError) и возвращать соответствующий ответ пользователю.
    pass

# @input_error
def parser(command):  # Парсер команд. Часть, которая отвечает за разбор введенных пользователем строк, выделение из строки ключевых слов и модификаторов команд.
    if command.startswith("add ") or command.startswith("change "):
        #name, *remaining = command
        command = command.split(" ", 2)
        command = command[1:]
        name = command[0].capitalize()
        phone = []
        for i in command[1]:
            if not i.isdigit():
                continue
            elif i.isdigit() and len(phone) > 0 and phone[-1].isdigit():
                phone[-1] += i
            else:
                phone += i
        return (adder, name, phone[-1])
        # adder(name, phone[-1])
    elif command.startswith("phone "):
        command = command.split(" ", 1)
        name = command[1].capitalize()
        return (contacts[name])


# Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают за непосредственное выполнение команд.

def adder(name, phone):
    contacts[name] = phone
    return None


def main():
    while True:  # Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.
        command = input(">>>")
        if command == "hello":
            print("How can I help you?")
        elif command == "good bye" or command == "close" or command == "exit":
            end()
        elif command.startswith("add ") or command.startswith("change "):
            result = parser(command)
            result[0](result[1], result[2])
        elif command.startswith("phone "):
            print(parser(command))
        elif command.startswith("show all"):
            for i,v in contacts.items():
                print(i, v)
        else:
            print("""You entered an unknown command.The valid commands are:
                  "hello"
                  "add [name] [phone_number]" - Adds new contact: name and phone number must be saparated by a space.
                  "change [name] [phone_number]" - Replaces the phone number for existing contact: name and phone number must be saparated by a space.
                  "phone [name]" - Shows phone number for the existing contact.
                  "show all" - Shows the list of all contacts with phone numbers.
                  "good bye" or "close" or "exit" - Exits the program.
                  """)


if __name__ == "__main__":
    main()
