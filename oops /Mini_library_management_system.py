# -------------------- Book Class --------------------

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def mark_as_issued(self):
        self.is_available = False

    def mark_as_returned(self):
        self.is_available = True


# -------------------- Member Class --------------------

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_limit = 3

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_limit

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


# -------------------- Library Class --------------------

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Book not found")
            return

        if not member:
            print("Member not found")
            return

        if not book.is_available:
            print("Book already issued")
            return

        if not member.can_borrow():
            print("Borrow limit reached")
            return

        member.borrow_book(book)
        book.mark_as_issued()
        print(f"Book '{book.title}' issued to {member.name}")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book or not member:
            print("Invalid book or member")
            return

        member.return_book(book)
        book.mark_as_returned()
        print(f"Book '{book.title}' returned successfully")


# -------------------- Usage Example --------------------

library = Library()

# Add books
book1 = Book(1, "Python Basics", "sidd")
book2 = Book(2, "OOP Design", "dhruv")

library.add_book(book1)
library.add_book(book2)

# Register member
member1 = Member(101, "Siddharth")
library.register_member(member1)

# Issue and return
library.issue_book(1, 101)
library.return_book(1, 101)