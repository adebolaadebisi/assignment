# python Dictionaries
# A dictionary in python is a collection of key-value pairs.
# key are unique and used to store and retrieve values.

# creating dictionaries
# using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)

# Empty dictionary
empty_dict = {}
print(empty_dict)

# Dictionary comprehension
# Syntax
#{Key_expression: Value_expression for item in iterable if condition}
# create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1,6)}
print(squares)

# with condition
# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1,10) if x % 2 == 0}
print(evens_cube)

# From Existing Dictionary
students = {"Ada":  85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score>= 50}
print(passed_students)

# using string keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Accessing Dictionary items
# define a dictionary
student = {"name": "Ada", "age": 20, "course": "computer science"}

# using get() method (avoid error if key is missing)
print(student.get("age"))
print(student.get("grade","Not found"))

# modifying dictionaries
student["age"] = 21 # change value
student["grade"]= "A"# Add new key -value pair print(student)
#Removing items from dictionaries
# using pop()
student.pop("grade")
#using popitem() - removes last inserted key-value
student.popitem()
# using del keyword
del student["age"]
# using clear() - remove all items
student.clear()
print(student)

#dictionary method
# dot keys(), dot values(), dot items(), dot updated
person = {"name": "Emeka", "age": 30}
# 1. keys()
print(person.keys())

# 2. values()
print(person.values())

#3. items()
print(person.items())

#4. update()
# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)

# nested dictionaries
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])  # Access nested data

# looping through dictionaries
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# Loop through keys
for key in student:
    print(key)

    #loop through values
    for value in student.values():
        print(value)

        # loop through key-value pairs
        for key, value in student.items():
            print(f"{key}: {value}")

            # storing a student's biodata


student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")

# final thought
# storing a student's biodata
student={"name":"Chinedu","age":19,"department":"Engineering","Subject":["Maths","Physics","Chemistry"],"is_full_time":True}
print(f"Name:{student['name']}")
print(f"Subject:{','.join(student['Subject'])}")

# how to add key-value pairs to an empty dictionary
# create an empty dictionary
student = {}

# Add key -value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"
print(student)

#list of dictionaries-each student has their own dictionary
students = { "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

#dictionary of dictionaries each students is keyed by their ID

students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}
# dictionary of list subject store a list of score
print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1])  


