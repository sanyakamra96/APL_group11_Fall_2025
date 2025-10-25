#include "expense.hpp"

#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

vector<Expense> expenses;  // in-memory storage

// Convert Category enum to string
string categoryToString(Category c) {
  switch (c) {
    case Food:
      return "Food";
    case Travel:
      return "Travel";
    case Entertainment:
      return "Entertainment";
    case Misc:
      return "Misc";
  }
  return "Unknown";
}

// Convert string to Category enum
Category stringToCategory(const string& s) {
  if (s == "Food") return Food;
  if (s == "Travel") return Travel;
  if (s == "Entertainment") return Entertainment;
  return Misc;
}

// Add new expense
void addExpense() {
  Expense e;
  int choice;

  cout << "Enter date (YYYY-MM-DD): ";
  cin >> e.date;
  cout << "Enter amount: ";
  cin >> e.amount;
  cout << "Choose category:\n1. Food\n2. Travel\n3. Entertainment\n4. Misc\n> ";
  cin >> choice;
  e.category = static_cast<Category>(choice - 1);

  cin.ignore();
  cout << "Enter description: ";
  getline(cin, e.description);

  expenses.push_back(e);
  saveToFile();  // auto-save
  cout << "Expense added and saved!\n";
}

// Display all expenses
void displayExpenses() {
  cout << "\n===== All Expenses =====\n";
  if (expenses.empty()) {
    cout << "No expenses recorded yet.\n";
    return;
  }
  for (const auto& e : expenses) {
    cout << "Date: " << e.date << ", Amount: $" << e.amount
         << ", Category: " << categoryToString(e.category)
         << ", Description: " << e.description << endl;
  }
  cout << "========================\n";
}

// Save expenses to file
void saveToFile() {
  ofstream out("data/expenses.txt");
  for (const auto& e : expenses) {
    out << e.date << "," << e.amount << "," << categoryToString(e.category)
        << "," << e.description << "\n";
  }
  out.close();
}

// Load expenses from file
void loadFromFile() {
  expenses.clear();  // prevent duplication
  ifstream in("data/expenses.txt");
  if (!in.is_open()) return;

  Expense e;
  string line;
  while (getline(in, line)) {
    size_t pos1 = line.find(',');
    size_t pos2 = line.find(',', pos1 + 1);
    size_t pos3 = line.find(',', pos2 + 1);

    e.date = line.substr(0, pos1);
    e.amount = stoi(line.substr(pos1 + 1, pos2 - pos1 - 1));
    e.category = stringToCategory(line.substr(pos2 + 1, pos3 - pos2 - 1));
    e.description = line.substr(pos3 + 1);

    expenses.push_back(e);
  }
  in.close();
}

// Filter by date range and/or category
void filterAndSearchExpenses() {
  string startDate, endDate;
  int choice;
  bool useCategory = false;
  Category catChoice;

  cout << "\nFilter by date range? (1 = Yes, 0 = No): ";
  cin >> choice;
  if (choice == 1) {
    cout << "Enter start date (YYYY-MM-DD): ";
    cin >> startDate;
    cout << "Enter end date (YYYY-MM-DD): ";
    cin >> endDate;
  }

  cout << "Filter by category? (1 = Yes, 0 = No): ";
  cin >> choice;
  if (choice == 1) {
    useCategory = true;
    int cat;
    cout << "Choose category:\n1. Food\n2. Travel\n3. Entertainment\n4. "
            "Misc\n> ";
    cin >> cat;
    catChoice = static_cast<Category>(cat - 1);
  }

  cout << "\n--- Matching Results ---\n";
  bool found = false;
  for (const auto& e : expenses) {
    bool match = true;
    if (!startDate.empty() && !endDate.empty())
      match = (e.date >= startDate && e.date <= endDate);
    if (useCategory && match) match = (e.category == catChoice);
    if (match) {
      found = true;
      cout << e.date << " | $" << e.amount << " | "
           << categoryToString(e.category) << " | " << e.description << endl;
    }
  }
  if (!found) cout << "No matching expenses found.\n";
}

// Calculate total amount per category
void totalByCategory() {
  int totals[4] = {0};
  for (const auto& e : expenses) totals[e.category] += e.amount;

  cout << "\n===== Total by Category =====\n";
  cout << "Food: $" << totals[Food] << endl;
  cout << "Travel: $" << totals[Travel] << endl;
  cout << "Entertainment: $" << totals[Entertainment] << endl;
  cout << "Misc: $" << totals[Misc] << endl;
}
