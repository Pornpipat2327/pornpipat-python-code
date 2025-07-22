# Complete this ATM simulation
#balance = 1000
#pin = "1234"

#entered_pin = input("Enter PIN: ")
#if entered_pin == pin:
    #print("PIN accepted")
    #while True:
        #print("\n1. Check Balance")
        #print("2. Withdraw")
        #print("3. Deposit") 
        #print("4. Exit")
        
        #choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
balance = 1000
pin = "6730202327"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")

        if choice == "1":
            print(f"Your balance is: ${balance}")
        
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance}")
            else:
                print("Insufficient balance.")
        
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Deposit successful. New balance: ${balance}")
            else:
                print("Invalid amount.")
        
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break

        else: 
            print("Please select 1-4 ONLY!!!")       
else:
    print("Invalid PIN")
