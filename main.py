import sqlite3


connection = sqlite3.connect('data/book_collection.db')
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price REAL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    )
""")

connection.commit()
connection.close()