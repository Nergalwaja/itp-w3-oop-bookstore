class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books
    
    def search_books(self, author=None, title=None):
        # import pdb
        # pdb.set_trace()

        if author is None and title is None:
            return []
        elif author is None and title is not None:
            title_list = []
            for book in self.books: 
                if title.lower() in book.title.lower():
                    title_list.append(book)
            return title_list
        elif author is not None and title is None:
            author_list = []
            for book in self.books: 
                if author == book.author:
                    author_list.append(book)
            return author_list
        

    
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
