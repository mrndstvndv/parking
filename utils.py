import os

def get_key():
    try:
        import msvcrt
        print()
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                
                # Check for the first byte of a special key sequence
                if key == b'\xe0':
                    # Read the second byte which contains the actual key code
                    # This second call will block if the first was not available,
                    # but since kbhit() was true, the second byte should be available
                    # or become available almost immediately.
                    special_key_code = msvcrt.getch() 
                    return (key, special_key_code) # Return both bytes as a tuple
                
                # For regular keys, return the single byte
                return key
    except ImportError:
        return False

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS/POSIX
        _ = os.system('clear')

def prompt(msg = "") -> str:
    return input("\n"+msg + " > ")

def prompt_int(msg):
    while True:
        inpt = input(msg)
        if not inpt.isnumeric():
            print("Please type in a valid integer")
            continue
        return inpt

def prompt_res_no(msg, ps):
    while True:
        inpt = input(msg)
        if not inpt.isnumeric():
            print("Please type in a valid integer")
            continue

        if ps.get_res_by_no(inpt) != None:
            print("Reservation number already exists")
            continue

        return inpt


def prompt_yn(msg):
    while True:
        inpt = input(msg + " [y/n] > ").lower().strip()
        if inpt[0] not in "yn":
            print("You may only enter y/n or Y/N")
            continue
        return inpt

def print_matrix(data):
    widths = {}
    for row in data: 
        for i, col in enumerate(row):
            try:
                if len(col) > widths[i]:
                    widths[i] = len(col)
            except KeyError:
                widths[i] = len(col)
            except Exception as e:
                print(e)

    for row in data:
        print()
        for i, col in enumerate(row):
            print(col.ljust(widths[i]), end="   ")

