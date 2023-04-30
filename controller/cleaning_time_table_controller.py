from PyQt5.QtWidgets import QMainWindow
from ui.cleaning_time_table_ui import CleaningTimeTableUI
from src.cleaning_time_table import CleaningTimeTable

class CleaningTimeTableController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 950, 1000)
        self.setWindowTitle("Cleaning Time Table")

        self.cleaningTimeTable = CleaningTimeTable()
        self.ui = CleaningTimeTableUI(self, self.cleaningTimeTable.getMembers(), self.cleaningTimeTable.getSemesterStartD(), self.cleaningTimeTable.getSemesterEndD())