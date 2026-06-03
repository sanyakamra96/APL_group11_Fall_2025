# expense_tracker.py
# Interactive Expense Tracker (Python)
# Author: Kajol Makhijani
# Date: 2025

"""
Overview:
A console-based Expense Tracker that allows users to record, view, filter,
and summarize expenses. Users can filter expenses by date range or category
and calculate total expenses by category or overall.

Core Requirements:
- Data storage for expenses with fields: date, amount, category, description
- Ability to filter/search by date range and category
- Summary function showing total by category and overall

Python-Specific Features:
- Uses dictionaries for dynamic data storage
- Demonstrates Python’s dynamic typing and built-in data structures
- Uses the 'datetime' library for date manipulation
"""

from datetime import datetime
import json
import os


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_from_file()

    def add_expense(self, date, amount, category, description):
        """Add a new expense"""
        self.expenses.append(
            {
                "date": date,
                "amount": amount,
                "category": category,
                "description": description,
            }
        )
        self.save_to_file()
        print("✅ Expense added and saved successfully!")

    def view_expenses(self):
        """Display all recorded expenses"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n===== All Expenses =====")
        for e in self.expenses:
            print(
                f"{e['date']} | ${e['amount']} | {e['category']} | {e['description']}"
            )

    def filter_by_category(self, category):
        """Display expenses filtered by category"""
        results = [
            e for e in self.expenses if e["category"].lower() == category.lower()
        ]
        if not results:
            print(f"No expenses found for category: {category}")
            return
        print(f"\n===== {category} Expenses =====")
        for e in results:
            print(f"{e['date']} | ${e['amount']} | {e['description']}")

    def filter_by_date_range(self, start, end):
        """Display expenses filtered by date range"""
        fmt = "%Y-%m-%d"
        results = []
        for e in self.expenses:
            d = datetime.strptime(e["date"], fmt)
            if datetime.strptime(start, fmt) <= d <= datetime.strptime(end, fmt):
                results.append(e)
        if not results:
            print("No expenses found in this date range.")
            return
        print(f"\n===== Expenses from {start} to {end} =====")
        for e in results:
            print(
                f"{e['date']} | ${e['amount']} | {e['category']} | {e['description']}"
            )

    def summary_by_category(self):
        """Display total spending by category"""
        totals = {}
        for e in self.expenses:
            cat = e["category"]
            totals[cat] = totals.get(cat, 0) + e["amount"]
        print("\n===== Total by Category =====")
        for cat, total in totals.items():
            print(f"{cat}: ${total:.2f}")

    def total_expenses(self):
        """Display total of all recorded expenses"""
        total = sum(e["amount"] for e in self.expenses)
        print(f"\n===== Overall Total =====\nTotal Expenses: ${total:.2f}")

    def save_to_file(self):
        """Save expenses to a JSON file"""
        os.makedirs("data", exist_ok=True)
        with open("data/expenses.json", "w") as f:
            json.dump(self.expenses, f, indent=2)

    def load_from_file(self):
        """Load expenses from JSON file"""
        try:
            with open("data/expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Expense Tracker (Python) =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date Range")
        print("5. Summary by Category")
        print("6. Total Expenses")
        print("7. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(date, amount, category, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter category: ")
            tracker.filter_by_category(category)

        elif choice == "4":
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            tracker.filter_by_date_range(start, end)

        elif choice == "5":
            tracker.summary_by_category()

        elif choice == "6":
            tracker.total_expenses()

        elif choice == "7":
            tracker.save_to_file()
            print("Exiting... Data saved successfully!")
            break

        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
