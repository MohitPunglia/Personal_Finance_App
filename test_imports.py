try:
    from expenses import add_expense, view_expenses
    print("Imports from expenses.py successful")
except ImportError as e:
    print(f"Error importing from expenses.py: {e}")

try:
    from budget import set_budget
    print("Imports from budget.py successful")
except ImportError as e:
    print(f"Error importing from budget.py: {e}")

try:
    from database import create_db, execute_query, fetch_all
    print("Imports from database.py successful")
except ImportError as e:
    print(f"Error importing from database.py: {e}")
