class Checkbook:
    """
    A simple checkbook simulate a checking account with operations.

    Attributes:
    - balance (float): The current balance of the account. Initially set to 0.0.

    Methods:
    - deposit(amount): Deposits amount into the account and prints the updated balance.
    - withdraw(amount): Withdraws amount from the account if sufficient funds are available. 
    Prints an error message if there are insufficient funds.
    - get_balance(): Displays the current balance of the account.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the given amount into the checkbook.
        Args:
        - amount (float): The amount to deposit into the checkbook.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the given amount from the checkbook if sufficient funds are available.
        If there are insufficient funds, an error message is printed.
        Args:
        - amount (float): The amount to withdraw from the checkbook.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
    def get_balance(self):
        """
        Displays the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function that runs a simple interactive checkbook program.
    The user can perform the following actions:
    - Deposit money into the account
    - Withdraw money from the account
    - Check the current balance
    - Exit the program
    """
    cb = Checkbook()  # Create a new Checkbook instance

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        # Handle the exit case
        if action.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Handle the deposit case
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Deposit amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit.")

        # Handle the withdraw case
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Withdrawal amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal.")

        # Handle the balance case
        elif action.lower() == 'balance':
            cb.get_balance()

        # Handle invalid commands
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
