import requests


class ItemList:
    def __init__(self, member):
        self.member = member
        self.id_list = self.getItemList()

    def addItem(self, information: list):
        headers = {"member_id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/item_list_add_item",
            data={"information": information},
            headers=headers,
        ).json()["list"]

    def deleteItem(self, id: int):
        headers = {"member_id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/item_list_delete_item",
            data={"id": id},
            headers=headers,
        ).json()["list"]

    def getItemList(self):
        headers = {"member_id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/item_list_get_list",
            headers=headers,
        ).json()["list"]
