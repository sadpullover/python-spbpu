from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO заменить на метод
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

#  TODO создать метод, который будет инициализировать атрибут capacity_volume
    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        self.capacity_volume = capacity_volume

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError


if __name__ == "__main__":
    glass_instance = Glass(200, 100)
    # TODO инициализировать экземпляр класса Glass
    print(glass_instance.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(glass_instance.occupied_volume)  # TODO распечатать атрибут occupied_volume
