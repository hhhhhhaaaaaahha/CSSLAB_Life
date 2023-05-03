import requests


class CleaningTimeTable:
    def __init__(self, member):
        self.member = member

    def getMembers(self):
        headers = {"member_id": self.member.token}

        return requests.post(
            "http://127.0.0.1:5000/cleaning_get_members", headers=headers
        ).json()["list"]

    def getSemesterStartD(self):
        headers = {"member_id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/cleaning_get_startD", headers=headers
        ).json()["startD"]

    def getSemesterEndD(self):
        headers = {"member_id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/cleaning_get_endD", headers=headers
        ).json()["endD"]
