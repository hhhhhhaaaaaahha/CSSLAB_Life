from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from ui.item_list_ui import ItemListUI
from src.item_list import ItemList


class ItemListController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()

        self.item_list = ItemList(member)
        self.ui = ItemListUI(self)

        # Todo
        self.item_label_list = list()

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()
