from database import execute_query, fetch_all

def add_expense(date, category, amount):
    query = "INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)"
    execute_query(query, (date, category, amount))

def view_expenses():
    query = "SELECT * FROM expenses"
    return fetch_all(query)
