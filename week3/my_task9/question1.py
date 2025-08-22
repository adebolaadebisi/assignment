# Define variables with integers
# score = 20         # data types int
# name="adebola"     # data types string
# height = 1.83      # data types float
# print(f"{name} scored {score}  height {height} ")

#str()
#int ()
#flooat ()

#age  = int(input("Enter your age:"))
#print(f"you will be (age + 1) years old next year.")

# step1 create a bot welcome text
# USING :IF, ELSE and ELIF

print(" Welcome to Adebola global service!")
print("\nPlease choose your option:")
print("1. Recharge")
print("2. Data")
print("3. Exit")
option = input("Enter option: ")
if option == "1":
    print("\nYou selected Recharge :")
    print("Available amounts: 500, 1000, 1500, 2000, 2500, 3000")
    amount = input("Enter amount: ")
    if amount in ["500", "1000", "1500", "2000", "2500", "3000"]:
        print(f"You have successfully purchased ₦{amount} recharge card.")
    else:
        print("Invalid amount. Please choose from the listed options.")
elif option == "2":
    print("\nYou selected Data")
    print("Available plans:")
    print("1. 500MB - ₦100")
    print("2. 1.5GB - ₦500")
    print("3. 3GB - ₦1000")
    print("4. 10GB - ₦2500")
    data_plan = input("Enter plan number: ")
    if data_plan == "1":
        print("You have successfully purchased 500MB for ₦100.")
    elif data_plan == "2":
        print("You have successfully purchased 1.5GB for ₦500.")
    elif data_plan == "3":
        print("You have successfully purchased 3GB for ₦1000.")
    elif data_plan == "4":
        print("You have successfully purchased 10GB for ₦2500.")
    else:
        print("Invalid plan selected.")
elif option == "3":
    print("\nThank you for using Adebola Network Service. Goodbye!")
else:
    print("Invalid option! Please select 1, 2, or 3.")