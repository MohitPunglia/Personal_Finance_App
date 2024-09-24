def fetch_all(query, params=()):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows
