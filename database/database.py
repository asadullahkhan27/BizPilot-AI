import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "bizpilot.db"


def get_connection():

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def init_db():

    connection = get_connection()

    cursor = connection.cursor()

    # Finance
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            kind TEXT NOT NULL,

            category TEXT NOT NULL,

            amount REAL NOT NULL,

            description TEXT,

            date TEXT NOT NULL
        )
    """)

    # Sales CRM
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer TEXT NOT NULL,

            company TEXT,

            value REAL DEFAULT 0,

            status TEXT NOT NULL,

            next_followup TEXT,

            notes TEXT
        )
    """)

    # Inventory
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            product TEXT NOT NULL,

            sku TEXT,

            quantity INTEGER NOT NULL,

            reorder_level INTEGER DEFAULT 5,

            unit_price REAL DEFAULT 0
        )
    """)

    # Employees
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            department TEXT,

            role TEXT,

            salary REAL DEFAULT 0,

            status TEXT DEFAULT 'Active'
        )
    """)

    connection.commit()

    connection.close()
