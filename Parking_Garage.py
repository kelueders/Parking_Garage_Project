class ParkingGarage():
    def __init__(self, parking_space, avail_spaces):
        self.parking_space = parking_space
        self.tickets_given = parking_space - avail_spaces
        self.avail_spaces = avail_spaces
        self.unpayed_customers = []
        self.payed_customers = {}#key = customers name| value = payed amount
        self.total_price = 0
        self.customer = ''
        self.payed_amount = 0
        self.current_ticket = {'Paid': False}
        
    def enter_garage(self):
        self.customer = input("What is your name? ")
        print("")
        if self.avail_spaces <= 0:
            print("Sorry, the parking lot is full.")
        else:
            print("We have space for your car. Welcome to the garage!")
            self.tickets_given += 1
            self.avail_spaces -= 1
            print("You are now parked. ")
            self.unpayed_customers.append(self.customer)

    def check_space(self):
        print(f"There are {self.parking_space} in total. ")
        print(f"There are {self.avail_spaces} parking spots available")
        print(f"There are {self.tickets_given} tickets given out.")
        
    def leave_garage(self):
        hours_parked = float(input("How many hours have you parked here? "))
        self.total_price = hours_parked * 5
        print(f"You parked for: {hours_parked} hours  |   Total price: ${self.total_price: .2f}")
        self.tickets_given -= 1
        self.avail_spaces += 1
    

    def payment(self):
        self.payed_amount = int(input("Type the amount you are paying: "))
        if self.payed_amount == self.total_price:
            print("Thank for your payment. Have a nice day. ")
        elif self.payed_amount >= self.total_price:
            tip_amount = self.payed_amount - self.total_price
            print(f"Thank you for your ${tip_amount: .2f} tip. ")
        else:
            amount_owed = self.total_price - self.payed_amount
            print(f"Sorry that is the wrong amount. You cannot leave the garage. You still owe ${amount_owed: .2f}")

        self.payed_customers[self.customer] == self.payed_amount
        print(self.payed_customers)


class Employer(ParkingGarage):
    def __init__(self, payed_customers, payed_amount):
        super().__init__(payed_customers, payed_amount)
        self.employee = ''

    def current_employee(self):
        self.employee = input("What is employee's name? ")

    def change_employee(self):
        change = input("Who is replacing you? ")
        self.employee = change
        print(f"The new parking garage employee is {self.employee}. Be sure to thank them!")

    def total_income(self):
        print(self.payed_customers)
        print(sum(self.payed_customers.values()))


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
        main_garage = Employer(20, 20)
        

        response = input("Are you an employee or a customer or neither? 'E' for employee or 'C' for customer or 'q' to quit")
        while True:
            if response.lower() == 'e':
                while True:
                    response3 = input("Would you like to check employee name, change employee, total income for the day or quit? Enter 'name' for employee name, 'change' to change employee, 'income' for total Income, or 'quit' to quit. ")            
                    if response3.lower() == 'name':
                        main_garage.current_employee()
                    elif response3.lower() == 'change':
                        main_garage.change_employee()
                    elif response3.lower() == 'income':
                        main_garage.total_income()
                    elif response3.lower() == 'quit':
                        break
                    else:
                        print("Invalid response, try again")

            elif response.lower() == 'c':
                while True:
                    response1 = input(f"Hello, would you like to park your car or leave the parking lot? P for Park or L for Leave or Q to quit ")
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
                break
            else:
                print("Invalid response. Try aqain. ")


main_garage = Main
main_garage.run()




