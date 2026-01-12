def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. view Expenses")
    print("3. Exit")
'''
show_menu function displays the main menu options for the expense tracker application.

'''
def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1 to 3):")

        if choice == "1":
            print("Add expense selected.")
        elif choice == "2":
            print("View expenses selected.")
        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Invalid choice . Please retry")

''' 

def main function runs the main loop of the expense tracker application, handling user input and menu navigation.
While True: keeps the program running until the user decides to exit.

'''
if __name__ == "__main__":
    main()

'''
The __name_ == "_main_" block ensures that the main function is called when the script is executed directly.
Why This Is Critical (Real Reason)
Without this block:

Code runs every time the file is imported

Causes unwanted side effects

Breaks modular design

With this block:

Your file can be:

Run as a script

Imported as a module

Clean separation of concerns
'''