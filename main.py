class Book:
  def __init__(self, id, name, pages):
    self.id = id
    self.name = name
    self.pages = pages


    def __str__(self):
        return f"Book: {self.name}"

    def __repr__(self):
        return f"Book({self.id}, '{self.name}', {self.pages})"
      
class Library:
    def __init__(self, books=[]):
      self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        return None

if __name__ == "__main__":
  book1 = Book(1, "Python Programming", 300)
  book2 = Book(2, "Data Science Essentials", 250)

  library = Library([book1, book2])

  print(library.get_next_book_id())  # Output: 3
  print(library.get_index_by_book_id(2))  # Output: 1
