class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest {interest} added. Balance: {self.balance}")


acc = SavingsAccount("Umar", 1000)

while True:
    print("\n--- Bank System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Add Interest")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        acc.deposit(amount)
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        acc.withdraw(amount)
    elif choice == "3":
        print(acc)
    elif choice == "4":
        acc.add_interest()
    elif choice == "5":
        print("Exiting Bank System. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
