from PyQt5.QtWidgets import QLabel


class Roulette:
    def __init__(self):
        self.restaurant_list: list[str] = []

    def addRestaurant(self, name: str):
        self.restaurant_list.append(name)

    def delRestaurant(self, index: int):
        self.restaurant_list.pop(index)

    def getRestaurant(self, index: int) -> str:
        return self.restaurant_list[index]

    def getRestaurantList(self) -> list:
        return self.restaurant_list

    def getRestaurantCount(self) -> int:
        return len(self.restaurant_list)
