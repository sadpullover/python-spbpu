import doctest


class Car:
    def init(self, brand: str, model: str, year: int):
        """
            Создает объект класса Car.
            :param brand: марка автомобиля
            :type brand: str
            :param model: модель автомобиля
            :type model: str
            :param year: год выпуска автомобиля
            :type year: int
        """
        pass

    def start_engine(self):
        """
            Запускает двигатель автомобиля.
        """
        pass

    def drive(self, destination: str) -> None:
        """
            Осуществляет поездку до указанного места.

            :param destination: пункт назначения
            :type destination: str
            :return: сообщение о завершении поездки
            :rtype: str
        """
        pass

    def refuel(self, amount: int):
        """
            Заправляет автомобиль указанным количеством топлива.

            :param amount: количество топлива для заправки
            :type amount: int
        """
        pass

class Animal:
    def init(self, species: str, name: str, age: int):
        """
            Создает объект класса Animal.
            :param species: вид животного
            :type species: str
            :param name: кличка животного
            :type name: str
            :param age: возраст животного
            :type age: int
        """
        pass

    def make_sound(self):
        """
            Издает звук, характерный для данного животного.
        """
        pass

    def move(self, destination: str) -> None:
        """
            Передвигается до указанного места.

            :param destination: пункт назначения
            :type destination: str
            :return: сообщение о завершении передвижения
            :rtype: str
        """
    pass

    def feed(self, food_type: str):
        """
            Кормит животное указанным типом еды.

            :param food_type: тип корма
            :type food_type: str
        """
    pass

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации