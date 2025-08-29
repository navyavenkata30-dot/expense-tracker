import os

# File to store expenses
EXPENSE_FILE = "expenses.txt"

# Function to add expense
def add_expense(amount, category, note=""):
    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{amount},{category},{note}\n")
    print("✅ Expense added successfully!")

# Function to view expenses
def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("⚠️ No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    with open(EXPENSE_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            print("⚠️ No expenses found.")
            return
        for idx, line in enumerate(lines, start=1):
            amount, category, note = line.strip().split(",", 2)
            print(f"{idx}. 💵 {amount} | 📂 {category} | 📝 {note if note else 'N/A'}")

# Main program loop
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Clean input so user can type 200, 200$, or 1,200.50
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input.replace("$", "").replace(",", "").strip())
        except ValueError:
            print("❌ Invalid amount! Please enter numbers only.")
            continue

        category = input("Enter category (Food/Transport/etc): ")
        note = input("Enter note (optional): ")
        add_expense(amount, category, note)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("👋 Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again!")

