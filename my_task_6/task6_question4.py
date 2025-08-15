# register unique voters
voters = set()
while True:
    name = input("Enter voter name (or 'done' to finish):")
    if name.lower() == "done":
        break
    if name in voters:
        print("* This voter is already registered!")
    else:
        voters.add(name)
        print(f"{name} registered successfully.")
        print("\nTotal unique voters:", len(voters))