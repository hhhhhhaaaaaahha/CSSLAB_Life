import requests


class ItemList:
    def __init__(self, member):
        self.member = member
        self.id_list = self.getItemList()

    # Send add item request to server and sync id_list afterward
    def addItem(self, information: str):
        headers = {"Member-Id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/item_list_add_item",
            data={"information": information},
            headers=headers,
        ).json()["list"]

    # Send delete item request to server and sync id_list afterward
    def deleteItem(self, id: int):
        headers = {"Member-Id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/item_list_delete_item",
            data={"id": id},
            headers=headers,
        ).json()["list"]

    # Request item info by providing item id
    def getItemById(self, id: int):
        headers = {"Member-Id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/item_list_get_item",
            data={"id": id},
            headers=headers,
        ).json()["info"]

    # Sync item_list with server
    def getItemList(self):
        headers = {"Member-Id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/item_list_get_list",
            headers=headers,
        ).json()["list"]
