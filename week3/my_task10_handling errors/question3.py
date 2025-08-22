while True:  # retry loop
    print("\n\t=== Enter 5 Fruits ===")
    # Store fruits in a set
    fruits = set()
    try:
        # Collect 5 fruits
        for i in range(1, 6):
            fruit = input(f"{i}. ").strip()
            # Control flow to check duplicates and empty input
            if fruit == "":
                print("You didn't enter anything!")
            elif fruit.isdigit():
                print("Numbers are not valid fruits!")
            elif fruit in fruits:
                print(f":warning: Warning: {fruit} already exists, try another one!")
            else:
                fruits.add(fruit)
    except (KeyboardInterrupt, EOFError):
        print("\n\n:warning: Input was interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # Final output (always runs)
        if len(fruits) == 0:
            print("\nYou didn't enter any valid fruit.")
        elif len(fruits) < 5:
            print(f"\nYou entered only {len(fruits)} unique fruits.")
        else:
            print("\nYou entered 5 unique fruits!")
        print("\nList of fruits: ", ", ".join(fruits) if fruits else "None")
        # Ask if user wants to retry
        retry = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if retry not in ("yes", "y"):
            print("\nGoodbye! Thanks for using Fruit Collector.")
            break
