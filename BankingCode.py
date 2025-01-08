# Bank Account Class
class Bank_Account:
    def __init__(self):
        self.Balance = 0
        print("Welcome to FOSS Bank")

# Deposit Amount
    def Deposit(self):
        Amount=float(input("Enter Amount To Be Deposited: "))
        self.Balance += Amount
        print("\n Amount Deposited: ", Amount)

# Withdraw Amount
    def Withdraw(self):
        Amount = float(input("Enter Amount To Be Withdrawn: "))
        if self.Balance >= Amount:
            self.Balance -= Amount
            print("\n Withdrew Amount: ", Amount)
        else:
            print("\n Insufficient Balance, Try Lower Amount")

# Display Amount
    def display(self):
            print("\n Net Avaiable Balance: ", self.Balance)


Bank = Bank_Account()

Bank.Deposit()
Bank.Withdraw()
Bank.display()
