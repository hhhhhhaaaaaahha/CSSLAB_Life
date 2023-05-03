import requests


class Roulette:
    def __init__(self, member):
        self.restaurant_list_cached: list[str] = []
        self.member = member

    def addRestaurant(self, name: str):
        headers = {"member_id": self.member.token}
        requests.post(
            "http://127.0.0.1:5000/add_restraunt", data={"name": name}, headers=headers
        )
        self.getRestaurantList()

    def clearRestaurantList(self):
        headers = {"member_id": self.member.token}
        requests.post("http://127.0.0.1:5000/clear_restraunt", headers=headers)
        self.getRestaurantList()

    def getRestaurant(self, index: int) -> str:
        # headers = {"member_id": self.member.token}
        # requests.post(
        #     "http://127.0.0.1:5000/get_restraunt",
        #     data={"index": index},
        #     headers=headers,
        # ).json()["name"]
        return self.restaurant_list_cached[index]

    def getRestaurantCount(self) -> int:
        # headers = {"member_id": self.member.token}
        # requests.post(
        #     "http://127.0.0.1:5000/get_restraunt_count", headers=headers
        # ).json()["count"]
        return len(self.restaurant_list_cached)

    def getRestaurantList(self) -> list:
        headers = {"member_id": self.member.token}
        self.restaurant_list_cached = requests.post(
            "http://127.0.0.1:5000/get_restraunt_list", headers=headers
        ).json()["list"]
        return self.restaurant_list_cached
