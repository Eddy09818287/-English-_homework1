# Counter for the number of operations performed
i = 0
# Initial balance in the account
balance = 1000
# Format the initial balance with commas and two decimals
initial_balance = f"{balance:,.2f}"
# Ask the user how many transactions they want to perform
number_operations = int(input("Enter the number of transactions: "))
# Loop that runs while the number of operations is not exceeded
while i < number_operations:    
    # Display menu options
    print("Menu:")
    print("1 -> Check balance")
    print("2 -> Withdraw money")
    print("3 -> Deposit money")
    print("0 -> Exit")
    # Ask the user to choose an operation
    operation = int(input("Choose an option: "))
    # Option 1: Show current balance
    if operation == 1:
        print(f"Your balance is: {balance}")
    # Option 2: Withdraw money
    elif operation == 2:
        while True:
            withdrawal_amount = float(input("Enter your withdrawal amount: "))
            # Check if withdrawal is greater than available balance
            if withdrawal_amount > balance:
                print("Insufficient funds")
            # Check if the value entered is negative
            elif withdrawal_amount < 0:
                print("Error, enter a correct value.")
            # Valid withdrawal
            elif withdrawal_amount > 0 and withdrawal_amount <= balance:
                print(f"Your current balance is: {balance - withdrawal_amount}")
                break
    # Option 3: Deposit money
    elif operation == 3:
        while True:
            amount_to_deposit = float(input("Enter your deposit amount: "))
            # Validate that the amount is not negative
            if amount_to_deposit < 0:
                print("Error, please enter a correct value")
            # Valid deposit
            elif amount_to_deposit > 0:
                print(f"Your current balance is: {balance + amount_to_deposit}")
                break
    # Option 0: Exit the program
    if operation == 0:
        print("Thank you for using our cashier")
        break
    # Increase the operation counter
    i += 1