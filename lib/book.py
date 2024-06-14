import os
import sqlite3

class Book:
    def __init__(self, title, price, author_id):
        self.title = title
        self.price = price
        self.author_id = author_id

        # Ensure the directory exists
        os.makedirs('data', exist_ok=True)

        # Create the database file if it doesn't exist
        self.create_database()

    def create_database(self):
        connection = sqlite3.connect('data/book_collection.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            book_id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            price REAL NOT NULL,
                            author_id INTEGER NOT NULL)''')
        connection.commit()
        connection.close()

    def save(self):
        connection = sqlite3.connect('data/book_collection.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, price, author_id) VALUES (?, ?, ?)", (self.title, self.price, self.author_id))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect('data/book_collection.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        connection.close()
        return books

    @staticmethod
    def delete(book_id):
        connection = sqlite3.connect('data/book_collection.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE book_id=?", (book_id,))
        connection.commit()
        connection.close()
