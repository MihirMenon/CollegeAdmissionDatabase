import sqlite3

def query_all(table_name):
    conn = sqlite3.connect("college_admission.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_record(table: str, columns: list, values: tuple):
    conn = sqlite3.connect("college_admission.db")
    cur = conn.cursor()
    placeholders = ", ".join("?" for _ in values)
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
    cur.execute(query, values)
    conn.commit()
    conn.close()
