Expense Tracker Application (Fall 2025 – Group 11)
## Overview

The Expense Tracker is a console-based application that allows users to record, view, and categorize their daily expenses.
Users can filter expenses by date range or category, and view total spending by category or overall.

This project demonstrates how the same functionality can be implemented in two different languages — C++ and Python — highlighting syntax, design, and performance differences.

## Languages and Branches
Language	Branch Name	            Description
C++	        cpp_implementation	Contains the C++ version with struct-based data model, STL vectors, and file I/O.
Python	    python_implementation	Contains the Python version using dictionaries, lists, and the datetime library.

## Core Functionalities

Add a new expense (date, amount, category, description)

View all recorded expenses

Filter and search by date or category

Display total expenses by category

Save and load data from file

## Repository Structure
APL_group11_Fall_2025/
├── cpp/
│   ├── main.cpp
│   ├── expense.cpp
│   ├── expense.hpp
│   └── data/expenses.txt
├── python/
│   └── expense_tracker.py
├── test/
│   └── test_expense_tracker.py│   
    ├── test_expense.cpp
└── docs/
    ├── design.md
How to Run (C++)
cd cpp
g++ -std=c++11 main.cpp expense.cpp -o expense_app
./expense_app

How to Run (Python)
cd python
python expense_tracker.py

Credits
Kajol Makhijani— Python Implementation (python_implementation)
Sanya Kamra — C++ Implementation (cpp_implementation)

