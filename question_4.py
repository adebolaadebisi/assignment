#tuple unpacking
profile = (
    input("Enter your first_ name: "),
    int(input("Enter your age: ")),
    input("Enter your favorite color: "),
    input("Enter your hometown: ")
)
first_name, age, color, hometown =profile
print(F"{first_name} \n {age} \n {color} \n {hometown}")
