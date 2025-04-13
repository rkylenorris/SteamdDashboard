import sqlite3
import os
from pathlib import Path

# set paths
sql_script_path = Path(__file__).parent / "sql" / "create_db.sql"
db_path = Path(__file__).parent / "data" / "games.db"

# if db already exists, delete it
if db_path.exists():
    os.remove(db_path)

# connect/create db and cursor
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# read sql script
sql_script = sql_script_path.read_text(encoding='utf-8')

# execute sql script to create tables
cursor.executescript(sql_script)
conn.commit()
conn.close()