# modularizing your code 1
#1. introduction to modularity
# what modular programming means
# why modularity is important (readability, reuseability, debugging,teamwork)
#what is modular programming ?
#modular programming is a way of writting programs by dividing them into smaller, independent, and reuseable parts(modules)instead of writting one long block of code
# a module can be a function, a class, or a python file(.py) that performs a specific task.
# these modules can then be combined to build a complete program.
# in simple words, modular programming = breaking big problems into smaller , manageable solutions.

# why modularity is important
#1. REABILITY 
# breaking code to smaller modules makes it easier to read and understand.
# instead of scrolling through hundrends of lines inside a file, you can just put them in different files within a folder and look at the specific file that has the codes you need.
#2. REUSABILITY
# once you create a module, you can reuse it in different programs.
# no need to rewrite the same code over and over again.
# for example , a function that calculates the area of a circle can be used in a school project, an engineering project, or even in a game.
#3. DEBUGGING AND MAINTENANCE
# if there's an error , you only need to check the specific module where the problem is, instead of combing through the whole program.
# updating or improving one module doesn't break the rest of the system.
# let say, you are building a banking application. if the payment module  in the app has a bug, the user login module is unaffected.
#4. TEAMWOK AND COLLABORATION
# in real -world projects, different developers can work on different modules simultaneously
# later, all modules are combined into the main project.
# for example , in building a school management system.
# one developer handles student records
# another handles teacher records 
# another handles payment system
# all parts are then combined to make one big system.

#**lets put things in perspective**
# imagine we are planning a wedding event. if one person tries to do everything(cook, decorate, handle invitations, music, photography), it becomes chaotic or nearly impossible.
#instead, tasks are divided:
# The caterer handles food
# The decorator handles decoration
# The DJ handles music
# The photographer handles pictures
# at the end, when everyone brings their contribution together, the event runs smootly.
# this is exactly how modular programming works in coding. each part (module) does its job, and together they form the complete program.
# *do you understand?*

#2. FUNCTIONS(FIRST LEVEL OF MODULARITY)
#definition of a function
# defining and calling functions
# function parameters and arguments
# return values
# use cases(math operations, repeated tasks, formattinmg output)

#DEfINITION OF A FUNCTION
# A function is a block of organized, reusable code that performs a single specific task. in python, we have the inbuilt functions, the user defined functions and lambda function(which is also a type of user defined function)
# PYTHON BUILT-IN FUNCTIONS
# built-in functions are functions that come pre-installed with python. you dont need to import any library to use them. They are always available ,just like how a phone comes with default apps
#(calculator, messages, clock). and you have used some of them without even knowing.
# common categories of built-in functions
# 1. input and output funtions
#print() # Displays output.
# input() #  takes user input.

#2. Type conversion functions
# int(), float(), str(), bool(), list(), dict(), tuple(), set()

#3 MATHEMATICAL FUNCTIONS
#abs() # absolute value
#pow(x, y) # x raised to power y
# round()  # round numbers to the defined decimal places
# min (), max() # find smallest/largest

#4. SEQUENCE AND COLLECTION FUNCTIONS
# len () # length of a sequence
# sum() # sum of elements
# sorted() # sort items
# enumerate() # Track index and value

# UTILITY FUNCTIONS
# TYPE () # SHOWS THE TYPE OF AN OBJECT(VARIABLES,DATATYPES, DATA STRUCTURES, FUNCTIONS,CLASSES)
# id() # Return unique ID of object in memory
# help() # Documentation about an object

# 6. SPECIAL BUILT-INS
# range() # generates a sequence of numbers
#zip() # combines two list element by element
# map() # applies a function to all elements in a sequence
# filter() # filters elements in a sequence based on condition

# see examples of use here

# range()
# for i in range(3):
#     print(i)   # 0, 1, 2

#zip()

# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# age =  [10, 11,13]
# for n, s, in zip(names, scores):
#     print(n, "scored", s)

# map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 ==0, nums))
# print(even_nums) # [2,4]

# student performance & feedback system

# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # step3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# #Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)
# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# step5:Ranking(using sorted and zip) 
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # step7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))

# # step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)
# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)

# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[10], line 5
#       1 # Student Performance & Feedback System
#       2 
#       3 # Step 1: Input student data
#       4 name1 = input("Enter first student name: ")
# ----> 5 score1 = int(input("Enter score for " + name1 + ": "))
#       7 name2 = input("Enter second student name: ")
#       8 score2 = int(input("Enter score for " + name2 + ": "))

