# tuple operations
# create a tuple of five Nigerian states entered by the user
states = tuple(input(f"Enter state {i+1}: ") for i in range(5)) 
print("First state:", states[0])
print("Last states:", states[-1])
if "lagos" in states:
    print("Yes")
else:
    print("No")
print("Number of states entered:", len(states))