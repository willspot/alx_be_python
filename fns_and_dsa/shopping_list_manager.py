def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Prompt for user input

        if choice == '1':  # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add item to the list
            print(f"{item} has been added to the list.")

        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} was not found in the list.")

        elif choice == '3':  # View the list
            if shopping_list:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices

if __name__ == "__main__":
    main()
