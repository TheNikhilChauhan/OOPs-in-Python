class App():
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username

    def login(self):
        if self.username == "owner" and self.users >= 1:
            print("Welcome ", self.username)
            print("Your storage is ", self.storage)
        else:
            print("Login is denied")
    
    def increase_capacity(self, number):
        self.storage += number
        print("Updated storage ", self.storage)

    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amt = int(input("Upgrade Amount: "))
            self.storage += upgrade_amt
        else:
            print("You still have: ", (self.storage - self.users), "spaces open")

product_one = App(35, 256, "owner")
product_one.login()
product_one.increase_capacity(50)
print()

product_two = App(35, 256, "nik")
product_two.login()
product_two.check_upgrade()