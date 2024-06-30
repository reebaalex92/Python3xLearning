class BankAccount:
    def __init__(self):
        self.balance = 0
        __private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print(f"Balance: {self.balance}")

    def you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("You are not authorized to view the balance.")

    def you_are_auth2(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("You are not authorized to withdraw.")


jp_chase = BankAccount()
jp_chase.deposit(100)
secret_code = input("Enter the secret code to see balance: ")
if secret_code == "1234":
    jp_chase.you_are_auth(True)
else:
    jp_chase.you_are_auth(False)

secret_code = input("Enter the secret code to withdraw: ")
your_amount = int(input("Enter the amount to withdraw: "))
if secret_code == "1234":
    jp_chase.you_are_auth2(True, amount=your_amount)
    jp_chase.you_are_auth(True)
else:
    jp_chase.you_are_auth2(False)
