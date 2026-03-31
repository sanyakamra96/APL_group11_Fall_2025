# APL_group11_Fall_2025
Expense Tracker Application 

# Expense Tracker Application (C++)

## Overview
A console-based application that allows users to record, view, and categorize expenses.
Users can filter expenses by date or category and calculate total spending by category.

## Features
- Add and view expenses
- Filter or search by date and category
- Display totals by category
- Persistent storage in `data/expenses.txt`
- Uses C++ features: structs, enums, STL vectors, and file I/O

## Compilation
```bash
cd src
g++ -std=c++11 main.cpp expense.cpp -o expense_app
./expense_app


Output----->

========================

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Filter / Search Expenses
4. Total by Category
5. Save & Exit
Choose option: 

1
Enter date (YYYY-MM-DD): 2009-02-21
Enter amount: 500
Choose category:
1. Food
2. Travel
3. Entertainment
4. Misc
> 2
Enter description: flight to sf
Expense added and saved!

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Filter / Search Expenses
4. Total by Category
5. Save & Exit
Choose option: 2

===== All Expenses =====
Date: 2022-21-21, Amount: $212, Category: Travel, Description: sanya
Date: 2022-03-23, Amount: $32, Category: Food, Description: dsd
Date: 2009-21-12, Amount: $2222, Category: Food, Description: 121
Date: 2120-12-12, Amount: $311, Category: Food, Description: 1121
Date: 2011-21-12, Amount: $2, Category: Food, Description: baba
Date: 2033-31-12, Amount: $2112, Category: Entertainment, Description: dsada
Date: 2021-21-21, Amount: $4302, Category: Misc, Description: heyey
Date: 2009-02-21, Amount: $500, Category: Travel, Description: flight to sf
========================

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Filter / Search Expenses
4. Total by Category
5. Save & Exit
Choose option: 3

Filter by date range? (1 = Yes, 0 = No): 1
Enter start date (YYYY-MM-DD): 2000-01-02
Enter end date (YYYY-MM-DD): 2005-01-02
Filter by category? (1 = Yes, 0 = No): 0

--- Matching Results ---
No matching expenses found.

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Filter / Search Expenses
4. Total by Category
5. Save & Exit
Choose option: 4

===== Total by Category =====
Food: $2567
Travel: $712
Entertainment: $2112
Misc: $4302

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Filter / Search Expenses
4. Total by Category
5. Save & Exit
Choose option: 5
Exiting...
```
===============
## Test
===============
``` g++ -I src/cpp tests/test_expense.cpp -o test_expense
./test_expense

Output---->

sanya.kamra@MAC-F4NQ92FVL2 APL_group11_Fall_2025 % g++ tests/test_expense.cpp -o test_expense
./test_expense

=== Running Expense Tracker Tests ===
testExpenseCreation passed.
 testExpenseStorage passed.
 testCategoryNames passed.
All tests passed successfully 
