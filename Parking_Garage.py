class ParkingGarage():
    def __init__(self, parking_space, tickets_given, avail_spaces, employee):
        self.parking_space = parking_space
        self.tickets_given = tickets_given
        self.avail_spaces = avail_spaces
        self.payers = []
        self.employee = employee
        self.current_ticket = {'Paid': False}
        
    def enter_garage(self):
        # customer = input("What is your name? ")
        # self.payers.append(customer)
        print("")
        if self.avail_spaces <= 0:
            print("Sorry, the parking lot is full.")
        else:
            print("We have space for your car. Welcome to the garage!")
            self.tickets_given += 1
            self.avail_spaces -= 1
        print("")

    def check_space(self):
        print(f"There are {self.avail_spaces} parking spots available")
        print(f"There are {self.tickets_given} tickets given out.")
        
    def leave_garage(self):
        hours_parked = float(input("How many hours have you parked here? "))
        total_price = hours_parked * 5
        print(f"You parked for: {hours_parked} hours  |   Total price: ${total_price: .2f}")
        self.tickets_given -= 1
        self.avail_spaces += 1
    
    def change_employee(self):
        change = input("Who is replacing you? ")
        self.employee = change
        print(f"The new parking garage employee is {self.employee}. Be sure to thank them!")

class Main():
    def show_prices():
        print("Welcome to S&K Garage. Here are our prices.")
        print("""
            0 to 1 hours: $10.00
            >1 to 2 hours: $12.00
            >2 to 3 hours: $15.00
            >3 hours: $20.00
        """)

    def run():
        main_garage = ParkingGarage(20, 20, 20, "saraa")
        response1 = input(f"Hello, would you like to park your car or leave the parking lot? P for Park or L for leave ")
        if response1 == 'P':
            main_garage.enter_garage()


class GarageWorker():
    pass

class Driver():
    pass

main_garage = ParkingGarage(20, 0, 20, "saraa")
main_garage.leave_garage()