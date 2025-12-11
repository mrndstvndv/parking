import os

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS/POSIX
        _ = os.system('clear')

def prompt(msg = "") -> str:
    return input("\n" +msg + " > ")

def prompt_int(msg):
    while True:
        inpt = input(msg)
        if not inpt.isnumeric():
            print("Please type in a valid integer")
            continue
        return inpt

def prompt_yn(msg):
    while True:
        inpt = input(msg + " [y/n] > ").lower().strip()
        if inpt[0] not in "yn":
            print("You may only enter y/n or Y/N")
            continue
        return inpt