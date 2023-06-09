class ParkingGarage():
    def __init__(self, parking_space, tickets, avail_space, employee):
        self.parking_space = parking_space
        self.tickets = tickets
        self.avail_space = avail_space
        self.payers = []
        self.employee = employee
        self.current_ticket = {'Paid': False}
        
    def enter_garage():
        customer = input("What is your name? ")
        self.payers.append(customer)

    
    def check_space():
        print(f"There are {self.parking_space} parking spots available")
        
    def leave_garage():
    
    def change_employee(self):
        change = input("Who is replacing you? ")
        self.employee = change
        print(f"The new parking garage employee is {self.employee}. Be sure to thank them!")

    def run():
        main_garage = ParkingGarage(20, 20, 20, "saraa")
        response1 = input(f"Hello, would you like to park your car or leave the parking lot? P for Park or L for leave ")
        if response1 == 'P':
            main_garage.enter_garage()


class TicketSystem():