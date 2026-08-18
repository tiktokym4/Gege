import sqlite3
from pathlib import Path
from datetime import datetime

DB = Path("data/jiji.db")

def connect():
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    con.commit()
    return con

def add_message(role, text):
    con = connect()
    con.execute(
        "INSERT INTO messages(role,text,created_at) VALUES(?,?,?)",
        (role, text, datetime.utcnow().isoformat())
    )
    con.commit()
    con.close()

def recent_messages(limit=12):
    con = connect()
    rows = con.execute(
        "SELECT role,text FROM messages ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
    con.close()
    return [{"role": r[0], "text": r[1]} for r in reversed(rows)]
