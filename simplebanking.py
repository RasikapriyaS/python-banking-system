class bankaccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed! Amount is higher than account balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def display(self):
        print(f"Account Holder: {self.name}, Account No: {self.account_number}, Balance: {self.balance}")


def main():
    print("== Welcome to Simple Banking System ==")
    accounts = {}

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")

            if acc_no in accounts:
                print("Account already exists!")
            else:
                accounts[acc_no] = bankaccount(acc_no, name, 0)
                print("Account created successfully!")

        elif choice == '2':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter amount: "))
                accounts[acc_no].deposit(amount)
            else:
                print("Account not found!")

        elif choice == '3':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter amount: "))
                accounts[acc_no].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == '4':
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                accounts[acc_no].display()
            else:
                print("Account not found!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
