# control flow in  python
# contol flow refers to the order in which statements are excuted in a program. 
# instead of always running line by line , control flow allows your program to:
#   - make decisions(choose one path or another, explore alternatives)- Control flow refers to the order in which statements are executed in a program.
# Instead of always running line by line, control flow allows your program to:

#     - Make decisions (choose one path or another, explore alternatives).

#     - Repeat actions (loops).

#     - Exit or skip parts of code.

#    - It is the foundation for logic and problem solving in programming.
#     - Control flow is divided into 3 parts

#A. Conditional Statements**

# 1. if Statement

# Executes a block only when a condition is true.
# c

#  - some usecases.
#  - validting login attempts.
#  - ensuring a minimum purchase requirement, etc.

# 2. if-else statement
# - provides two alternative paths.
# wallet = 400
# price = 500
# if wallet >= price:
#    print("Purchase successful")
# else:
#    print("Insufficient balance")

   # some usecases
   # - deciding success or failure of a payment.
   # - granting or denying access to a system
   # - determining pass/fail in an exam, etc.

   # 3. if -elif-else statement
   # - used for multiple conditions.
#    score = 85
#    if  score >= 70:
#       print("Grade A")
#    elif score >= 50:
#         print("Grade B")
#    else:
#         print("Grade C") 

# some usecases
# student grading systems.
# Assigning ticket categories(VIP, Regular, Student).
#  categorizing temperature (Hot, Warm< Cold) e.t.c

# 4. Nested if
# placing an if inside another if.
# age = 19
# citizen = True

# if  age >= 18:
#     if  citizen:
#         print("You can  vote")
#     else:
#         print("You must be a citizen to vote")   
# else:
#     print("Too young to vote")         
   
# some usecases
# voting eligibility(age + citizenship).
# Banking (account active + balance sufficient).
# school admission (age+ gradelevel).

# B. Loops
# 1. for loop
# this  is used for iterating over a sequence (strings, list, tuple, dictionary)
# Iterates through each elements in a list.
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")
# some usecases
# Iterating through shopping lists.
#  checking availability of products.
# displaying student names, etc.

# Iterates through each element in a tuple. this works like lists, but remember that tuples are immutable.
# coordinates = (0.34654, -0.48585, 0.57477) 
# for point in coordinates:
#     print(f"point: {point}")
# some usecases
# storing fixed sensor readings
# displaying fixed seating postions, etc.    

# Iterates through each other each element in a dictionary. remeber that dictionaries have key-value pairs.
# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")
#     some usecases
#     readinmg database records.
#     showing user profile details.
#     checking configuration settings, etc.

# Iterates through each element in a sting. remeber that strings are sequences of characters.
# word = "PYTHON"
# for char in word:
#     print(char) 
#     some usecases
#     counting vowels/consonants.
#     password validation (checking digits/special chars).char
#     text analysis, etc.


#2. While loop
# A while loop is used to repeatedly execute a block of code as long as a given condition is true.
# unlike the for loop (which iterates over sequences like lists, tuples, etc.)the while loop is condition-based.
# while condition:
# code block
# the condition must evaluate to true or the loop to continue running.
#when the condition becomes false, the loop stops.

# using while loop
# documenting my thoughts#
# let the loop start with count = 1
# let it keep printing until count is greater than 5
# let the loop terminates when the condition is no longer true

# my code
# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

# # Incrementing with 'while'
# num = 1
# while num <= 10:
#    print(num, end=" ")
# num += 1

# # decrementing with 'while'

# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -= 1

# while with user input
# keep asking until the user enters a correct password.

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")
# print("Access Granted!")    

# understanding while true
# the while true: loop - it keepes running forever until you explicitly stop it with a break statement or by exiting the program.
# it is commonly used when:
# you dont know in advance how many times you want the loop to run.
# you want to keep asking the user for input until a valid condition is met.
# you are building continuous programs like menus, login systems, or simulations.
# while true:
# code block
# must include a break statement to stop

# keep asking the user for a name until they type "exit"
# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")
    # ---> I used 'break' here. if you dont know what it is or what it is doing, its ok. i will explain it next ...
  # useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.  

# loop control statements (break, continue and pass)
# these keywords help us control the behavior of loops (for and while). instead of loops always running all iterations, we can skip steps, stop early,or do nothing intentionally.
# 1. break
# stops loop immediately. it is used if a condition is met and there's no need to continue looping.

# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)
#The loop stops completely when num ==5.
# stop searching when an item is found.
# exit when user input matches a condition
#prevent unnecessary iterations

#2 . continue
# skips the current iteration and moves to the next one. it is used if you want to ignore some values but keep the loop running.
#for num in range(1, 6):
#    if num == 3:
 #       continue
  #  print(num)

# 3 is skipped, but the loop continues.

## Some usecases

#Skip invalid data.

#Ignore unwanted characters (like spaces in a string).

#Continue running but avoid certain cases, etc.

# 3. pass
# does nothing a placeholder to avoid errors . it is used if you havent written the code yet but want to keep the structure.
for num in range(1, 6):
    if num == 3:
        pass   # do nothing for now
    else:
        print(num)

# At num == 3, Python executes pass (nothing happens).

## Some usecases

# Writing code structure (to fill in later).

# Placeholders in class/method definitions.

# Temporarily disable parts of code.

# let try while true again
# Try and think through this...

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

        # try and use while true for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

        # let make a guess
        secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")

        # do you remember this?
        balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


