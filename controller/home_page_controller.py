from PyQt5.QtWidgets import QMainWindow

from controller.roulette_controller import RouletteController
from controller.cleaning_time_table_controller import CleaningTimeTableController
from controller.meeting_time_table_controller import MeetingTimeTableController
from controller.school_time_table_controller import SchoolTimeTableController
from ui.home_page_ui import HomePageUI


class HomePageController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = HomePageUI()
        self.ui.setupUI(self)
        self.setInitUI()

    def setInitUI(self):
        self.roulette_window = RouletteController()
        self.cleaning_time_table_window = CleaningTimeTableController()
        self.meeting_time_table_window = MeetingTimeTableController()
        self.school_time_table_window = SchoolTimeTableController()

        self.ui.pushButton.clicked.connect(self.changeToRoulette)
        self.ui.pushButton_2.clicked.connect(self.changeToCleaningTimeTable)
        self.ui.pushButton_3.clicked.connect(self.changeToSchoolTimeTable)
        self.ui.pushButton_4.clicked.connect(self.changeToMeetingTimeTable)

    def changeToRoulette(self):
        self.roulette_window.backSignal.connect(self.show)
        self.hide()
        self.roulette_window.show()

    def changeToCleaningTimeTable(self):
        self.cleaning_time_table_window.backSignal.connect(self.show)
        self.hide()
        self.cleaning_time_table_window.show()

    def changeToMeetingTimeTable(self):
        self.meeting_time_table_window.backSignal.connect(self.show)
        self.hide()
        self.meeting_time_table_window.show()

    def changeToSchoolTimeTable(self):
        self.school_time_table_window.backSignal.connect(self.show)
        self.hide()
        self.school_time_table_window.show()
