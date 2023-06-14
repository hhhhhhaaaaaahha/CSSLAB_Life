import requests


class BulletinBoard:
    def __init__(self, member):
        self.member = member
        self.id_list = self.getMessageList()

    # Send add message request to server and sync id_list afterward
    def addMessage(self, information: str):
        headers = {"Member-id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/bb_list_add_announcement",
            data={"information": information},
            headers=headers,
        ).json()["list"]

    # Send delete message request to server and sync id_list afterward
    def deleteMessage(self, id: int):
        headers = {"Member-id": self.member.token}
        self.id_list = requests.post(
            "http://127.0.0.1:5000/bb_list_delete_announcement",
            data={"id": id},
            headers=headers,
        ).json()["list"]

    # Request message info by providing message id
    def getMessageById(self, id: int):
        headers = {"Member-id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/bb_list_get_announcement",
            data={"id": id},
            headers=headers,
        ).json()["info"]

    # Sync message_list with server
    def getMessageList(self):
        headers = {"Member-id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/bb_list_get_list",
            headers=headers,
        ).json()["list"]

    def getPinnedId(self):
        headers = {"Member-id": self.member.token}
        return int(
            requests.post(
                "http://127.0.0.1:5000/bb_list_get_pinned_id",
                headers=headers,
            ).json()["id"]
        )

    def setPinnedMessage(self, id: int):
        headers = {"Member-id": self.member.token}
        requests.post(
            "http://127.0.0.1:5000/bb_list_pin_announcement",
            data={"id": id},
            headers=headers,
        )
