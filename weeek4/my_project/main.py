# main.py
# Import the whole package
# import my_package

# print(my_package.add(5, 3))           # 8
# print(my_package.subtract(10, 4))     # 6
# print(my_package.capitalize_text("python"))  # Python

# # OR import specific modules
# from my_package import string_utils

# print(string_utils.reverse_text("hello"))  # olleh

# **What is Code Reusability?**

# - Code reusability means writing code once and using it multiple times instead of rewriting it.

# - It helps make programs cleaner, faster to develop, and easier to maintain.

# - In Python, code reusability is achieved using;

#     - Functions (reusing blocks of code)

#     - Modules (saving functions in .py files to import later)

#     - Packages (organizing modules in folders)

#     - Classes & Objects (OOP makes reusable blueprints)

#     - Libraries (built-in or third-party)


# 🔹 Why Reuse Code?

#     - Saves time – no need to rewrite the same logic.

#     - Avoids duplication – reduces errors from copy and paste.

#     - Improves readability – your code is modular and organized.

#     - Easy to maintain – update once, reuse everywhere.
#6 Organizing a python project
# - A modular project is a way of organizing your code into separate files and folders, each responsible for a specific task.

# - This makes the project easier to read, test, and maintain.

# **Why Use Modular Structure?**

# - Separates concerns – Each file has one responsibility.

# - Easier to debug – You can fix issues in one place without breaking others.

# - Reusability – Functions/modules can be reused in other projects.

# - Collaboration-friendly – Multiple developers can work on different parts.

# **Folder & File Structure**

# - Let’s say we want to build a Student Records Project.
# - We will first structure our folder and files like this.


# student_project/
# │
# ├── data.py        # Handles storing and retrieving student data
# ├── utils.py       # Contains helper functions (e.g., calculations, formatting)
# ├── main.py        # Entry point to run the project


# data.py

# students = []

# def add_student(name, track):
#     students.append({"name": name, "track": track})

# def get_students():
#     return students

# # utils.py

# def format_student(student):
#     return f"{student['name']} is learning {student['track']} at NCC Digital Industrial Park, Abeokuta."

# main.py → Project entry point

# main.py

# import data
# import utils

# # Add some students
# data.add_student("Paul", "AI Engineering")
# data.add_student("Blessing", "AI Development")

# # Print formatted student records
# for s in data.get_students():
#     print(utils.format_student(s))

#     ```
# student_project/
# │
# ├── data/                 # Data-related files
# │   ├── __init__.py
# │   └── data.py
# │
# ├── utils/                # Helper functions
# │   ├── __init__.py
# │   └── utils.py
# │
# ├── main.py               # Entry point
# └── requirements.txt      # List of dependencies (if any)
# **Lets work on Library Management System**

# - The goal of this project is to
#  - Manage books in a library
#  - Add books, list books, and borrow books.
#  - Organized into folders and files for modularity.**Lets structure the folder and possible files**

#lets structure the folder and possible files

# library_project/
# │
# ├── data/                   # Handles storage & retrieval
# │   ├── __init__.py
# │   └── data.py
# │
# ├── utils/                  # Helper functions
# │   ├── __init__.py
# │   └── helpers.py
# │
# ├── services/               # Core business logic
# │   ├── __init__.py
# │   └── library.py
# │
# ├── main.py                 # Entry point of the program
# └── requirements.txt        # (optional) external dependencies

# let implement the project
# data/data.py - This will handle data storage

# books = []

# def add_book(title, author):
#     books.append({"title": title, "author": author, "available": True})

# def get_books():
#     return books

# #utils/helpers.py - This will handle helper functions
# def format_book(book):
#     status = "Available" if book["available"] else "Borrowed"
#     return f"{book['title']} by {book['author']} - {status}"

# # service/libary.py -This will handle business logic
# import my_data as data

# def borrow_book(title):
#     for book in data.get_books():
#         if book["title"].lower() == title.lower() and book["available"]:
#             book["available"] = False
#             return f"You have borrowed '{book['title']}'"
#     return "Book not available."

# # main.py - This will be our project entry point


# from data import data
# from utils import helpers
# from services import library

# # Add some books
# data.add_book("Python Basics", "John Doe")
# data.add_book("Advanced Python", "Jane Smith")

# # Display all books
# print("Library Collection:")
# for b in data.get_books():
#     print(helpers.format_book(b))

# # Borrow a book
# print("\nBorrowing a book:")
# print(library.borrow_book("Python Basics"))

# # Display books again
# print("\nUpdated Library Collection:")
# for b in data.get_books():
#     print(helpers.format_book(b))

# lets make the scope of the implementation broader and interactive**

# - Lets have our project structure

# ```
# library_project/
# │
# ├── data/
# │   └── data.py
# │
# ├── utils/
# │   └── helpers.py
# │
# ├── services/
# │   └── library.py
# │
# └── main.py
# lets implement it






