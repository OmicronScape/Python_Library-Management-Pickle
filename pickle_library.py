#------>LIBRARY MANAGEMENT PROGRAM<----

# Import the pickle library for saving and loading objects from files.
import pickle  

# Definition of the Book class.
class Book:
    def __init__(self,title,author,year,rating):
        # Initialize the required attributes for each book.
        self.title = title   # Book title.
        self.author = author # Book author.
        self.year = year     # Book publication year.
        self.rating = rating # Book rating (1-10).
    
    def __str__(self):
        # Method to transform book information into a string.
        # Returns the book's information as a string.
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Rating: {self.rating}"

# Definition of the Library class.
class Library:
    # Method for creating a library.
    def __init__(self,filename):
         # Initialize the library.
         self.books = []             # List containing the books in the library.
         self.filename = filename    # Name of the pickle file for saving/loading.
         self.load_books()           # Load books from the file.
         self.menu()                 # Display the management menu.

    # Method load_books (Loads books from the pickle file.)
    def load_books(self):
        try:
            with  open(self.filename, 'rb') as file: # Open the file in binary read mode.
                self.books = pickle.load(file)       # Load the list of books from the file.
        except (FileNotFoundError, EOFError):
            # If the file is not found or is empty, create a new library.
            print("File not found or empty. Creating a new library.")
            self.books = []
        except Exception as e:
            # Handle different errors during reading.
            print(f"Error reading file: {e}")
    
    # Method save_books (Saves books to the pickle file.)
    def save_books(self):
        try:
              with open(self.filename, 'wb') as file:  # Open the file in binary write mode.
                pickle.dump(self.books, file)          # Save the list of books to the file.
        except Exception as e:
            # Handle errors during saving.
            print(f"Error saving file: {e}")
    
    # Method add_book (Adds a new book to the library.)
    def add_book(self):
        try:

            # Ask the user for book details.
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            year = int(input("Enter the book publication year: "))

            # Here we validate the publication year (between -2025 and 2025).
            if year < -2025 or year > 2025 or year == 0:
                 raise ValueError("The year must be between -2025 and 2025.")
            rating = float(input("Enter the book rating (1-10): "))
            
            # Here we validate the rating (between 1 and 10).
            if rating < 1 or rating > 10:
                raise ValueError("The rating must be between 1 and 10.")
            # Create a book object and add it to the list.
            book = Book(title, author, year, rating)
            self.books.append(book)
            print("Book added successfully!")
            
        except ValueError as e:
            # Handle input errors.
            print(f"Error: {e}")
            
    # Method display_books (Prints book details sorted by rating in descending order.)
    def display_books(self):
         # Sort books.
         sorted_books  = sorted(self.books, key=lambda b: b.rating, reverse=True)
         for book in sorted_books:
              print(book)  # Display each book.
    
    # Method Menu (Displays the library management menu.)  
    def menu(self):
         while True:
            print("\n|-----> Library <------|")
            print("1. Add book")
            print("2. Display sorted library")
            print("3. Exit")
            choice = input("Select an action: ")
                
            if choice == "1":
                self.add_book()  # Call method to add a book.
            elif choice == "2":
                self.display_books()  # Call method to display books.
            elif choice == "3":
                self.save_books()  # Save books before exiting.
                print("Terminating...")
                break  # Exit the program.
            else:
                # Message for invalid choice.
                print("Invalid choice. Please select again.")

#------->Program Start<-----
#(Create a Library object, passing the pickle file name as an argument.)
if __name__ == "__main__":
    Library("books.pkl")
