contacts = {}


def input_error(func):
    
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Contact with that name not found.'
        except ValueError:
            return 'Please enter a valid command.'
        except IndexError:
            return 'Please enter both name and phone number, separated by a space.'
    return wrapper

@input_error
def hello(*args):
    return """How can I help you?"""

@input_error
def add(*args):
    _, name, phone = args[0].split()
    contacts[name] = phone
    return f'Contact: {name} and phone: {phone} - has been added.'


@input_error
def change(*args):
    _, name, phone = args[0].split()
    if name in contacts:
        contacts[name] = phone
        return f'Phone number changed for {name}.'
    else:
        return f'Contact {name} not found.'
    

@input_error
def phone(*args):
    _, name = args[0].split()
    if name in contacts:
        return f'Phone number for contact {name} is {contacts[name]}.'
    else:
        return f'Contact with name {name} is not defined.'
    
@input_error
def show_all(*args):
    if contacts:
        contacts_string = ""
        for name, phone in contacts.items():
            contacts_string += f"{name} : {phone}\n"
        return contacts_string
    else:
        return 'No contacts.'
    
@input_error
def exit(*args):
    return "Good bye"

@input_error
def close(*args):
    return "Good bye"

@input_error
def good_bye(*args):
    return "Good bye"

@input_error
def no_command(*args):
    return "Unknown command try again"


COMMANDS = {hello: 'hello',
            add: 'add',
            exit: 'exit',
            close: 'close',
            good_bye: 'good by',
            phone: 'phone',
            change: 'change',
            show_all: 'show all'}

def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.lower().startswith(kword):
            return command, text.replace(kword, '').strip()
    return None, ''

def main():
    
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)
        if not command:
            print("Unknown command, try again.")
            continue
        print(command(data))
        if command == exit or close or good_bye:
            break


if __name__ == '__main__':
    main()
