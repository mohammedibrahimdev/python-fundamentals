import json


class Book:

    def __init__(self, book_ID, title, author, available):
        self.book_ID = book_ID
        self.title = title
        self.author = author
        self.available = available

    def display_books_details(self):
        print("Book Details:")
        print(f"Book ID   : {self.book_ID}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Available : {self.check_availability()}")

    def check_availability(self):
        if self.available:
            return "Available"
        return "Not Available"

    def update_book_details(self, new_author, new_title):
        self.author = new_author
        self.title = new_title
        print("Updated successfully")

    def change_availability(self, new_status):
        self.available = new_status
        print("Availability changed")


class Members:

    def __init__(self, member_ID, member_name, Email):
        self.member_ID = member_ID
        self.member_name = member_name
        self.Email = Email
        self.borrowed_books = []

    def display_member_details(self):
        print("Member Details:")
        print(f"Member ID       : {self.member_ID}")
        print(f"Name            : {self.member_name}")
        print(f"Email           : {self.Email}")
        print(f"Borrowed Books  : {len(self.borrowed_books)}")

    def display_borrowed_books(self):
        print(f"Member Name : {self.member_name}")
        print("Borrowed Books:")

        if not self.borrowed_books:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print(f"Book ID : {book.book_ID}")
                print(f"Title   : {book.title}")
                print(f"Author  : {book.author}")
                print("------------------------")

    def check_borrowed_book(self):
        if not self.borrowed_books:
            return False
        return True


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def load_data(self):
        try:
            with open("library.json", "r") as file:
                data = json.load(file)

            # Reconstruct Book objects
            loaded_books = []

            for book_data in data["books"]:
                book = Book(
                    book_data["book_ID"],
                    book_data["title"],
                    book_data["author"],
                    book_data["available"]
                )
                loaded_books.append(book)

            # Reconstruct Member objects
            loaded_members = []

            for member_data in data["members"]:
                member = Members(
                    member_data["member_ID"],
                    member_data["member_name"],
                    member_data["Email"]
                )
                loaded_members.append(member)

            # Restore borrowed-book relationships
            for member_data in data["members"]:
                for member in loaded_members:
                    if member.member_ID == member_data["member_ID"]:
                        for book_id in member_data["borrowed_books"]:
                            for book in loaded_books:
                                if book.book_ID == book_id:
                                    member.borrowed_books.append(book)
                        break

            # Replace current data after successful reconstruction
            self.books = loaded_books
            self.members = loaded_members

            print("Library data loaded successfully!")

        except FileNotFoundError:
            print("Library data file not found")

        except json.JSONDecodeError:
            print("Invalid JSON data")

        except KeyError as e:
            print(f"Required data is missing from JSON file: {e}")

        except TypeError:
            print("Invalid data format in JSON file")

    def display_all_books(self):

        if not self.books:
            print("No books are available")
        else:
            print("Books:")

            for book in self.books:
                print("--------------------------")
                print(f"Book ID  : {book.book_ID}")
                print(f"Title    : {book.title}")
                print(f"Author   : {book.author}")
                print(f"Available: {book.check_availability()}")
                print("--------------------------")

            print(f"Total Books : {len(self.books)}")

    def add_books(self, book):

        for existing_book in self.books:

            if book.book_ID == existing_book.book_ID:
                print("Book already exists")
                return False

        self.books.append(book)
        print("Book added successfully")
        return True

    def search_book(self, book_id):

        for book in self.books:

            if book.book_ID == book_id:
                return book

        return None

    def search_member(self, member_id):

        for member in self.members:

            if member.member_ID == member_id:
                return member

        return None

    def remove_book(self, book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Book not found")
            return False

        elif not book.available:
            print("Cannot remove. This book is currently borrowed")
            return False

        else:
            self.books.remove(book)
            print("Book removed successfully")
            return True

    def register_member(self, member):

        existing_member = self.search_member(member.member_ID)

        if existing_member is not None:
            print("Member is already registered")
            return False

        self.members.append(member)
        print("Member registered successfully")
        return True

    def display_members(self):

        if not self.members:
            print("No members registered")
        else:
            for member in self.members:
                member.display_member_details()
                print("------------------------")

    # Issue Book
    def issue_book(self, member_id, book_id):

        existing_member = self.search_member(member_id)
        existing_book = self.search_book(book_id)

        if existing_member is None:
            print("Member not found")
            return False

        if existing_book is None:
            print("Book not found")
            return False

        if not existing_book.available:
            print("Book is already borrowed")
            return False

        existing_book.available = False
        existing_member.borrowed_books.append(existing_book)

        print("Book issued successfully")
        return True

    def return_book(self, member_id, book_id):

        # Finding the member
        exiting_member = self.search_member(member_id)

        if exiting_member is None:
            print("Member is not registered")
            return False

        # Finding the book
        isBookexit = self.search_book(book_id)

        if isBookexit is None:
            print("Book does not exist")
            return False

        # Checking whether this member borrowed this book
        if isBookexit in exiting_member.borrowed_books:
            isBookexit.available = True
            exiting_member.borrowed_books.remove(isBookexit)
            print("Book returned successfully")
            return True
        else:
            print("This member has not borrowed this book")
            return False

    def save_data(self):

        books_data = []

        for book in self.books:

            book_dict = {
                "book_ID": book.book_ID,
                "title": book.title,
                "author": book.author,
                "available": book.available
            }

            books_data.append(book_dict)

        members_data = []

        for member in self.members:

            member_dict = {
                "member_ID": member.member_ID,
                "member_name": member.member_name,
                "Email": member.Email,
                "borrowed_books": [book.book_ID for book in member.borrowed_books]
            }

            members_data.append(member_dict)

        Library_data = {
            "books": books_data,
            "members": members_data
        }

        try:
            with open("library.json", "w") as file:
                json.dump(Library_data, file, indent=4)

            print("Library data saved successfully")

        except OSError as e:
            print(f"Unable to save library data: {e}")


# --------------------------------
# Main Interface
# --------------------------------

Libr1 = Library()

# Load existing data
Libr1.load_data()

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

    print("1.  Display All Books")
    print("2.  Add Book")
    print("3.  Search Book")
    print("4.  Remove Book")
    print("5.  Register Member")
    print("6.  Display All Members")
    print("7.  Issue Book")
    print("8.  Return Book")
    print("9.  Display Borrowed Books")
    print("10. Save Data")
    print("0.  Exit")

    print("================================================")

    choice = input("Enter your choice: ").strip()

    match choice:

        case "1":
            Libr1.display_all_books()

        case "2":
            print("\n--- Add New Book ---")

            try:
                book_ID = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            title = input("Enter Book Title: ").strip()
            if not title or title.isdigit():
                print("Invalid title! Title cannot be empty or only numbers.")
                continue

            author = input("Enter Author Name: ").strip()
            if not author or author.isdigit():
                print("Invalid author! Author cannot be empty or only numbers.")
                continue

            book = Book(book_ID, title, author, True)

            if Libr1.add_books(book):
                Libr1.save_data()

        case "3":
            try:
                book_ID = int(input("Enter Book ID to search: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            book = Libr1.search_book(book_ID)

            if book is not None:
                book.display_books_details()
            else:
                print("Book not found")

        case "4":
            try:
                book_ID = int(input("Enter Book ID to remove: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if Libr1.remove_book(book_ID):
                Libr1.save_data()

        case "5":
            print("\n--- Register New Member ---")

            try:
                member_ID = int(input("Enter Member ID: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            member_name = input("Enter Member Name: ").strip()
            if not member_name or member_name.isdigit():
                print("Invalid member name! Please enter a valid name.")
                continue

            Email = input("Enter Email: ").strip()
            if not Email:
                print("Email cannot be empty.")
                continue

            member = Members(member_ID, member_name, Email)

            if Libr1.register_member(member):
                Libr1.save_data()

        case "6":
            Libr1.display_members()

        case "7":
            try:
                member_ID = int(input("Enter Member ID: "))
                book_ID = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if Libr1.issue_book(member_ID, book_ID):
                Libr1.save_data()

        case "8":
            try:
                member_ID = int(input("Enter Member ID: "))
                book_ID = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if Libr1.return_book(member_ID, book_ID):
                Libr1.save_data()

        case "9":
            try:
                member_ID = int(input("Enter Member ID: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            member = Libr1.search_member(member_ID)

            if member is not None:
                member.display_borrowed_books()
            else:
                print("Member not found")

        case "10":
            Libr1.save_data()

        case "0":
            Libr1.save_data()
            print("Thank you for using Library Management System!")
            break

        case _:
            print("Invalid choice. Please try again.")
