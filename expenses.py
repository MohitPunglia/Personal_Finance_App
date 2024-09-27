

def view_expenses():
    query = "SELECT * FROM expenses"
    return fetch_all(query)
