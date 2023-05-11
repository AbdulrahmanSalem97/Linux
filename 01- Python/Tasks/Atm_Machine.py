#dictionary inside dictionary to connet all user data 
Accounts_Data ={
        'Ahmed': {'balance': 5000, 'pin': '1111'},
        'Salem': {'balance': 3500, 'pin': '2222'},
        'Mohamed':  {'balance': 2000, 'pin': '3333'},
        'Abdulrahman':{'balance': 50000, 'pin': '4444'}}

#Super Loop For Program
while True:
    print("\nWelcome to ITI Banking!")
    name = input("Please Enter Account name: ")
    if name not in Accounts_Data:
        print("Invalid Account Name! Please try again!")
        continue

    pin = input("Enter PIN: ")
    if pin != Accounts_Data[name]['pin']:
        print("Invalid PIN!!! Please try again.")
        continue

    print("Welcome To Your Acccount")
    print("--------------------------------------------------------------------------")
   
    #Super loop after Login to remain in options 
    while True:
        print("\n1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Logout")

        #Taking choise from user
        choice = int(input("Enter your choice (1->4): "))

        #options directory
         
        #Checking Balance
        if choice == 1:
            print(f"Account balance for {name}: {Accounts_Data[name]['balance']}")

        #Withdraw
        elif choice == 2:
            amount = int(input("Please Enter the amount: "))
            if amount > Accounts_Data[name]['balance']:
                print("Sorry your balance Can't Cover")
            else:
                Accounts_Data[name]['balance'] -= amount
                print(f"Withdrawa successful Get Money! New balance for {name}: {Accounts_Data[name]['balance']}")

        #DePosit
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            Accounts_Data[name]['balance'] += amount
            print(f"Deposit successful! Your new balance {name}: {Accounts_Data[name]['balance']}")

        #loging out
        elif choice == 4:
            print("Thank Your for Banking with us")
            break

        else:
            print("Invalid choice")
    break

 

