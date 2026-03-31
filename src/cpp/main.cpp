#include <iostream>

#include "expense.hpp"
using namespace std;

int main() {
  loadFromFile();
  int choice;

  do {
    cout << "\n===== Expense Tracker =====\n";
    cout << "1. Add Expense\n";
    cout << "2. View Expenses\n";
    cout << "3. Filter / Search Expenses\n";
    cout << "4. Total by Category and Overall Total\n";
    cout << "5. Save & Exit\n";
    cout << "Choose option: ";
    cin >> choice;

    switch (choice) {
      case 1:
        addExpense();
        break;
      case 2:
        displayExpenses();
        break;
      case 3:
        filterAndSearchExpenses();
        break;
      case 4:
        totalByCategory();
        break;
      case 5:
        saveToFile();
        cout << "Exiting...\n";
        break;
      default:
        cout << "Invalid choice.\n";
        break;
    }
  } while (choice != 5);

  return 0;
}
