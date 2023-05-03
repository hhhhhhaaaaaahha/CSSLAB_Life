import requests


class SchoolTimeTable:
    def __init__(self, member):
        self.member = member

    def getMemberClassTimeScedual(self, memberName):
        headers = {"member_id": self.member.token}

        return requests.post(
            "http://127.0.0.1:5000/course_get_time",
            headers=headers,
            data={"name": memberName},
        ).json()["time"]

    def getAllMembers(self):
        headers = {"member_id": self.member.token}
        return requests.post(
            "http://127.0.0.1:5000/course_get_members",
            headers=headers,
        ).json()["members"]

    # 未來新功能
    # def addMemberClassTimeScedual():
    # def setMemberClassTimeScedual():
