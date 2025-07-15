import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)
''', [
    ("Alice", "HR", 60000),
    ("Bob", "IT", 75000),
    ("Charlie", "Sales", 50000),
    ("David", "IT", 68000),
    ("Eve", "Marketing", 62000)
])

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database 'company.db' created with 'employees' table and sample data.")
