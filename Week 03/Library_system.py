class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(f"Book '{self.title}' issued successfully!")
        else:
            print(f"Book '{self.title}' is already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(f"Book '{self.title}' returned successfully!")
        else:
            print(f"Book '{self.title}' was not issued.")

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} by {self.author} - {status}"



b1 = Book("Python Basics", "Harry")
print(b1)
b1.issue()
print(b1)
b1.return_book()
print(b1)
