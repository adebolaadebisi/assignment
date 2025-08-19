# create an empty dictionary called student
student = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
scores = [70, 85, 90]
average_score = (scores[0] + scores[1] + scores[2]) / 3
passed = average_score >= 50
teenager = age > 13 and age < 19
student = {
    "name": name, 
    "age": age,
   "scores": scores, 
   "passed": passed
    }
print(student)
print(f"student record:\nName: {student['name']}\nAge: {student['age']}\nScores:{student['scores']}\nPassed: {student['passed']}\nTeenager: {teenager}")