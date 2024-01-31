
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None  # Используем _pages для хранения значения

        self.pages = pages  # Используем свойство для установки значения

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    # Необязательно перегружать __str__ и __repr__, используем реализацию из базового класса


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None  # Используем _duration для хранения значения

        self.duration = duration  # Используем свойство для установки значения

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration must be a number.")
        if value <= 0:
            raise ValueError("Duration must be a positive number.")
        self._duration = value

    # Необязательно перегружать __str__ и __repr__, используем реализацию из базового класса


# Пример использования:
paper_book = PaperBook("The Catcher in the Rye", "J.D. Salinger", 224)
audio_book = AudioBook("1984", "George Orwell", 9.5)

print(paper_book)
print(audio_book)

# Пример сравнения str и repr
print(str(paper_book))
print(repr(audio_book))

