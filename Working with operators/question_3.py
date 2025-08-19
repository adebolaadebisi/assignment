# online store cart calculation
# create a list of items
items = ["Book", "Pen", "Bag", "Erazer"]
prices = [600, 2000, 3000, 4000]
# start with an empty cart total (cart_total =0)
cart_total = 0

# use assignment operators (+=) to add  the price of some items into cart_total
cart_total += 600
cart_total += 2000
cart_total += 3000
cart_total += 4000

# print the list of items and the total price using an f-string
print(f"Items: {items}\nTotal price: #{cart_total}")