from sys import exit


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, TypeError, ValueError):
            return "Command was entered incorrectly."
        except KeyError:
            return "The name you entered could not be found in the database."
    return inner

def hello(*result):
    return "How can I help you?"
    
def end(*result):
    return "Good bye!"


contacts = {'Raymod': '9929143792',
            'Aldend': '9299417329',
            'Dalend': '2994919273'
            }


def parser(user_input:str):
    # result = (command.lower()).split()
    if user_input.startswith("add"):
        return add_new_contact, user_input.removeprefix("add").strip().split()
    elif user_input.startswith("change"):
        return change_phone, user_input.removeprefix("change").strip().split()
    elif user_input.startswith("show all"):
        return show_all_contacts, user_input.removeprefix("show all").strip().split()
    elif user_input.startswith("exit"):
        return end, user_input.removeprefix("exit").strip().split()
    # elif result[0] == "phone":
    #     return (show_phone, result)
    # 
    #     return (end, result)
    # elif result[0] == "hello":
    #     return (hello, result)
    # elif result[0] + " " + result[1] == "show all":
    #     return (show_all_contacts, result)


@input_error
def add_new_contact(*data):
    name, remaining = data
    name = name.lower().capitalize()
    phone = ""
    for i in remaining:
        if not i.isdigit():
            continue
        else:
            phone += i
    contacts[name] = phone
    return f"Contact {name} add"


@input_error
def show_all_contacts(*result):
    result = []
    for i,v in contacts.items():
        result.append(f"{i} {v}")
    return '\n'.join(result)
    

@input_error
def change_phone(*data):
    name, phone = data
    contacts[name] = phone
    return f"Contact {name} change phone"


def main():  # Функція main приймає input від користувача і одразу (без перевірки на правильність) передає його в функцію parser.
    while True:  # Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        print(command(*data))
        if command == end:
            break


if __name__ == "__main__":
    main()
