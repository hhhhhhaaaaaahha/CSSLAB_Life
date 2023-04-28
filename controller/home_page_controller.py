from PyQt5.QtWidgets import QMainWindow

from controller.roulette_controller import RouletteController
from ui.home_page_ui import HomePageUI


class HomePageController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = HomePageUI()
        self.ui.setupUI(self)
        self.setInitUI()

    def setInitUI(self):
        self.roulette_window = RouletteController()
        self.ui.pushButton.clicked.connect(self.changeToRoulette)
        # self.ui.pushButton_2.clicked.connect(self.changeWindow)
        # self.ui.pushButton_3.clicked.connect(self.changeWindow)
        # self.ui.pushButton_4.clicked.connect(self.changeWindow)

    def changeToRoulette(self):
        self.close()
        self.roulette_window.show()
