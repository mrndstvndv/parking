from app import Screen
from system import ParkingSystem
import textwrap
from utils import prompt, prompt_yn, prompt_res_no

class PScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.ps: ParkingSystem = self.app.context["ps"]

class GenerateReportScreen(PScreen):
    def show(self):
        print("\n### Generate Report Screen ###\n")

        date = input("Date: ")

        print()

        self.ps.report(date=date)

        input("\nPress any key to go back to menu...")

        self.back()

class ViewAllReservationsScreen(PScreen):
    def show(self):
        print("\n### All Reservations ###")

        self.ps.view_reservations()

        prompt("Go back")
        self.back()

class CancelReservationScreen(PScreen):
    def show(self):
        res_no = self.ps.select_row("### Cancel Reservation ###")

        if prompt_yn("\nProceed?") == "y":
            self.ps.cancel_reservation(res_no)

        self.back()

class UpdateReservationScreen(PScreen):
    title = "\n### Update Reservation ###"

    def show(self):
        res_no = self.ps.select_row(self.title)

        print(textwrap.dedent("""
            Select the data to update
            [N]ame
            [D]ate
            [T]ime
            [V]ehicle Type
            [P]late Number
        """))
        
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
            self.ps.update_reservation(res_no, name=i)
        elif selection == "d":
            i = input("Enter new date: ")
            self.ps.update_reservation(res_no, date=i)
        elif selection == "t":
            i = input("Enter new time: ")
            self.ps.update_reservation(res_no, time=i)
        elif selection == "v":
            i = input("Enter new vehicle type: ")
            self.ps.update_reservation(res_no, vehicle=i)
        elif selection == "p":
            i = input("Enter new plate number: ")
            self.ps.update_reservation(res_no, plate_number=i)

        print("\nRESERVATION SUCCESSFULLY UPDATED\n")

        input("Press any key to go back to menu...")

        self.back()

class MakeReservationScreen(PScreen):
    def show(self):
        print(textwrap.dedent("""
        ### Make A Reservation ###
        
        """))
        
        res_no = prompt_res_no("Reservation Number: ", self.ps)
        name = input("Name: ")
        date = input("Date: ")
        time = input("Time: ")
        vehicle_type = input("Vehicle Type: ")
        plate_number = input("Plate Number: ")  

        if prompt_yn("\nConfirm?") == "y":
            row = self.ps.add_reservation(res_no, date, time, name, vehicle_type, plate_number)

            self.ps.display_row(row)

            prompt()

        self.back()

class MainScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
    
    def show(self):
        print(textwrap.dedent("""
        ### Parking Reservation System ###
        
        System Menu
        
        a. View All Reservations
        b. Make Reservation
        c. Update Reservation
        d. Cancel Reservation
        e. Generate Report
        f. Exit
        """))
        
        i = input("> ")
        
        if i == "f":
            exit()
        elif i == "a":
            self.go(ViewAllReservationsScreen)
        elif i == "b":
            self.go(MakeReservationScreen)
        elif i == "c":
            self.go(UpdateReservationScreen)
        elif i == "d":
            self.go(CancelReservationScreen)
        elif i == "e":
            self.go(GenerateReportScreen)
