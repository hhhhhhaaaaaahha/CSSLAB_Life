from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from ui.school_time_table_ui import ShoolTimeTableUI
from src.school_time_table import SchoolTimeTable


class SchoolTimeTableController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()

        self.setGeometry(100, 100, 850, 850)
        self.setWindowTitle("School Time Table")

        self.schoolTimeTable = SchoolTimeTable(member)
        self.ui = ShoolTimeTableUI(self)

        # ComboBox lisener
        self.ui.setComboBoxLisener(self.changeClassTimeScedualLissener)

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

        # initail 顯示yuko課表
        self.ui.initailize(
            self.schoolTimeTable.getAllMembers(),
            self.schoolTimeTable.getMemberClassTimeScedual("子瑩"),
        )

    def changeClassTimeScedualLissener(self):
        name = self.ui.ComboBoxGetter()
        self.ui.change(self.schoolTimeTable.getMemberClassTimeScedual(name))

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()
