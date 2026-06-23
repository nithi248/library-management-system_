#ATM BANKING SYSTEM
login_pin=int(input("Enter your login pin: "))
store_the_pin_into_database=2412
if login_pin==store_the_pin_into_database:
    print("Access granted")
    print("Welcome to the ATM Banking System")
    Balance=10000
    minimum_balance=1000
    mini_statement_with_accurate_time_and_date=[]
    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Mini Statement")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Your current balance is: ", Balance)
        elif choice==2:
            withdraw_amount=int(input("Enter the amount to withdraw: "))
            if withdraw_amount>Balance:
                print("Insufficient balance.")
            elif Balance-withdraw_amount<minimum_balance:
                print("You cannot withdraw this amount as it will bring your balance below the minimum required balance of ", minimum_balance)
            else:
                Balance-=withdraw_amount
                mini_statement_with_accurate_time_and_date.append(("Withdrawal", withdraw_amount, Balance))
                print("Withdrawal successful. Your new balance is: ", Balance)  

        elif choice==3:
            deposit_amount=int(input("Enter the amount to deposit: "))
            Balance+=deposit_amount
            mini_statement_with_accurate_time_and_date.append(("Deposit", deposit_amount, Balance))
            print("Deposit successful. Your new balance is: ", Balance)
        elif choice==4:
            print("Mini Statement:")
            for transaction in mini_statement_with_accurate_time_and_date:
                print(f"{transaction[0]}: {transaction[1]} | Balance: {transaction[2]}")
        elif choice==5:
            print("Thank you for using the ATM Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")