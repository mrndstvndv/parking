from app import App
from screens import MainScreen
from system import ParkingSystem

App(MainScreen, {"ps": ParkingSystem("reservations.csv")}).run()