# Check if a given string starts with "https://"
# Using the "if-else"  and "while True" statements.
url = input("Enter a URL: ")
if url.startswith("https://"):
    print("\nWelcome!")
else:
    print("Incorrect URL")
# OR
url = input("Enter a URL: ")
if (url[0:8]) == "https://":
    print("\nWelcome!")
else:
    print("\nIncorrect URL")
# OR
while True:
    url = input("Enter a URL: ")
    if url.lower() == "https://":
        print("\nWelcome!")
        break
    print("Incorrect URL!!!")