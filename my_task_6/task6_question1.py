# task1
#Ask the user to enter five favorite fruits and store them in a set and display the set
fruits = set()
for i in range (5):
    fruit = input(f"Enter fruit {i+1}:")
    fruits.add(fruit)
    print("Your favorite fruits are:", fruits)