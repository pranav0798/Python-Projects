'''
For Day 2: Below is the syntax followed
expenses = []

def show_menu():
    ...

def add_expense():
    ...

def view_expenses():
    ...

def main():
    ...

if __name__ == "__main__":
    main()

For Day 3 : We add the date field to each expense entry and update the add_expense function to capture the date from the user.
For date field , we will use a tuple in the format (YYYY,MM,DD)
We will also update the view_expenses function to display the date along with other expense details.
'''

expenses = []

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. view Expenses")
    print("3. Exit")
'''
1)show_menu function displays the main menu options for the expense tracker application.
2) len(parts) is used to ensure the date input is in the correct format (YYYY-MM-DD). If value is not 3, it indicates an invalid format.
3) year, month, day = parts unpacks the split date input into individual components for further processing.
'''

def add_expense():
    try:
        date_input = input(" Enter the date (YYYY-MM-DD):").strip()
        parts = date_input.split("-")
        
        if len(parts)!=3:
            print("Invalid format , please use yyyy-mm-dd for example 2024-12-31")
            return
        
        year, month, day = parts

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            print("Please enter numerical date values.")
            return
        
        date = (int(year), int(month), int(day))

        amount = float(input("Enter expense amount:"))
        if amount <=0:
            print("Amount must be greater than zero.")
            return
        
        category = input("Enter category(Food,Transport,etc):").strip()
        note = input("Enter a short note:").strip()

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "note": note
        }
        expenses.append(expense)
        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
'''

1) add_expense function prompts the user to input expense details and adds the expense to the expenses list.
2) .strip() is used to remove any leading or trailing whitespace from user input.
3) try-except block handles invalid numeric input for the amount.
4) For Day 3 if not expenses(): loop remains same as Day 2
5) 

'''
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\n--- Your Expenses ---")
    for idx,expense in enumerate(expenses, start=1):
        year, month, day = expense["date"]
        print(
            f"{idx}.{year}-{month:02d}-{day:02d} | "
            f"{expense['category']} | "
            f"{expense['amount']} | "
            f"{expense['note']}"
            )

'''
1) if not expenses: checks if the expenses list is empty and informs the user if there are no recorded expenses.
2) for idx,expense in enumerate(expenses, start=1): iterates over the expenses list, providing an index for each expense starting from 1. 
3) enumerate is used to get both the index and the expense item.
4) print(f"{idx}.{expense['category']} | {expense['amount']} | {expense['note']}") formats and displays each expense's details.
5) f-strings are used for easier and more readable string formatting.
6) | is used as a separator for better readability of expense details.
'''
def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1 to 3):")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Invalid choice . Please retry")

''' 

1) def main function runs the main loop of the expense tracker application, handling user input and menu navigation.





2) While True: keeps the program running until the user decides to exit.
3) In Day 1 , we had print to show which option is selected.
4) In Day 2, we will replace those print statements with actual function calls to add and view expenses.

'''
if __name__ == "__main__":
    main()

'''
1) The __name_ == "_main_" block ensures that the main function is called when the script is executed directly.
2) Why This Is Critical (Real Reason)
Without this block:

Code runs every time the file is imported

Causes unwanted side effects

Breaks modular design

3) With this block:

Your file can be:

Run as a script

Imported as a module

Clean separation of concerns
'''