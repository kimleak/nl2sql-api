from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import xlsxwriter
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

@app.post("/download")
def download_excel(request: QueryRequest):
    sql = nl_to_sql(request.question)
    if not sql:
        return {"error": "Invalid query"}

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    file_path = "query_result.xlsx"
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    # Write headers
    for col, name in enumerate([desc[0] for desc in cursor.description]):
        worksheet.write(0, col, name)

    # Write data
    for row_idx, row_data in enumerate(rows, start=1):
        for col_idx, value in enumerate(row_data):
            worksheet.write(row_idx, col_idx, value)

    workbook.close()
    return FileResponse(file_path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="query_result.xlsx")
