#include <cassert>
#include <iostream>
#include <vector>

#include "../src/cpp/expense.hpp"

using namespace std;

string getCategoryName(Category c) {
  switch (c) {
    case Food:
      return "Food";
    case Travel:
      return "Travel";
    case Entertainment:
      return "Entertainment";
    case Misc:
      return "Misc";
    default:
      return "Unknown";
  }
}

void testExpenseCreation() {
  Expense e;
  e.date = "2025-10-25";
  e.amount = 500;
  e.category = Travel;
  e.description = "Flight ticket";

  assert(e.date == "2025-10-25");
  assert(e.amount == 500);
  assert(e.category == Travel);
  assert(e.description == "Flight ticket");

  cout << "testExpenseCreation passed.\n";
}

void testExpenseStorage() {
  vector<Expense> expenses;

  Expense e1 = {"2025-10-25", 100, Food, "Lunch"};
  Expense e2 = {"2025-10-26", 200, Entertainment, "Movie"};

  expenses.push_back(e1);
  expenses.push_back(e2);

  assert(expenses.size() == 2);
  assert(expenses[0].amount == 100);
  assert(expenses[1].category == Entertainment);

  cout << " testExpenseStorage passed.\n";
}

void testCategoryNames() {
  assert(getCategoryName(Food) == "Food");
  assert(getCategoryName(Travel) == "Travel");
  assert(getCategoryName(Entertainment) == "Entertainment");
  assert(getCategoryName(Misc) == "Misc");

  cout << " testCategoryNames passed.\n";
}

int main() {
  cout << "=== Running Expense Tracker Tests ===\n";
  testExpenseCreation();
  testExpenseStorage();
  testCategoryNames();
  cout << "All tests passed successfully \n";
  return 0;
}
