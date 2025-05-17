import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Store Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"\nContact {i}")
            print(f"Name   : {c['name']}")
            print(f"Phone  : {c['phone']}")
            print(f"Email  : {c['email']}")
            print(f"Address: {c['address']}")

# Search contact by name or phone
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print("\nContact Found:")
            print(f"Name   : {c['name']}")
            print(f"Phone  : {c['phone']}")
            print(f"Email  : {c['email']}")
            print(f"Address: {c['address']}")
            found = True
    if not found:
        print("No contact found with that keyword.")

# Update a contact
def update_contact(contacts):
    phone = input("Enter the phone number of the contact to update: ")
    for c in contacts:
        if c["phone"] == phone:
            print("Leave blank to keep existing value.")
            c["name"] = input(f"New name ({c['name']}): ") or c["name"]
            c["email"] = input(f"New email ({c['email']}): ") or c["email"]
            c["address"] = input(f"New address ({c['address']}): ") or c["address"]
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ")
    for i, c in enumerate(contacts):
        if c["phone"] == phone:
            confirm = input(f"Are you sure you want to delete {c['name']}? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                print("Contact deleted.")
            return
    print("Contact not found.")

# Main Menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the application
if __name__ == "__main__":
    main()
