# store inventory update
store = {}
items = ["Bags", "Book", "Pen", "Erazer"]

# Avaliable quantities
quantities = [500, 450, 300, 250]
print("The following are the available items: ")
store = {items[0]: quantities[0], items[1]: quantities[1], items[2]: quantities[2],
items[3]: quantities[3]}
before_store = {item: quantity for item, quantity in store.items()}
print(store)

# ASk the user to input the item they want to buy
item_needed = input("\nEnter the item you want: ")
quant_needed = int(input("Enter the quantity you want to purchase: "))

# use the assignment operator (-=) to update (reduce) the item quantity in the dictionary
store[item_needed] -= quant_needed
print(store)

#print the updated dictionary
print(f"Before purchase: {before_store}")
print(f"After purchase: {store}")