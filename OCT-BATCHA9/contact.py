# Create an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact added!")

# Function to display contacts
def show_contacts():
    if not contacts:
        print("No contacts in the book.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print()
            # Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        info = contacts[name]
        print("Contact details:")
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
    else:
        print("Contact not found.")

# Function to remove a contact
def remove_contact():
    name = input("Enter the name to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been removed from contacts.")
    else:
        print("Contact not found.")

# Main loop for the contact book
while True:
    print("\nOptions:")
    print("1. Add a contact")
    print("2. Show contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        remove_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")