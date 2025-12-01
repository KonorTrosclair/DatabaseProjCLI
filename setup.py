import sqlite3

# Connect (creates the DB if not exists)
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Read SQL file
with open("database.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Execute SQL script
cur.executescript(sql_script)

# Commit changes and close
conn.commit()
conn.close()

print("Database created successfully with all tables!")
