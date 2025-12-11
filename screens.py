from app import Screen
from system import ParkingSystem
import textwrap
from utils import prompt, prompt_int, prompt_yn, clear_screen

class PScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.ps = self.app.context["ps"]

class MakeReservationScreen(PScreen):
    def show(self):
        print(textwrap.dedent("""
        ### Make A Reservation ###
        
        """))
        
        res_no = prompt_int("Reservation no: ")
        name = input("Name: ")
        date = input("Date: ")
        time = input("Time: ")
        vehicle_type = input("Vehicle Type: ")
        plate_number = input("Plate Number: ")  

        if prompt_yn("Proceed?") == "y":
            self.ps.add_reservation(res_no, date, time, name, vehicle_type, plate_number)

            self.back()

class MainScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.app.context["ps"] = ParkingSystem("reservations.csv")
    
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
            self.go(MakeReservationScreen)