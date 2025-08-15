#simulate a football match ticket system
seats = set(range(1, 51))

while seats:
    print("\nAvailable seats:",  sorted(seats))
    try:
        choice = int(input("Enter seat number to book (or 0 to stop): "))
        if choice == 0:
            break
        if choice in seats:
            seats.remove(choice)
            print(f"seat {choice} booked successfully!")
        else:
            print(f"seat not available.")
    except ValueError:
            print("please enter a valid number.")