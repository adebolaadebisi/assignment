# 3: Create a Unique Voters Registration System
# Ask for voter names and store in a set.
print("\nList of Eligibile Voters.")
voter_1 = input("Enter your name: ")
voter_2 = input("Enter your name: ")
voter_3 = input("Enter your name: ")
voter_4 = input("Enter your name: ")
voter_5 = input("Enter your name: ")
# Store voters names in a set.
voters = set()
# If a voter tries to register twice, display a warning.
for voter in [voter_1, voter_2, voter_3, voter_4, voter_5]:
    if voter in voters:
        print(f"\nWarning!!!: {voter} has already registered.")
    else:
        voters.add(voter)
# After registration, display the total number of unique voters.
print("\nTotal number of unique voters: ", len(voters))
print("Voters list:", ", " .join(voters))