class Book:

    def __init__(self, book_ID , title , author , available):
        self.book_ID = book_ID
        self.title = title
        self.author = author
        self.available = available


    def display_books_details(self):
        print("Book Details : ")
        print(f"Book ID   : {self.book_ID}")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Available : {self.available}")

    def checks_Availability(self):
        if self.available:
            return "Available"
        else:
            return "Not Available"

    def Update_book_details(self , new_author , new_title):
        self.author = new_author
        self.title = new_title
        print("Updated sucessfully")

    def change_availability(self , New_Status):
        self.available = New_Status
        print("changed Availability")


class Members:

    def __init__(self , member_ID , member_name , Email):
        self.member_ID = member_ID
        self.member_name = member_name
        self.Email = Email
        self.borrowed_books = []


    def display_member_details(self):
        
        print("Member Details:")
        print(f"Member ID     : {self.member_ID}")
        print(f"Name          : {self.member_name}")
        print(f"Email     : {self.Email}")
        print(f"borrowedbooks : {len(self.borrowed_books)}")

       
    def display_borrowed_books(self):

        print(f"Member Name : {self.member_name}")
        print("Borrowed Books : ")

        if len(self.borrowed_books) == 0:
            print("NO books borrowed")

        else:
            for book in self.borrowed_books:
                print(f"Book_ID : {book.book_ID}")
                print(f"Title   : {book.title}")
                print(f"Author  : {book.author}")
                print("------------------------")

    def check_borrowed_book(self):

        if len(self.borrowed_books) == 0:
            return False

        return True

class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def display_all_books(self):

        if len(self.books) == 0:
            print("no books are available")
        else:
            print("Books : ")
            for book in self.books:
                print("--------------------------")
                print(f"Book_ID  : {book.book_ID}")
                print(f"Title    : {book.title}")
                print(f"Author   : {book.author}")
                print("--------------------------")

            print(f"Total Books : {len(self.books)}")


    def add_books(self , book):

        self.books.append(book)
        print("Added sucessfully")


    def search_book(self , book_id):

        for book in self.books:

            if book.book_ID == book_id:
                return book
        return None

    def search_member(self , member_id):

        for member in self.members:

            if member_id == member.member_ID:
                return member
        return None


    def remove_book(self , book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Book is not found")
        elif not book.available:
            print("Cannot remove. This book is currently borrowed")
        else:
            self.books.remove(book)
            print("Removed book successfuly")

    def register_member(self , member):

        exiting_member = self.search_member(member.member_ID)

        if exiting_member is not None:
            print("Member is already  Registered")
        else:
            self.member.append(member)
            print("Register successfully")


    #Most important method
    def issue_book(self , member_id , book_id):

        exiting_member = self.search_member(member_id)
        book_exit = self.search_book(book_id)

        if exiting_member is not None:

            if  book_exit is not None:

                if book_exit.available == True:

                    book_exit.available = False
                    exiting_member.borrowed_books.append(book_exit)
                    print("Book issue successfully")
                else:
                    print("Book is  already Borrowed")
            else:
                print("Book is not found")
        else:
            print("Member is not found")




        
book1 = Book(101 , "python basics" , "John" , True)
book2 = Book(102, "C language" , "Ibrahim" , True)
book3 = Book(103, "DBMS" , "Ibrahim" , True)
book4 = Book(104, "COA" , "Ibrahim" ,False)

BOOKS = []
BOOKS.append(book1)
BOOKS.append(book2)
BOOKS.append(book3)
BOOKS.append(book4)

member1 = Members(1 , 'ibrahim' , 'ibrahim@email.com')
member1.borrowed_books.append(book1)
member1.borrowed_books.append(book2)


Libr1 = Library()
Libr2 = Library()

Libr1.books.append(book1)
Libr1.books.append(book2)

Libr1.members.append(member1)


result = Libr1.search_book(101)

if result:
    result.display_books_details()
else:
    print("Book not found")