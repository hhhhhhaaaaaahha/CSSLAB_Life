from PyQt5.QtWidgets import QApplication, QMainWindow

from controller.roulette_controller import RouletteController
from controller.bulletin_board_controller import BulletinBoardController
from controller.cleaning_time_table_controller import CleaningTimeTableController
from controller.item_list_controller import ItemListController
from controller.meeting_time_table_controller import MeetingTimeTableController
from controller.school_time_table_controller import SchoolTimeTableController
from ui.home_page_ui import HomePageUI
from src.member import Member


class HomePageController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = HomePageUI()
        self.member = Member()
        self.ui.setupUI(self)
        self.setInitUI()

    def setInitUI(self):
        self.roulette_window = RouletteController(self.member)
        self.bulletin_board_window = BulletinBoardController(self.member)
        self.cleaning_time_table_window = CleaningTimeTableController(self.member)
        self.meeting_time_table_window = MeetingTimeTableController(self.member)
        self.school_time_table_window = SchoolTimeTableController(self.member)
        self.item_list_window = ItemListController(self.member)

        self.bulletin_board_window.pinned_signal.connect(self.announcementInfo)

        if self.bulletin_board_window.pinned_id == -1:
            self.ui.annnouncement_label.setText("目前無釘選公告")
        else:
            text = self.bulletin_board_window.bulletin_board.getAnnouncementById(
                self.bulletin_board_window.pinned_id
            )[2]
            self.ui.annnouncement_label.setText(text)

        self.ui.pushButton.clicked.connect(self.changeToRoulette)
        self.ui.pushButton_2.clicked.connect(self.changeToCleaningTimeTable)
        self.ui.pushButton_3.clicked.connect(self.changeToSchoolTimeTable)
        self.ui.pushButton_4.clicked.connect(self.changeToMeetingTimeTable)
        self.ui.pushButton_5.clicked.connect(self.changeToItemListTable)
        self.ui.pushButton_6.clicked.connect(self.changeToBulletinBoard)

    def changeToRoulette(self):
        self.roulette_window.backSignal.connect(self.show)
        self.hide()
        self.roulette_window.show()
        self.roulette_window.mModified = True
        self.roulette_window.update()

    def changeToBulletinBoard(self):
        self.bulletin_board_window.backSignal.connect(self.show)
        self.hide()
        self.bulletin_board_window.show()

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

    def changeToItemListTable(self):
        self.item_list_window.backSignal.connect(self.show)
        self.hide()
        self.item_list_window.show()

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()

    def announcementInfo(self, info):
        print(info)
        if info == "new":
            text = self.bulletin_board_window.bulletin_board.getAnnouncementById(
                self.bulletin_board_window.pinned_id
            )[2]
            self.ui.annnouncement_label.setText(text)
        else:
            self.ui.annnouncement_label.setText("目前無釘選公告")
