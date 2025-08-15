#Sets in python
# in python , a set is an unordered collection of unique elements. sets are useful when you want to store multiple items but avoid duplicates.
# creating sets
#1 using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

#2 using the set() construtor
numbers = set([1, 2, 3, 4])
print(numbers)

#3 creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

#4 from a string (duplicates remove automatically)
letters = set("mississippi")
print(letters)
#characteristics of sets
# set operations
 # adding elements
colors = {"red", "blue"}
colors.add("green")
print(colors)
 # Removing elements
colors.remove("blue")   # Removes an element, raises error if not four 
colors.discard("yellow") # Removes if found, no error if missing

 # pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)

# clear a set
colors.clear()
print(colors)

#mathematical set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#1 union
print(set1 | set2)
print(set1.union(set2))

#2 Intersection
print(set1 & set2)
print(set1.intersection(set2))

#3 difference
# 3. Difference
print(set1 - set2)
print(set1.difference(set2))

#4 symetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# collecting unique visitors to an event
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# Checking if a visitor attended
# (Dont worry if you can't figure this part out yet. We will discuss it properly later in the course.)

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")




