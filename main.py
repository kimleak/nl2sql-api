from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Input model
class QueryRequest(BaseModel):
    question: str

# NL to SQL logic (you can replace with spaCy or transformers)
def nl_to_sql(nl_input):
    if "all employees" in nl_input.lower():
        return "SELECT * FROM employees;"
    elif "it department" in nl_input.lower():
        return "SELECT * FROM employees WHERE department = 'IT';"
    return None

@app.post("/query")
def query_db(request: QueryRequest):
    sql = nl_to_sql(request.question)
    if not sql:
        return {"error": "Could not parse question."}

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return {"query": sql, "results": rows}
