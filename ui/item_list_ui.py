from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont


class ItemListUI:
    def __init__(self, window: QtWidgets.QMainWindow):
        window.setGeometry(0, 0, 800, 600)
        window.setWindowTitle("Item List")

        self.retbtn = QtWidgets.QPushButton(window)
        self.retbtn.setText("返回首頁")
        self.retbtn.move(10, 10)
