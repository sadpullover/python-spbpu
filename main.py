import doctest


class Animal:
  def __init__(self, name: str, age: int):
      """
      Конструктор базового класса Animal.

      :param name: Имя животного
      :param age: Возраст животного
      """
      self.name = name
      self.age = age

  def __str__(self) -> str:
      """
      Метод для представления объекта в виде строки.

      :return: Строковое представление объекта
      """
      return f"{self.name} is {self.age} years old"

  def __repr__(self) -> str:
      """
      Метод для представления объекта в виде строки для отладки.

      :return: Строковое представление объекта
      """
      return f"Animal('{self.name}', {self.age})"


class Dog(Animal):
  def __init__(self, name: str, age: int, breed: str):
      """
      Конструктор дочернего класса Dog. Расширяет конструктор базового класса Animal.

      :param name: Имя собаки
      :param age: Возраст собаки
      :param breed: Порода собаки
      """
      super().__init__(name, age)
      self.breed = breed

  def make_sound(self) -> str:
      """
      Метод для издания звука. Перегружает метод базового класса Animal.

      :return: Звук, издаваемый собакой
      """
      return f"{self.name} barks"

  def __str__(self) -> str:
      """
      Метод для представления объекта в виде строки. Унаследован из базового класса.

      :return: Строковое представление объекта
      """
      return f"{self.name} the {self.breed} is {self.age} years old"

  def __repr__(self) -> str:
      """
      Метод для представления объекта в виде строки для отладки. Унаследован из базового класса.

      :return: Строковое представление объекта
      """
      return f"Dog('{self.name}', {self.age}, '{self.breed}')"

  if __name__ == "__main__":
      doctest.testmod()