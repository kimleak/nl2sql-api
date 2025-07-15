📡 NL2SQL API
A FastAPI-based backend that converts natural language questions into SQL queries, executes them on a SQLite database, and optionally returns results as downloadable Excel files.

🚀 Features
🧠 Natural Language to SQL conversion

🔍 SQL query execution on SQLite

📊 Return query results as JSON

📁 Excel download endpoint (.xlsx)

🌐 Designed to integrate with iOS (SwiftUI) chat apps

📦 API Endpoints
POST /query
Request:

json
Copy
Edit
{
  "question": "Show all employees"
}
Response:

json
Copy
Edit
{
  "query": "SELECT * FROM employees;",
  "results": [
    [1, "Alice", "HR", 60000],
    [2, "Bob", "IT", 75000]
  ]
}
POST /download
Request:

json
Copy
Edit
{
  "question": "Show all employees"
}
Response:

Returns: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

Attachment: Excel file containing SQL results

📁 Project Structure
graphql
Copy
Edit
nl2sql-api/
├── main.py             # FastAPI entrypoint
├── model.py            # NL-to-SQL logic
├── schema.py           # Pydantic models
├── database.py         # DB setup and sample data
├── excel.py            # Excel export logic
├── requirements.txt    # Python dependencies
└── .renderignore       # Ignore unnecessary files during deployment
🧪 Local Setup
Clone the repo:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/nl2sql-api.git
cd nl2sql-api
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run locally:

bash
Copy
Edit
uvicorn main:app --reload
🌍 Deploy
This app can be deployed to Render with:

Auto deploy on main branch push

render.yaml (optional)

.renderignore to skip local-only files

📄 License
MIT License © 2025
