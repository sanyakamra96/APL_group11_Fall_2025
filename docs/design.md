Expense Tracker Application – Design Document

Overview
The Expense Tracker Application is designed to record, view, filter, and summarize daily expenses. Each expense entry includes a date, amount, category, and description. The program allows users to add new records, filter by date or category, and view total spending summaries.
The project includes two implementations:

C++ Implementation (branch: cpp_implementation)

Python Implementation (branch: python_implementation)

Objectives

Store and manage expense records efficiently.

Provide filtering and search features based on date range or category.

Summarize expenses by category and display total spending.

Demonstrate language-specific features (C++ vs Python).

Data Model
Fields:

date: Expense date in ISO format (YYYY-MM-DD)

amount: Expense amount

category: Expense type (Food, Travel, Entertainment, Misc)

description: Brief explanation of the expense

C++ Implementation:

Uses a struct Expense to define the model.

Categories are represented using an enum.

Data stored in an in-memory vector<Expense>.

Data persistence handled with file I/O (ifstream / ofstream).

Python Implementation:

Uses a list of dictionaries for dynamic data storage.

Each record is a dictionary with keys: date, amount, category, and description.

Data persistence achieved using the json module.

Date comparison handled using the datetime library.

Functional Components
Add Expense – Prompts user for details and stores new record.
View Expenses – Displays all expenses with details.
Filter / Search – Filters by date range and/or category.
Total by Category – Calculates total spent in each category.
Save to File – Saves all expenses persistently.
Load from File – Loads previous session data.

C++ Implementation: struct-based data, STL vector, manual file handling.
Python Implementation: dictionary-based data, list operations, json-based file handling.

Program Flow
Start
│
├── Load expenses from file
│
├── Display menu:
│ 1. Add Expense
│ 2. View Expenses
│ 3. Filter / Search Expenses
│ 4. Total by Category
│ 5. Save & Exit
│
├── Perform selected action
│
├── Save to file (auto or on exit)
│
└── End

File Storage Format
C++ (data/expenses.txt):
2025-10-25,50,Food,Lunch
2025-10-26,100,Travel,Uber ride

Python (expenses.json):
[
{"date": "2025-10-25", "amount": 50, "category": "Food", "description": "Lunch"},
{"date": "2025-10-26", "amount": 100, "category": "Travel", "description": "Uber ride"}
]

Language-Specific Features
C++

Structs and Enums for strong typing

STL Vector for dynamic storage

File I/O for persistence

Static typing for compile-time safety

Manual compilation with g++ -std=c++11

Python

Dictionaries and Lists for dynamic data

datetime library for date comparison

Automatic memory management

Dynamic typing for faster development

Simple file handling using json module

Design Decisions

ISO date format (YYYY-MM-DD) used for consistent comparison.

File-based persistence ensures data retention between sessions.

Menu-driven CLI ensures a similar experience across both languages.

Testing

Hardcoded test files added under the test/ directory.

Tested for:

Adding new expenses

Displaying all expenses

Filtering by date and category

Calculating totals

Conclusion
The design emphasizes simplicity, modularity, and comparability across languages. Both implementations fulfill the same functional requirements while showcasing the contrasting strengths of C++ (performance, structure) and Python (simplicity, flexibility).