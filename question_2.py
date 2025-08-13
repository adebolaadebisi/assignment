# tuple and input
names = input("Enter your five best friends names:")
name_1 = input("Enter your first friends name: ")
name_2 = input("Enter your second friends name: ")
name_3 = input("Enter your third friends name: ")
name_4 = input("Enter your forth friends name: ")
name_5 = input("Enter your fifth friends name: ")
friends = (name_1, name_2, name_3, name_4, name_5)
print(friends[::-1])
