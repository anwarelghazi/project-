# Book Manager CLI Application

This is a Python-based CLI application for managing a collection of books and authors. It allows users to add, view, and delete authors and books. The application uses SQLite for database management and is implemented using Object-Relational Mapping (ORM) techniques.

## Features

- _Add Author_: Add a new author to the database.
- _Add Book_: Add a new book to the database, associating it with an existing author.
- _View All Authors_: List all authors in the database.
- _View All Books_: List all books in the database, along with their associated authors.
- _Delete Author_: Remove an author from the database.

# Book Manager CLI Application

This is a Python-based CLI application for managing a collection of books and authors. It allows users to add, view, and delete authors and books. The application uses SQLite for database management and is implemented using Object-Relational Mapping (ORM) techniques.

## Features

- _Add Author_: Add a new author to the database.
- _Add Book_: Add a new book to the database, associating it with an existing author.
- _View All Authors_: List all authors in the database.
- _View All Books_: List all books in the database, along with their associated authors.
- _Delete Author_: Remove an author from the database.

## ORM Requirements

- The application includes an SQLite database created and modified with Python ORM methods.
- The data model includes at least 2 model classes: Author and Book.
- The data model includes a one-to-many relationship: An author has many books.
- Property methods are defined to add appropriate constraints to each model class.
- Each model class includes ORM methods: create, delete, get_all, and find_by_id.

## CLI Requirements

- The CLI displays menus for user interaction.
- The CLI uses loops to keep the user in the application until they choose to exit.
- For each class in the data model, the CLI includes options to create, delete, display all, view related objects, and find by attribute.
- The CLI validates user input and object creations/deletions, providing informative errors to the user.

## Requirements

- Python 3.x
- sqlite3

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anwarelghazi/project-
```
