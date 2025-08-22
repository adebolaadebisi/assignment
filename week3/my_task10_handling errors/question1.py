# Handling errors

print("Welcome to Adebola global service!")
print("\nPlease choose your option:")
print("1. Recharge")
print("2. Data")
print("3. Exit")
try:
    option = int(input("Enter option: "))  
except ValueError:
    print("Invalid input! Please enter a number (1, 2, or 3).")
    exit()  
if option == 1:
    print("\nYou selected Recharge :credit_card:")
    print("Available amounts: 100, 200, 300, 400, 500, 1000")
    try:
        amount = int(input("Enter amount: "))
    except ValueError:
        print(":x: Invalid input! Please enter a number only.")
        exit()
    if amount in [500, 1000, 1500, 2000, 2500, 3000]:
        print(f"You have successfully purchased ₦{amount} recharge card.")
    else:
        print(":x: Invalid amount. Please choose from the listed options.")
elif option == 2:
    print("\nYou selected Data :signal_strength:")
    print("Available plans:")
    print("1. 500MB - ₦500")
    print("2. 1.5GB - ₦1000")
    print("3. 3GB - ₦1500")
    print("4. 10GB - ₦2000")
    try:
        data_plan = int(input("Enter plan number: "))
    except ValueError:
        print("Invalid input! Please enter a number only.")
        exit()
    if data_plan == 1:
        print("You have successfully purchased 500MB for ₦100.")
    elif data_plan == 2:
        print("You have successfully purchased 1.5GB for ₦500.")
    elif data_plan == 3:
        print("you have successfully purchased 3GB for ₦1000.")
    elif data_plan == 4:
        print("You have successfully purchased 10GB for ₦2500.")
    else:
        print("Invalid plan selected.")
elif option == 3:
    print("\nThank you for using Adebola Network Service. Goodbye!")
else:
    print("Invalid option! Please select 1, 2, or 3.")









