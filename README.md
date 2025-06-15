# Python_Library-Management-Pickle
A Python library management system using pickle for data storage.


Library Management System

This is a simple Python-based Library Management System that helps you keep track of your books. It allows you to add new books, view your collection, and saves all your data automatically.
What It Does

This program lets you:

    Add New Books: Easily input details like the title, author, publication year, and your personal rating (from 1 to 10) for each book.
    View Your Library: See all your added books, neatly sorted from the highest-rated to the lowest-rated.
    Save & Load Data: All your book information is automatically saved to a file and loaded back when you start the program, so you never lose your data.

How to Use It

    Save the code: Save the provided Python code into a file named library_manager.py on your computer.
    Run the program:
        Open your terminal or command prompt.
        Navigate to the folder where you saved library_manager.py.
        Run the command: python library_manager.py
    Follow the menu: Once the program starts, you'll see a simple menu:
        1. Add book: Choose this to add a new book and enter its details when prompted.
        2. Display sorted library: Select this to see all your books, ordered by their rating.
        3. Exit: Choose this to close the program. Your data will be saved automatically.

Technical Details (For Developers)

This project uses Python's built-in pickle module to store and retrieve book objects. This means your book data is saved in a binary file (named books.pkl by default), making it easy to persist your information between sessions.

    Book Class: Represents an individual book with attributes like title, author, year, and rating.
    Library Class: Manages the collection of Book objects. It handles loading from and saving to the books.pkl file, and provides methods for adding and displaying books.

Getting Started (Quick Steps)

    Make sure you have Python 3 installed on your system.
    Download the library_manager.py file.
    Run python library_manager.py in your terminal.
    Start managing your book collection!
