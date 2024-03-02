# Guest Management and Loyalty Programs

# Description
'''
This code represents a guest management system with a loyalty program.
It allows you to input information about guests, such as their names, ranks and ages.
The system provides various functionalities to retireve guest information, track loyalty points and calculate average guest age.
'''

class Guest:
    def __init__(self, first_name, last_name, rank, age):
        self.first_name = first_name
        self.last_name = last_name
        self.rank = int(rank)
        self.age = int(age)

    def guest_info(self, all_guests):
        for guest in all_guests:
            print(f"The guest name is: {guest.first_name} {guest.last_name} and the age is: {guest.age}")

    def loyalty_program(self, all_guests):
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print("Gold members:")
            for member in gold_members:
                print("\tGuest: ", member)
        
    def guest_avg(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        ave_age = total_age / len(all_guests)
        print("Average customer age: ",ave_age)


all_guests = list()
num_guests = int(input("Enter a number of guests: "))
for i in range(num_guests):
    data = input("First Name/ Last Name/ Rank/ Age: ").split("/")
    guest = Guest(data[0], data[1], data[2], data[3])
    all_guests.append(guest)

guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)

