from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from ui.meeting_time_table_ui import MeetingTimeTableUI
from src.meeting_time_table import MeetingTimeTable


class MeetingTimeTableController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()
        self.setGeometry(100, 100, 950, 600)
        self.setWindowTitle("Meeting Time Table")

        self.meetingTimeTable = MeetingTimeTable(member)
        self.ui = MeetingTimeTableUI(self, self.meetingTimeTable.getmeeting_time())

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()


if __name__ == "__main__":
    import sys

    app = QMainWindow.QApplication(sys.argv)
    Form = QMainWindow()
    Form.show()
    sys.exit(app.exec_())
