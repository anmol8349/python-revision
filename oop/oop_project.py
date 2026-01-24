import json
from datetime import datetime

# ----------------- BOOK CLASS -----------------
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.issued = 0

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
            "issued": self.issued
        }

    @staticmethod
    def from_dict(data):
        b = Book(data["book_id"], data["title"], data["author"], data["copies"])
        b.issued = data["issued"]
        return b

    def display(self):
        print(f"{self.book_id} | {self.title} | {self.author} | Available: {self.copies - self.issued}")


# ----------------- FILE MANAGER -----------------
class FileManager:
    FILE = "library.json"

    @staticmethod
    def save(library):
        data = [b.to_dict() for b in library.books]
        with open(FileManager.FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load():
        try:
            with open(FileManager.FILE, "r") as f:
                data = json.load(f)
                return [Book.from_dict(b) for b in data]
        except FileNotFoundError:
            return []


# ----------------- USER CLASSES -----------------
class User:
    def __init__(self, username):
        self.username = username

    def role(self):
        return "User"


class Admin(User):
    def role(self):
        return "Admin"


class Member(User):
    def role(self):
        return "Member"


# ----------------- LIBRARY CLASS -----------------
class Library:
    def __init__(self):
        self.books = FileManager.load()

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("\nID | Title | Author | Available")
        print("-" * 40)
        for b in self.books:
            b.display()

    def search_book(self, keyword):
        found = False
        for b in self.books:
            if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower():
                b.display()
                found = True
        if not found:
            print("No matching books found.")

    def issue_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if b.issued < b.copies:
                    b.issued += 1
                    print("Book issued successfully.")
                    return
                else:
                    print("No copies available.")
                    return
        print("Book not found.")

    def return_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if b.issued > 0:
                    b.issued -= 1
                    print("Book returned successfully.")
                    return
                else:
                    print("No book is currently issued.")
                    return
        print("Book not found.")

    def delete_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                self.books.remove(b)
                print("Book deleted.")
                return
        print("Book not found.")







# ----------------- MAIN APP -----------------
class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.current_user = None

    def login(self):
        username = input("Enter username: ").strip()
        role = input("Enter role (admin/member): ").strip().lower()

        if role == "admin":
            self.current_user = Admin(username)
        else:
            self.current_user = Member(username)

        print(f"Logged in as {self.current_user.username} ({self.current_user.role()})")

    def menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book (Admin only)")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Delete Book (Admin only)")
            print("7. Save & Exit")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    if not isinstance(self.current_user, Admin):
                        print("Access denied.")
                        continue

                    book_id = int(input("Book ID: "))
                    title = input("Title: ")
                    author = input("Author: ")
                    copies = int(input("Total Copies: "))
                    self.library.add_book(Book(book_id, title, author, copies))

                elif choice == "2":
                    self.library.view_books()

                elif choice == "3":
                    keyword = input("Enter title or author: ")
                    self.library.search_book(keyword)

                elif choice == "4":
                    book_id = int(input("Enter Book ID: "))
                    self.library.issue_book(book_id)

                elif choice == "5":
                    book_id = int(input("Enter Book ID: "))
                    self.library.return_book(book_id)

                elif choice == "6":
                    if not isinstance(self.current_user, Admin):
                        print("Access denied.")
                        continue
                    book_id = int(input("Enter Book ID: "))
                    self.library.delete_book(book_id)

                elif choice == "7":
                    FileManager.save(self.library)
                    print("Data saved. Exiting...")
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input. Please enter numbers correctly.")


# ----------------- RUN APP -----------------
app = LibraryApp()
app.login()
app.menu()
