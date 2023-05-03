import requests


class MeetingTimeTable:
    def __init__(self, member):
        self.member = member

    def getmeeting_time(self):
        headers = {"member_id": self.member.token}

        return requests.post(
            "http://127.0.0.1:5000/meeting_get_time", headers=headers
        ).json()["time"]
