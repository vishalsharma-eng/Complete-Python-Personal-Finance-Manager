from src.file_manager import load_expenses

def get_all_expenses():
    return load_expenses()

def show_all_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    for exp in expenses:
        print(exp)

def category_summary():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        summary[exp.category] = summary.get(exp.category, 0) + exp.amount

    print("\nCategory-wise Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")

def monthly_report(month):
    expenses = load_expenses()
    print(f"\nMonthly Report for {month}:")
    for exp in expenses:
        if exp.date.startswith(month):
            print(exp)
