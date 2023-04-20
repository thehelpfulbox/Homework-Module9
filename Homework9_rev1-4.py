contacts = {'Rian': '9929143792',
            'Aldo': '9299417329',
            'Dale': '2994919273',
            'Jane': '2873648723'
            }


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, TypeError, ValueError):
            return "Command was entered incorrectly."
        except KeyError:
            return "Can't find such name in the database."
    return inner


@input_error
def hello(*result):
    return "How can I help you?"


@input_error
def end(*result):
    return "Good bye!"


def unknown_input(*command):
    return "Unknown command"


def parser(user_input:str):
    user_input = user_input.lower()
    if user_input.startswith("add"):
        return add_new_contact, user_input.removeprefix("add").strip().split()
    elif user_input.startswith("hello"):
        return hello, user_input.removeprefix("hello").strip().split()
    elif user_input.startswith("change"):
        return change_phone, user_input.removeprefix("change").strip().split()
    elif user_input.startswith("phone"):
        return show_phone, user_input.removeprefix("phone").strip().split()
    elif user_input.startswith("show all"):
        return show_all_contacts, user_input.removeprefix("show all").strip().split()
    elif user_input.startswith("exit") or user_input.startswith("close") or user_input.startswith("good bye"):
        return end, user_input
    else:
        return unknown_input, user_input


@input_error
def add_new_contact(*data):
    name, remaining = data
    name = name.lower().capitalize()
    if name in contacts.keys():
        return f'The record with name "{name}" already exists in the database. Nothing was added.'
    phone = ""
    for i in remaining:
        if not i.isdigit():
            continue
        else:
            phone += i
    if len(phone) == 0:
        return f"Can't create the record '{name}'. The number that you entered does not contain any digits."
    else:
        contacts[name] = phone
        return f'Contact "{name}" was added with phone "{phone}"'


@input_error
def show_phone(*result):
    name = result[0].lower().capitalize()
    return contacts[name]


@input_error
def show_all_contacts(*result):
    result = []
    for i,v in contacts.items():
        result.append(f"{i} {v}")
    return '\n'.join(result)
    

@input_error
def change_phone(*data):
    name, phone = data
    name = name.lower().capitalize()
    if not (name in contacts.keys()):
        return f'The name "{name}" was not found in the database'
    else:
        sanitized_phone = ""
        for i in phone:
            if not i.isdigit():
                continue
            else:
                sanitized_phone += i
        if len(sanitized_phone) == 0:
            return f"The number that you entered does not contain any digits"
        else:
            contacts[name] = sanitized_phone
            return f'The phone number of contact "{name}" was changed to "{sanitized_phone}"'


def main():
    while True:
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        print(command(*data))
        if command == end:
            break


if __name__ == "__main__":
    main()

