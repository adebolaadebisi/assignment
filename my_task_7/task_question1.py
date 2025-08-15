# task1
student_data ={}

# collect details
student_data["name"] = input("Enter your name: ")
student_data["age"]  = int(input("Enter your age: "))
student_data["gender"] = input("Enter your gender: ")
courses = input("Enter your courses separated by commas: ").split(",")
student_data["courses"] = [courses.strip() for courses in courses]
# display neatly
print("\n--- Student Bio Data ---")
print(f"Name:\t\t{student_data['name']}")
print(f"Age:\t\t{student_data['age']}")
print(f"Gender:\t\t{student_data['gender']}")
print("Courses:\t" +", ".join(student_data['courses']))