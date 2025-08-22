# 4: Fruit Collector (with control flow)
print("\n\t=== Enter 5 Fruits ===")
# Store fruits in a set
fruits = set()
# Collect 5 fruits
for i in range(1, 6):
    fruit = input(f"{i}. ")
    # Control flow to check duplicates
    if fruit in fruits:
        print(f":warning: Warning: {fruit} already exists, try another one!")
    elif fruit == "":
        print(":x: You didn't enter anything!")
    else:
        fruits.add(fruit)
# Final output
if len(fruits) == 0:
    print("\nYou didn't enter any valid fruit.")
elif len(fruits) < 5:
    print(f"\nYou entered only {len(fruits)} unique fruits.")
else:
    print("\nYou entered 5 unique fruits!")
print("\nList of fruits: ", ", ".join(fruits))