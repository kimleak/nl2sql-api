import sqlite3

def nl_to_sql(nl_input):
    nl_input = nl_input.lower()

    if "all employees" in nl_input:
        return "SELECT * FROM employees;"
    elif "it department" in nl_input:
        return "SELECT * FROM employees WHERE department = 'IT';"
    elif "hr department" in nl_input:
        return "SELECT * FROM employees WHERE department = 'HR';"
    elif "salary more than" in nl_input:
        # Extract the number
        words = nl_input.split()
        for i, word in enumerate(words):
            if word.isdigit():
                return f"SELECT * FROM employees WHERE salary > {word};"
    else:
        return None

# Connect to DB
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Loop to get user input
print("Ask me a question about the employees:")
while True:
    user_input = input(">> ")
    if user_input.lower() in ['exit', 'quit']:
        break

    sql_query = nl_to_sql(user_input)
    if sql_query:
        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print("SQL error:", e)
    else:
        print("Sorry, I couldn't understand your question.")

conn.close()
