import sqlite3

def create_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    category TEXT,
                    amount REAL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY,
                    category TEXT,
                    amount REAL
                )''')
    conn.commit()
    conn.close()

def execute_query(query, params=()):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()

def fetch_all(query, params=()):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows
