# unique name collecter
names =set()
while True:
    name = input("Enter a name (or 'done' to finish): ")
    if name.lower() == "done":
       break
    names.add(name)
    print("unique names in alphabetical order:")
    for name in sorted(names):
        print(name)