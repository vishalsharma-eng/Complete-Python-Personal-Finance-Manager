from src.menu import show_menu
from src.expense import Expense
from src.file_manager import save_expense, backup_data
from src.reports import show_all_expenses, category_summary, monthly_report, get_all_expenses
from src.utils import is_valid_amount

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        amount = input("Enter amount: ")
        if not is_valid_amount(amount):
            print("Invalid amount!")
            continue
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        desc = input("Enter description: ")
        save_expense(Expense(amount, category, date, desc))
        print("✅ Expense added successfully!")

    elif choice == "2":
        show_all_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        month = input("Enter month (YYYY-MM): ")
        monthly_report(month)

    elif choice == "5":
        keyword = input("Enter search keyword: ").lower()
        expenses = get_all_expenses()

        for exp in expenses:
            if keyword.lower() in exp.description.lower():
                print(exp)

    elif choice == "6":
        backup_data()
        print("✅ Backup created successfully!")

    elif choice == "7":
        print("Thank you! Exiting program.")
        break

    else:
        print("❌ Invalid choice")
