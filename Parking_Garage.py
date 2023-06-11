class ParkingGarage():
    def __init__(self, parking_space, avail_spaces):
        self.parking_space = parking_space
        self.tickets_given = parking_space - avail_spaces
        self.avail_spaces = avail_spaces
        self.employee = ''
        self.unpayed_customers = []
        self.payed_customers = {}#key = customers name| value = payed amount
        self.total_price = 0
        self.total_tip_amount = []
        self.customer = ''
        self.name_leaving = ''
        self.payed_amount = 0
        self.current_ticket = {'Paid': False}
        
    def enter_garage(self):
        if self.avail_spaces <= 0:
            print("Sorry, the parking lot is full. Please turn around.")
            print("")
        else:
            print("Welcome to S&K Garage")
            self.customer = input("What is your name? ")
            print("")
            print("We have space for your car. Welcome to the garage!")
            print("We charge $5 per hour. Take a ticket and pay when you leave.")
            self.tickets_given += 1
            self.avail_spaces -= 1
            print("You are now parked. ")
            print("----------")
            print("Welcome new customer!")
            self.unpayed_customers.append(self.customer)

    def check_space(self):
        print("")
        print("Parking Lot Status:")
        print(f"There are {self.parking_space} in total. ")
        print(f"There are {self.avail_spaces} parking spots available")
        print(f"There are {self.tickets_given} tickets given out.")
        print("")
        
    def leave_garage(self):
        while True:
            self.name_leaving = input("What is your name? ")
            if self.name_leaving in self.unpayed_customers:
                self.unpayed_customers.remove(self.name_leaving)
                while True:
                    hours = input(f"How many hours have you parked here {self.name_leaving.title()}? ")
                    try:
                        hours_parked = int(hours)
                        break
                    except ValueError:
                        print("Please enter numbers only")

                self.total_price = hours_parked * 5
                print(f"You parked for: {hours_parked} hours  |   Total price: ${self.total_price: .2f}")
                self.tickets_given -= 1
                self.avail_spaces += 1
                break
            else:
                print("That is an invalid name. Try again")
           
            
                
    
    def payment(self):
        add_money = 0
        while True:
            number = input(f"Enter the amount you are paying {self.name_leaving}: ")
            try:
                self.payed_amount = int(number)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")
            
        while True:
            if self.payed_amount == self.total_price:
                print(f"Thank for your payment {self.name_leaving}. Have a nice day. ")
                print("")
                break
            elif self.payed_amount >= self.total_price:
                tip_amount = self.payed_amount - self.total_price
                print(f"Thank you {self.name_leaving.title()} for your ${tip_amount: .2f} tip. ")
                self.total_tip_amount.append(tip_amount)
                break
            else:
                amount_owed = self.total_price - self.payed_amount
                print(f"Sorry {self.name_leaving.title()} that is the wrong amount. You cannot leave the garage. You still owe ${amount_owed: .2f}")
                while True:
                    money = input("Please give more money: ")
                    try:
                        add_money = int(money)
                        self.payed_amount += add_money
                        break
                    except ValueError:
                        print("Please enter numbers only")
                    

        self.payed_customers[self.name_leaving] = self.payed_amount      # creating the dictionary of customers and the amount they paid


class Employee(ParkingGarage):
    def __init__(self, payed_customers, payed_amount):
        super().__init__(payed_customers, payed_amount)
        self.employee = 'Saraa'

    def current_employee(self):
        print("")
        print(f"Current employee is {self.employee} if you need any help ")
        print("")
        
        print("")

    def change_employee(self):
        print("")
        change = input("Who is replacing you? ")
        self.employee = change
        print(f"The new parking garage employee is {self.employee}. Have a great day working at the garage, {self.employee}!")
        print("")

    def total_income(self):
        print(f"Unpaid customers: {self.unpayed_customers}")
        print("")
        print("These are the customers who have paid:")
        for name, amount in self.payed_customers.items():
            print(f"{name} - ${amount: .2f} | ")
        print(f"Total earnings: ${sum(self.payed_customers.values()): .2f}")
        print("")

    def employee_tips(self):
        self.tips = sum(self.total_tip_amount)
        print(f"Total tips is ${self.tips: .2f}")


class Main():

    def run():

        main_garage = Employee(20, 20)
        
        print("Welcome to S&K Parking Garage!")
        while True:
            response = input("Are you an employee or a customer? 'E' for employee or 'C' for customer or 'Q' to quit ")
        
            if response.lower() == 'e':
                while True:
                    response3 = input("Enter 'name' to get current employee name, 'change' to change employee, 'income' for to get total income, or 'q' for quit  or 'tips' for employee tips ")            
                    if response3.lower() == 'name':
                        main_garage.current_employee()
                    elif response3.lower() == 'change':
                        main_garage.change_employee()
                    elif response3.lower() == 'income':
                        main_garage.total_income()
                    elif response3.lower() == 'tips':
                        main_garage.employee_tips()
                    elif response3.lower() == 'q':
                        break
                    else:
                        print("Invalid response, try again")

            elif response.lower() == 'c':
                while True:
                    response1 = input(f"Would you like to park your car or leave the parking lot? P for Park or L for Leave or Q to quit ")
                    if response1.lower() == 'l':
                        main_garage.leave_garage()
                        main_garage.payment()
                    elif response1.lower() == 'p':
                        main_garage.check_space()
                        main_garage.enter_garage()
                    elif response1.lower() == 'q':
                        break
                    else:
                        print("Invalid response")
            elif response.lower() == 'q':
                print("Have a nice day! ")
                break
            else:
                print("Invalid response. Try aqain. ")


main_garage = Main
main_garage.run()




