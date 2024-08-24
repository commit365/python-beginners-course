# contact_book.py

import os

# Define the contact book file
contact_file = 'contacts.txt'

def add_contact(name, phone):
    """Add a new contact to the contact book."""
    with open(contact_file, 'a') as file:
        file.write(f"{name},{phone}\n")
    print(f"Contact '{name}' added.")

def view_contacts():
    """Display all contacts in the contact book."""
    if os.path.exists(contact_file):
        with open(contact_file, 'r') as file:
            print("Contacts:")
            for line in file:
                name, phone = line.strip().split(',')
                print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

def search_contact(name):
    """Search for a contact by name."""
    if os.path.exists(contact_file):
        with open(contact_file, 'r') as file:
            for line in file:
                contact_name, phone = line.strip().split(',')
                if contact_name.lower() == name.lower():
                    print(f"Found: Name: {contact_name}, Phone: {phone}")
                    return
    print("Contact not found.")

def main():
    """Main program loop for the contact book."""
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            search_contact(name)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
