import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../data/book_collection.db")

class Author:
    def __init__(self, name):
        self.name = name

    def save(self):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        connection.close()
        return authors

    @staticmethod
    def delete(author_id):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM authors WHERE author_id=?", (author_id,))
        connection.commit()
        connection.close()