# ValueError: invalid literal for int() with base 10: ''


#User defined function

# - Instead of writing the same code again and again, we put it inside a function and just call it whenever we need it.

#  - So functions make programs cleaner, shorter, and easier to manage.

# - Now, I need you to think of a function like a machine in a factory.

#   - You put something in (input),

#   - The machine works on it (process),

#   - Then gives you something out (output).
# in python, we use the def keyword to define a function . then we call the function whenever we want to use it
# let see the function structure
# def function_name(takes in input):
#process block
# output block
# more explanation
# def function_name(input - here, you will insert an item or list of what the function will need to work):
# "process block - here will contain the logic or what you want the function t5o do"
# "output - Then here will contain what you want the function to output. you can either use the 'return' keyword or 'print()' or 'yield'"''

# Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
# greet()
# greet()
# greet()

# function arguments and parameters
# Arguments are variables you add inside the function parenthesis when defining the function
#(placeholders). sometimes, they can be optional.
# parameters are the actual values you pass inside the function parenthesis when calling the function.

# Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# # Calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

#when to use return, print(), and yield keywords inside a function
# a. print()
# you can use it if you are just interested in displaying your output(not storing). it does not give back a value you can use later.
# think of it like shouting information out loud, but not recording it for reference purpose.
# so you use it when you just want to show results to the user. Example:printing menus, reports, or logs.
# def greet(name):
#     print("Hello", name)


# Function call
# result = greet("Esther")

# You will notice that it did not store the name
# print("Result:", result)

#B . return
# you can use it if you want to give back a value
# return sends a value back to the function caller
# the funtion ends immediately once it hits return
# think of it like filling a form and handling it back, the caller now owns the result and can reuse it.
# so you can use return when you need the result for futher computation or storage. for example, math calculation, data processing, formatting text.
# def add(a, b):
#     return a + b

# Function call

# result = add(4, 6)
# print("The sum is:", result)

# Note the output and compare it with that of print()

#3. Yield
# This is used for producing a sequence(generators)
# yield works like return, but instead of ending the function, it pauses it and remembers its state.
# next time you call it, it resumes from where it stopped
# this creates a generator
# you can use it when working with large data or infinite sequences.

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i   # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.
# more on function arguments(types of arguments)
# functions can accept different types of arguments depending on how we want to pass data
# understanding these makes functions flexible and powerful

# 1 Position Arguments
# These are the most common
# The order matters. values are assigned to parameters in the same order as they appear.
# Think of it like lining up children in the same order as roll call.
# def introduce(name, track):

#     print("My name is", name)
#     print("I am learning", track, ".")

# function call
#introduce("Ngozi",  "AI Engineering")   # Correct order

# Change the arrangment and watch the output

#introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error
#2. Keyword Arguments
# here, you explicitly mention the parameter name when calling the function
# order doesn't matter, since python knows which value goes where.
# Think of it like addressing an envelope by name instead of postion in line.

# function call
#introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output

#introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not batter

# 3. Default argument
# here, you can give parameters a default value.
# even if no value is provided when calling, the default is used
# think of it like a restaurant menu where rice is served by default if you don't choose otherwise
# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track".")

# function call
# Without specifying the default argument, but watch the ouput
#introduce("Paul")  
# Specify the default argument and watch the output

#introduce("Tunji Paul", track = "AI Development")
# 4. Varying length arguments
# sometimes we dont know how nmany arguments will be passed. python provides two special symbols(that is the asterist)
# single asterisk for non-keyword arguments or tuple(*args)
# double asterisk for keyword arguments or dictionary (**kwargs)

# a. non-keyword(tuple)
# collects extra positional arguments into a tuple
# think of it like packing extra clothes into a bag
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# function call 
# Take note of the output
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50)

#b. keyword argument(dictionary)
# collects extra keyword arguments into a dictionary.
# think of it like a labeled container where each item has a name tag.
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="Block Chain")

# lets implement on full code

# Define student profile function

# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

# def participant_profile(name, age, track="AI Development", *skills, **extra_info):
#     """
#     Generate a profile for a bootcamp participant using different types of arguments.
#     """
#     profile = f"\n--- Bootcamp Participant Profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"

#     # Skills (from *args)
#     if skills:
#         profile += "Skills: " + ", ".join(skills) + "\n"
#     else:
#         profile += "Skills: Not yet specified\n"

