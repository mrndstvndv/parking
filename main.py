from system import ParkingSystem
from utils import prompt, prompt_int, prompt_yn, clear_screen

parking_main = ("""
### Parking Reservation System ###

System Menu

a. View All Reservations
b. Make Reservation
c. Update Reservation
d. Cancel Reservation
e. Generate Report
f. Exit
""")

ps = ParkingSystem("reservations.csv")

class Menu:
    def __init__(self, msg, on_input):
        self.msg = msg
        self.on_input = on_input

    def logic(self):
        pass

    def display(self):
        print(self.msg) 

        self.logic()
        
        self.on_input(input("> ").lower())

class MakeReservation(Menu):
    def __init__(self, msg, logic = None):
        self.msg = msg

    def logic(self):
        res_no = prompt_int("Reservation no: ")
        name = input("Name: ")
        date = input("Date: ")
        time = input("Time: ")
        vehicle_type = input("Vehicle Type: ")
        plate_number = input("Plate Number: ")  

        if prompt_yn("Proceed?") == "y":
            ps.add_reservation(res_no, date, time, name, vehicle_type, plate_number)

            global menu
            menu = main_menu

    def display(self):
        print(self.msg) 

        self.logic()

class UpdateReservation(Menu):
    def __init__(self, msg, logic = None):
        self.msg = msg

    def logic(self): 
        res_no = None

        while True:
            res_no = prompt_int("Reservation no: ")
            row = ps.get_res_by_no(res_no)
            if row is None:
                print("Reservation No. is not found in the system")
            else:
                print()
                ps.display_row(row)
                print()
                break        

        print("""
Select the data to update
[N]ame
[D]ate
[T]ime
[V]ehicle Type
[P]late Number
""")
        
        selection = None
        while True:
            selection = prompt().lower().strip()

            if len(selection)>1 or selection not in "ndtvp":
                print("Invalid input")
                continue
            else: 
                break

        print()

        if selection == "n":
            i = input("Enter new name: ")
            ps.update_reservation(res_no, name=i)
        elif selection == "d":
            i = input("Enter new date: ")
            ps.update_reservation(res_no, date=i)
        elif selection == "t":
            i = input("Enter new time: ")
            ps.update_reservation(res_no, time=i)
        elif selection == "v":
            i = input("Enter new vehicle type: ")
            ps.update_reservation(res_no, vehicle=i)
        elif selection == "p":
            i = input("Enter new plate number: ")
            ps.update_reservation(res_no, plate_number=i)

        print("\nRESERVATION SUCCESSFULLY UPDATED\n")

        input("Press any key to go back to menu...")

        global menu
        menu = main_menu

    def display(self):
        print(self.msg) 

        self.logic()

class CancelReservation(Menu):
    def __init__(self, msg, logic = None):
        self.msg = msg

    def logic(self):
        res_no = None

        while True:
            res_no = prompt_int("Reservation no: ")
            row = ps.get_res_by_no(res_no)
            if row is None:
                print("Reservation No. is not found in the system")
            else:
                print()
                ps.display_row(row)
                print()
                break        

        global menu

        if prompt_yn("\nProceed?") == "y":
            ps.cancel_reservation(res_no)

        menu = main_menu


    def display(self):
        print(self.msg) 

        self.logic()

class GenerateReport(Menu):
    def __init__(self, msg, logic = None):
        self.msg = msg

    def logic(self):
        date = input("Date: ")

        print()

        ps.report(date=date)

        input("Press any key to go back to menu...")

        global menu
        menu = main_menu

    def display(self):
        print(self.msg) 

        self.logic()

global menu
 
def main_input(x):
    global menu

    if x == "b":
        menu = MakeReservation("\nMake reservation\n")
    if x == "a":
        clear_screen()
        print()
        ps.view_reservations()
        prompt("Enter to continue")
    if x == "c":
        menu = UpdateReservation("\nUpdate Reservation\n")
    if x == "d":
        menu = CancelReservation("\nCancel Reservation\n")
    if x == "e":
        menu = GenerateReport("\nGenerate Reservations Report\n")
    if x == "f":
        exit()

main_menu = Menu(parking_main, main_input)

menu = main_menu

# Mainu

from app import App, Screen
from screens import MainScreen

App(MainScreen).run()