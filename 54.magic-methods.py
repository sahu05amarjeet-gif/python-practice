class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} {self.pages}"
    
    def __eq__(self, others):
        return self.title == others.title and self.author == others.author
    def __lt__(self, others):
        return self.pages < others.pages
    def __gt__(self, others):
        return self.pages > others.pages
    def __add__(self, others):
        return self.pages + others.pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title" or key == "author":
            return self.author

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Jungle Book", "C.S. Lewis", 172)

print(book2['author'])