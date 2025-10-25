# expense_tracker.py
# Python Implementation of Expense Tracker for Deliverable 2
# Author: Kajol Makhijani
# Date: 2025

from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        """Add a new expense to the tracker."""
        expense = {
            "date": datetime.strptime(date, "%Y-%m-%d"),
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)

    def view_expenses(self):
        """Return all expenses in a readable string format."""
        return [
            f"{e['date'].date()} | {e['category']} | ${e['amount']:.2f} | {e['description']}"
            for e in self.expenses
        ]

    def filter_by_category(self, category):
        """Return expenses filtered by category."""
        return [e for e in self.expenses if e["category"].lower() == category.lower()]

    def filter_by_date_range(self, start_date, end_date):
        """Return expenses within a date range (inclusive)."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return [e for e in self.expenses if start <= e["date"] <= end]

    def summary_by_category(self):
        """Return total expenses grouped by category."""
        summary = {}
        for e in self.expenses:
            summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
        return summary

    def total_expenses(self):
        """Return total of all expenses."""
        return sum(e["amount"] for e in self.expenses)

-
