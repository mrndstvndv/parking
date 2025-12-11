import os
import csv
import utils
import textwrap

class ParkingSystem:

    headers = ["#", "Date", "Time", "Name", "Vehicle Type", "Plate Number"]

    def __init__(self, filename):
        self.data = []
        self.filename = filename

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.data = [{"#": x[0], "Date": x[1], "Time": x[2], "Name": x[3], "Vehicle Type": x[4], "Plate Number": x[5]} for i, x in enumerate(csv.reader(file)) if i != 0]

    def save(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=ParkingSystem.headers)

            writer.writeheader()

            writer.writerows(self.data)

    def add_reservation(self, no, date, time, name, vehicle, plate_number):
        row = {
            "#": no,
            "Date": date,
            "Time": time,
            "Name": name,
            "Vehicle Type": vehicle,
            "Plate Number": plate_number
        }
        self.data.append(row)
        self.save()

        return row

    def get_res_by_no(self, no):
        for row in self.data:
            if row["#"] == no:
                return row
        
        return None

    def cancel_reservation(self, res_no):
        self.data.remove(self.get_res_by_no(res_no)) 
        self.save()

    def update_reservation(self, no, date = None, time = None, name = None, vehicle = None, plate_number = None):
        row = self.get_res_by_no(no)

        if date is not None:
            row["Date"] =  date

        if time is not None:
            row["Time"] =  time

        if name is not None:
            row["Name"] =  name

        if plate_number is not None:
            row["Plate Number"] =  plate_number

        if vehicle is not None:
            row["Vehicle Type"] =  vehicle

        self.save()

    def display_row(self, row):
        print()
        d = [list(row.values())]
        d.insert(0, ParkingSystem.headers)
        utils.print_matrix(d)
    
    def report(self, date: str):
        print(textwrap.dedent(f"""
        Generated Report For {date}"""))

        d = [list(x.values()) for x in self.data if x["Date"] == date]
        d.insert(0, ParkingSystem.headers)

        utils.print_matrix(d)

        print()

 
    def view_reservations(self):
        d = [list(x.values()) for x in self.data]
        d.insert(0, ParkingSystem.headers)

        utils.print_matrix(d)
        print()
