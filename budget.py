from database import execute_query, fetch_all

def set_budget(category, amount):
    query = "INSERT INTO budgets (category, amount) VALUES (?, ?)"
    execute_query(query, (category, amount))

def view_budgets():
    query = "SELECT * FROM budgets"
    return fetch_all(query)
