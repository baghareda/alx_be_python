
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input(int("Enter your choice: "))

        if choice == '1':
            item = input(int("choose your item: "))
            shopping_list.append(item)

        elif choice == '2':
            rm = input(int("enter the item you want to remove"))
            if rm in shopping_list:
                shopping_list.remove(item)

        elif choice == '3':
                    print(item)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()