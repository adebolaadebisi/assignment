#task4
# unique members registration
names = input('Enter 3 names separated by comma here: ')
names_set = set(names.split(','))
names_dict = {name: len(name) for name in names_set}
print(names_dict)