try:
    from expenses import add_expense, view_expenses
    print("Imports from expenses.py successful")
except ImportError as e:
    print(f"Error importing from expenses.py: {e}")
