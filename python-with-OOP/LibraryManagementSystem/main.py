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

        with open("library.json", "r") as file:
            data = json.load(file)

        self.books = []
        self.members = []

        for book_data in data["books"]:

            book = Book(
                book_data["book_ID"],
                book_data["title"],
                book_data["author"],
                book_data["available"]
            )

            self.books.append(book)



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
                return

        self.books.append(book)
        print("Book added successfully")

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

        elif not book.available:
            print("Cannot remove. This book is currently borrowed")

        else:
            self.books.remove(book)
            print("Book removed successfully")

    def register_member(self, member):

        existing_member = self.search_member(member.member_ID)

        if existing_member is not None:
            print("Member is already registered")
            return

        self.members.append(member)
        print("Member registered successfully")

    # Issue Book
    def issue_book(self, member_id, book_id):

        existing_member = self.search_member(member_id)
        existing_book = self.search_book(book_id)

        if existing_member is None:
            print("Member not found")
            return

        if existing_book is None:
            print("Book not found")
            return

        if not existing_book.available:
            print("Book is already borrowed")
            return

        existing_book.available = False
        existing_member.borrowed_books.append(existing_book)

        print("Book issued successfully")


    def return_book(self, member_id, book_id):

        #Finding the member
        exiting_member = self.search_member(member_id)

        if exiting_member is None:
            print("Member is not register")
            return
        else:

            #Findin the book
            isBookexit = self.search_book(book_id)

            if isBookexit is None:
                print("Book does not exit")
                return
            else:

                #book and member both are exit
                if isBookexit in exiting_member.borrowed_books:
                    isBookexit.available = True
                    exiting_member.borrowed_books.remove(isBookexit)
                    print("Successfully book is return")
                    return
                else:
                    print("This member has not borrowed this book")
                    return

    def display_members(self):

        if len(self.members) == 0:
            print("NO member is registered empty")
        else:
            for member in self.members:
                print(f"Member_ID : ")


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

        with open("library.json", "w") as file:
            json.dump(Library_data, file, indent=4)

        print("Library data saved successfully")


# --------------------------------
# Sample Data
# --------------------------------

book1 = Book(101, "Python Basics", "John", True)
book2 = Book(102, "C Language", "Ibrahim", True)
book3 = Book(103, "DBMS", "Ibrahim", True)
book4 = Book(104, "COA", "Ibrahim", True)

member1 = Members(1, "Ibrahim", "ibrahim@email.com")

Libr1 = Library()

# Adding Books
Libr1.add_books(book1)
Libr1.add_books(book2)
Libr1.add_books(book3)
Libr1.add_books(book4)

# Registering Member
Libr1.register_member(member1)

# Issuing Books
Libr1.issue_book(1, 101)
Libr1.issue_book(1, 102)


# Searching Book
result = Libr1.search_book(101)

if result:
    result.display_books_details()
else:
    print("Book not found")

Libr1.save_data()