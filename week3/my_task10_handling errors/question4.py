while True:
    try:
        url = input("Enter a URL: ").strip()
        # Control flow check for "https://"
        if url.startswith("https://"):
            print("\nWelcome! Valid URL.")
            break
        else:
            print("Incorrect URL! Must start with 'https://'\n")
    except KeyboardInterrupt:
        print("\n\n:warning: Program interrupted by user .")
        break
    except EOFError:
        print("\n\n:warning: Input stream closed unexpectedly .")
        break
    except Exception as e:
        print(f"\n:x: Unexpected error occurred: {e}")
        break