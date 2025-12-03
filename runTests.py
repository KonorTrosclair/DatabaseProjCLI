import sqlite3
import re

DB_FILE = "database.db"
SQL_FILE = "testQ.sql"

def clean_statement(stmt):
    """Remove SQL comments and trim whitespace."""

    stmt = re.sub(r"--.*", "", stmt)
    return stmt.strip()

def is_select(stmt):
    """Check if the cleaned statement starts with SELECT."""
    return stmt.lower().startswith("select")

def format_row(row):
    """SQLite-style formatting: pipe-separated."""
    return "|".join("" if col is None else str(col) for col in row)

def main():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql_script = f.read()


    raw_statements = sql_script.split(";")
    statements = [clean_statement(s) for s in raw_statements if clean_statement(s)]

    for stmt in statements:
        try:
            cur.execute(stmt)

            if is_select(stmt):
                rows = cur.fetchall()
                for row in rows:
                    print(format_row(row))

        except Exception as e:
            print(f"SQL ERROR in:\n{stmt}\n→ {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
