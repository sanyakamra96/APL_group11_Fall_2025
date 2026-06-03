# test_expense_tracker.py
# Automated Tests for Expense Tracker
# Author: Kajol Makhijani
# Date: 2025

"""
This test script validates all major functions of the Expense Tracker.
It runs without user input and demonstrates:
1. Adding expenses
2. Viewing all expenses
3. Filtering by category
4. Filtering by date range
5. Calculating category totals
6. Displaying total expenses
"""

import sys, os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "python"))
)
from expense_tracker import ExpenseTracker


def run_tests():
    tracker = ExpenseTracker()

    # Clear any previous data for clean testing
    tracker.expenses = []

    # Add sample expenses
    tracker.add_expense("2025-10-01", 45.5, "Food", "Lunch at Cafe")
    tracker.add_expense("2025-10-02", 120.0, "Travel", "Train Ticket")
    tracker.add_expense("2025-10-04", 30.0, "Food", "Groceries")
    tracker.add_expense("2025-10-05", 60.0, "Entertainment", "Movie night")

    print("\n===== Test 1: View All Expenses =====")
    tracker.view_expenses()

    print("\n===== Test 2: Filter by Category (Food) =====")
    tracker.filter_by_category("Food")

    print("\n===== Test 3: Filter by Date Range (2025-10-02 to 2025-10-05) =====")
    tracker.filter_by_date_range("2025-10-02", "2025-10-05")

    print("\n===== Test 4: Summary by Category =====")
    tracker.summary_by_category()

    print("\n===== Test 5: Total Expenses =====")
    tracker.total_expenses()


if __name__ == "__main__":
    run_tests()
