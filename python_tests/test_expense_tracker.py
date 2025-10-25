# test_expense_tracker.py
# Tests / Sample usage for Expense Tracker
# Author: Kajol Makhijani
# Date: 2025

from python_version.expense_tracker import ExpenseTracker

def run_tests():
    tracker = ExpenseTracker()

    # Sample expenses
    tracker.add_expense("2025-10-01", 50.0, "Food", "Groceries")
    tracker.add_expense("2025-10-03", 20.0, "Transport", "Uber")
    tracker.add_expense("2025-10-05", 15.0, "Food", "Lunch")

    # View all expenses
    print("All Expenses:")
    for e in tracker.view_expenses():
        print(e)

    # Filter by category
    print("\nFood Expenses:")
    for e in tracker.filter_by_category("Food"):
        print(e)

    # Filter by date range
    print("\nExpenses from 2025-10-02 to 2025-10-05:")
    for e in tracker.filter_by_date_range("2025-10-02", "2025-10-05"):
        print(e)

    # Summary by category
    print("\nSummary by category:")
    print(tracker.summary_by_category())

    # Total expenses
    print("\nTotal Expenses:", tracker.total_expenses())


if __name__ == "__main__":
    run_tests()

