# Day 4 Challenge: Phonebook Application

# Initialize an empty dictionary for the phonebook
phonebook = {}

# Define function to add a contact
def add_contact(name, number):
    phonebook[name] = number

# Define function to remove a contact
def remove_contact(name):
    if name in phonebook:
        del phonebook[name]

# Define function to look up a contact
def lookup_contact(name):
    return phonebook.get(name, "Contact not found")

# Start a loop for user interaction
while True:
    command = input("Enter a command (add, remove, lookup, or quit): ")
    if command == "quit":
        break
    elif command == "add":
        name = input("Enter the contact name: ")
        number = input("Enter the contact number: ")
        add_contact(name, number)
    elif command == "remove":
        name = input("Enter the contact name: ")
        remove_contact(name)
    elif command == "lookup":
        name = input("Enter the contact name: ")
        print(lookup_contact(name))
