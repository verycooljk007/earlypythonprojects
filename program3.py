# Display author/program information
print("Welcome to my program!")
print("Author: Meshaal M. Khan")
print("Program: Name Greeting")

# Request password from user
password = input("Enter password: ")

# Check if password is correct
if password == "hello":
    # Request user's name
    name = input("Enter your name: ")

    # Check if user's name matches author's name
    if name == "Meshaal":
        print("What a great name!")
    # Check if user's name is Madonna or Cher
    elif name == "Madonna" or name == "Cher":
        print("May I have your autograph, please?")
    # For all other names, print a generic greeting
    else:
        print(name + ", that's a nice name.")
else:
    print("Sorry, incorrect password. Goodbye!")
