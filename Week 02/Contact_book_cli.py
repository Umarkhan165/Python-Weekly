contacts = {
    "Umar": "1234567890",
    "Ali": "9876543210"
}

while True:
    print("\n--- Contact Book ---")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nContacts List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

    elif choice == "2":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print(f"{name} added successfully!")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s number: {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Exiting Contact Book... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")