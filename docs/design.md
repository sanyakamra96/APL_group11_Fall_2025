Expense Tracker Application – Design Document
## 1. Overview

The Expense Tracker Application is designed to record, view, filter, and summarize daily expenses.
Each expense entry includes a date, amount, category, and description.
The program allows users to add new records, filter by date or category, and view total spending summaries.

The project includes two separate implementations:

C++ Implementation (branch: cpp_implementation)

Python Implementation (branch: python_implementation)

## 2. Objectives

Store and manage expense records efficiently.

Provide filtering and search features based on date range or category.

Summarize expenses by category and display total spending.

Demonstrate language-specific features and design differences between C++ and Python.

## 3. Data Model
Fields
Field	Description	Example
date	Expense date in ISO format (YYYY-MM-DD)	2025-10-25
amount	Expense amount	100
category	Expense type (Food, Travel, Entertainment, Misc)	Food
description	Brief explanation of the expense	Lunch at cafe
C++ Implementation

Uses a struct Expense to define the model.

Categories are represented using an enum.

Data is stored in an in-memory std::vector<Expense>.

Data persistence handled with file I/O (ifstream / ofstream).

Python Implementation

Uses a list of dictionaries for dynamic data storage.

Each record is stored as:

{"date": "YYYY-MM-DD", "amount": 100, "category": "Food", "description": "Lunch"}


Data persistence is achieved using the json module.

Date comparison is handled using the datetime library.

## 4. Functional Components
```
| Function              | Description                                      | C++ Implementation           | Python Implementation                    |
| --------------------- | ------------------------------------------------ | ---------------------------- | ---------------------------------------- |
| Add Expense         | Prompts user for details and stores a new record | Struct pushed to vector      | Dictionary appended to list              |
| View Expenses       |  Displays all recorded expenses                   | Loops through vector         | Loops through list                       |
| Filter / Search     | Filters expenses by date range or category       | String-based date comparison | Uses `datetime` for accurate comparisons |
| Total by Category   | Calculates total spending by category            | Integer array accumulator    | Dictionary accumulator                   |
| Save to File        | Saves all expenses persistently                  | Writes to `.txt` file        | Writes to `.json` file                   |
| Load from File      | Loads previous session data                      | Reads text file              | Loads JSON data                          |
```
## 5. Program Flow
```
Start
│
├── Load expenses from file
│
├── Display menu:
│     1. Add Expense
│     2. View Expenses
│     3. Filter / Search Expenses
│     4. Total by Category
│     5. Save & Exit
│
├── Perform selected action
│
├── Save to file (auto or on exit)
│
└── End
```
## 6. File Storage Format
C++ (data/expenses.txt)

```
2025-10-25,50,Food,Lunch
2025-10-26,100,Travel,Uber ride
```
Python (expenses.json)
```
[
  {"date": "2025-10-25", "amount": 50, "category": "Food", "description": "Lunch"},
  {"date": "2025-10-26", "amount": 100, "category": "Travel", "description": "Uber ride"}
]
```

## 7. Language-Specific Features
C++

~~~Structs and enums for strong typing

STL vector for dynamic storage

File I/O for persistence

Static typing ensures compile-time safety

Manual compilation using g++ -std=c++11
~~~
Python

~~~
Dictionaries and lists for flexible, dynamic data structures

datetime library for date handling

Automatic memory management

Dynamic typing for faster development

Simple file operations using json
~~~
## 8. Design Decisions

ISO date format (YYYY-MM-DD) ensures consistent lexicographic comparison.

File-based persistence retains user data between sessions.

Menu-driven CLI provides a consistent user experience across both languages.

The design focuses on simplicity, modularity, and language comparability.

## 9. Testing

Testing was performed through both interactive user input and hardcoded test files located in the test/ directory.
Each implementation was tested for:
~~~
Adding new expenses

Displaying all expenses

Filtering by date and category

Calculating category totals
~~~
## 10. Conclusion

The Expense Tracker Application demonstrates the same functionality implemented in two programming languages — C++ and Python — highlighting differences in syntax, data handling, and design philosophy.
Both implementations fulfill the project’s requirements while showcasing the unique strengths of each language:

C++: Performance, structure, and static type safety.

Python: Simplicity, readability, and rapid development.

Together, they provide a clear comparative study of how language characteristics influence program design and implementation.