#     # Extra info (from **kwargs)
#     if extra_info:
#         profile += "Additional Info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"

#     return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places

# ---------- LEts test ----------

# Example 1: Using only positional arguments
#print(participant_profile("Peter", 24))
# Example 2: Adding keyword/default argument
#print(participant_profile("Ridwan", 29, track="AI Engineering"))
# Example 4: Adding variable-length keyword arguments (**kwargs)
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest="Blockchain", city="Shagamu", phone="08123456789"
# ))

# Namespaces and scope
# namespace
# A namespace is like a "container" that holds names (variables, function, object) and maps them to the actual data stored in memory.
# think of it as a dictionary where keys are names and values are objects.
# python uses namespaces to avoid name conflicts.
# lets imagine a company where different departments can have employees with the same name.
# in the IT department, there may be a "Chris".
# in the Training department, there may also be a "Chris".
# Both exist, but they are identified by their department (namespace), so thers"s no confusion.

# Types of Namespace
#1. Built-in namespace- Provided by python(e.g, len,print,list).
#2. Global namespace - Names defined at the top level of a script or module.
#3. Local namespace- Names created inside a function.
# Global Namespace
# employee = "General Employee"  

# def IT_department():
#     # Local Namespace inside IT_department
#     employee = "Chris (IT)"
#     print("Inside IT Department:", employee)

# def Training_department():
#     # Local Namespace inside Training_department
#     employee = "Chris (Training)"
#     print("Inside Training Department:", employee)

# print("In Global Namespace:", employee)  # Refers to global variable

# IT_department()   # Uses local variable in IT
# Training_department()   # Uses local variable in Training

# Using a built-in namespace function
#print("Length of 'Python':", len("Python"))  

# So 'Chris' can exist in more than one namespace without conflict.
# Please, take your time to study the output carefully.

# Scope
# scope defines where in the code a name is accessible. python follows the LEGB rule(order for a variable):
#L-Local- inside the current function
# E- Enclosing- inside any enclosing functions(s).
# G - Global - at the top level of the script/module
# B - built-in - python's built-in functions/objects.
# x = "global x"   # Global Namespace

# def outer():
#     x = "enclosing x"  # Enclosing Namespace
    
#     def inner():
#         x = "local x"  # Local Namespace
#         print("Inside inner:", x)  # Local wins
    
#     inner()
#     print("Inside outer:", x)  # Enclosing
    
# outer()
# print("In global:", x)  # Global

# Watch the output
# Notice how Python searches in the order Local → Enclosing → Global → Built-in (LEGB).
### Global keyword

# Used when you want to modify a global variable inside a function.

# x = 5

# def change_global():
#     global x
#     x = 10   # modifies the global x

# change_global()
# print(x)  # Output: 10

# # Watch the output
# nonlocal keyword

#Used in nested functions when you want to modify the variable from the enclosing scope (not global).

# def outer():
#     x = "outer x"
    
#     def inner():
#         nonlocal x
#         x = "changed by inner"
#         print("Inside inner:", x)
    
#     inner()
#     print("Inside outer:", x)

# outer()

# # Watch the output
#So understanding namespace and scope helps avoid name conflicts, makes modular code easier to read, and ensures functions and modules can work without interfering with each other.

#- A lambda function is a small, anonymous function (no name) defined using the lambda keyword.
#- It can have any number of arguments, but only one expression.
#- The result of the expression is automatically returned.

# this is the syntax
#lamba arguments: expression
# you use lambda"
# when you need a short, throwaway function(not reuseable)
# to aviod writting full def functions for small tasks
# used with functions like map (), filter(), sorted(), and reduce()
# Normal function
# def square(x):
#     return x ** 2

# # Lambda function
# square_lambda = lambda x: x ** 2

# print(square(5))         
# print(square_lambda(5))  

# Watch the output and note the difference
# This one has more that one arguments.

# add = lambda a, b: a + b
# print(add(3, 7))  # Output: 10
# Let us lambda to apply the square function to a list

# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)  # Output: [1, 4, 9, 16]# Lets use lambda to filter even numbers 

# numbers = [10, 15, 20, 25, 30]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Output: [10, 20, 30]
# Lets use lambda to sort the tuple within a list.

# students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# # Sort by age
# sorted_students = sorted(students, key=lambda student: student[1])
# print(sorted_students)

  
# # Output: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

# students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
# print(students_sorted_descending)

# # Output: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

# students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
# print(students_sorted_alphabetically)

# # Output: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]



