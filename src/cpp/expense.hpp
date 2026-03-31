#ifndef EXPENSE_HPP
#define EXPENSE_HPP

#include <string>
using namespace std;

// Enum for categories
enum Category { Food, Travel, Entertainment, Misc };

// Struct for an expense
struct Expense {
  string date;
  int amount;
  Category category;
  string description;
};

// Function declarations (no definitions here)
string categoryToString(Category c);
Category stringToCategory(const string& s);
void addExpense();
void displayExpenses();
void totalByCategory();
void filterAndSearchExpenses();
void saveToFile();
void loadFromFile();

#endif
