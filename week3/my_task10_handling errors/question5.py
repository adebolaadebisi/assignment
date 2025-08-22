print("\n:ballot_box_with_ballot: List of Eligible Voters.")
# Store voters names in a set
voters = set()
try:
    for i in range(1, 6):
        voter = input(f"Enter voter {i} name: ").strip()
        # Error handling for empty input
        if voter == "":
            print("You didn't enter a name, skipping...")
            continue
        # Check for duplicates
        if voter in voters:
            print(f"\n:warning: Warning: {voter} has already registered!")
        else:
            voters.add(voter)
except KeyboardInterrupt:
    print("\n\n:warning: Registration interrupted by user.")
except EOFError:
    print("\n\n:warning: Input ended unexpectedly.")
except Exception as e:
    print(f"\nUnexpected error: {e}")
finally:
    # Display final voter list no matter what
    print("\n:memo: Registration Summary:")
    print("Total number of unique voters:", len(voters))
    print("Voters list:", ", ".join(voters) if voters else "None")