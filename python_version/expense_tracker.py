import json
from datetime import datetime

# In-memory list of expenses
expenses = []

# Add a new expense
def add_expense(date, amount, category, description):
    try:
        expense = {
            "date": datetime.strptime(date, "%Y-%m-%d"),
            "amount": float(amount),
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print(f"✅ Expense added: {description} (${amount}) on {date}")
    except ValueError:
        print("❌ Invalid input. Please ensure date is YYYY-MM-DD and amount is numeric.")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for exp in expenses:
        print(f"{exp['date'].date()} | {exp['category']} | ${exp['amount']:.2f} | {exp['description']}")

# Filter by category
def filter_by_category(category):
    filtered = [e for e in expenses if e['category'].lower() == category.lower()]
    if not filtered:
        print(f"No expenses found for category '{category}'.")
    else:
        for e in filtered:
            print(f"{e['date'].date()} | {e['category']} | ${e['amount']:.2f} | {e['description']}")

# Filter by date range
def filter_by_date_range(start, end):
    try:
        s = datetime.strptime(start, "%Y-%m-%d")
        e = datetime.strptime(end, "%Y-%m-%d")
        filtered = [x for x in expenses if s <= x['date'] <= e]
        for exp in filtered:
            print(f"{exp['date'].date()} | {exp['category']} | ${exp['amount']:.2f}")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

# Summarize expenses
def summarize_expenses():
    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0) + e['amount']
    print("\nSummary by Category:")
    for cat, amt in totals.items():
        print(f"{cat}: ${amt:.2f}")
    print(f"Total Expenses: ${sum(totals.values()):.2f}")

# Simple Testing
if __name__ == "__main__":
    add_expense("2025-10-21", 25.50, "Food", "Lunch with team")
    add_expense("2025-10-22", 40, "Travel", "Uber to office")
    add_expense("2025-10-23", 15.75, "Food", "Coffee & snack")
    view_expenses()
    print("\nFiltered by Category: Food")
    filter_by_category("Food")
    print("\nFiltered by Date Range (2025-10-21 to 2025-10-22):")
    filter_by_date_range("2025-10-21", "2025-10-22")
    summarize_expenses()

