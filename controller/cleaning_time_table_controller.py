from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from ui.cleaning_time_table_ui import CleaningTimeTableUI
from src.cleaning_time_table import CleaningTimeTable


class CleaningTimeTableController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()

        self.setGeometry(100, 100, 950, 1000)
        self.setWindowTitle("Cleaning Time Table")

        self.cleaningTimeTable = CleaningTimeTable(member)
        self.ui = CleaningTimeTableUI(
            self,
            self.cleaningTimeTable.getMembers(),
            self.cleaningTimeTable.getSemesterStartD(),
            self.cleaningTimeTable.getSemesterEndD(),
        )

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()
