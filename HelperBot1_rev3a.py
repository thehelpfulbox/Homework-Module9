
from sys import exit


def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError or TypeError or ValueError:
            print(f"Command was entered incorrectly.")
        except KeyError:
            print(f"The name you entered could not be found in the database.")
    return inner

def hello(result):
    print("How can I help you?")
    return None
    
def end(result):
    print("Good bye!")
    return exit()


contacts = {'Raymod': '9929143792',
            'Aldend': '9299417329',
            'Dalend': '2994919273'
            }


def parser(command):
    result = (command.lower()).split()
    if result[0] in ("add", "change"):
        return (add_new_contact, result)     
    elif result[0] == "phone":
        return (show_phone, result)
    elif result[0] in ("exit", "close", "good bye"):
        return (end, result)
    elif result[0] == "hello":
        return (hello, result)
    elif result[0] + " " + result[1] == "show all":
        return (show_all_contacts, result)


@input_error
def add_new_contact(command):
    _, name, remaining = command
    name = name.lower().capitalize()
    phone = ""
    for i in remaining:
        if not i.isdigit():
            continue
        else:
            phone += i
    contacts[name] = phone
    return None


@input_error
def show_all_contacts(result):
    for i,v in contacts.items():
        print(i, v)
    

@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return None


def main():  # Функція main приймає input від користувача і одразу (без перевірки на правильність) передає його в функцію parser.
    while True:  # Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.
        result = parser(input(">>>").lower())
        result[0](result[1])


if __name__ == "__main__":
    main()
