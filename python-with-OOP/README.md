git commit -m "Complete Library Management System with Python OOP and JSON"
# Library Management System

A command-line Library Management System written in Python. It manages books and members, issues and returns books, and saves everything to a JSON file so data is kept between runs.

This is a beginner-to-intermediate project built to practise object-oriented programming, file handling and input validation in Python.

## Features

- Add, search and remove books
- Register members and view all members
- Issue a book to a member and return it
- View the books borrowed by a member
- Automatic saving to `library.json` after every change
- Data is loaded from `library.json` when the program starts
- Input validation (numeric IDs, non-empty titles, authors and names)

## Requirements

- Python **3.10 or higher** (the menu uses the `match` statement)
- No external libraries (only the built-in `json` module)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Run the program:

   ```bash
   python main.py
   ```

   (Use `python3 main.py` on Linux or macOS. Replace `main.py` with your file name.)

## Menu Options

```
========== LIBRARY MANAGEMENT SYSTEM ==========
1.  Display All Books
2.  Add Book
3.  Search Book
4.  Remove Book
5.  Register Member
6.  Display All Members
7.  Issue Book
8.  Return Book
9.  Display Borrowed Books
10. Save Data
0.  Exit
================================================
```

## Project Structure

The program has three classes:

| Class | Responsibility |
|-------|----------------|
| `Book` | Stores book ID, title, author and availability. Shows book details and availability status. |
| `Members` | Stores member ID, name, email and the list of borrowed books. Shows member details and borrowed books. |
| `Library` | Holds all books and members. Handles adding, searching, removing, issuing, returning, loading and saving. |

## How Data Is Stored

Data is saved in `library.json` in the same folder as the program. Borrowed books are stored as a list of book IDs, and the links between members and books are rebuilt when the file is loaded.

```json
{
    "books": [
        {
            "book_ID": 1,
            "title": "Python Basics",
            "author": "John Smith",
            "available": false
        }
    ],
    "members": [
        {
            "member_ID": 101,
            "member_name": "Asha",
            "Email": "asha@example.com",
            "borrowed_books": [1]
        }
    ]
}
```

## Rules and Error Handling

- Book IDs and member IDs must be unique.
- A book that is already borrowed cannot be issued again.
- A borrowed book cannot be removed from the library.
- A book can only be returned by the member who borrowed it.
- If `library.json` is missing, corrupted or incomplete, the program shows a message and starts with empty data instead of crashing.
- Data is fully rebuilt from the file before replacing the current data, so a bad file never leaves the library half-loaded.

## Concepts Practised

- Classes, objects and methods (OOP)
- Object relationships (members hold references to borrowed books)
- Reading and writing JSON files
- Exception handling (`FileNotFoundError`, `JSONDecodeError`, `KeyError`, `OSError`)
- Input validation and menu-driven programs with `match-case`

## Possible Improvements

- Due dates and fines for late returns
- Edit book details and remove members
- Search by title or author
- Store data in a database (SQLite or PostgreSQL) instead of JSON

## Author
Mohammed. Ibrahim