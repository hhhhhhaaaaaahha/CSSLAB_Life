from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel, QLineEdit


class BulletinBoardUI:
    def __init__(self, window: QtWidgets.QMainWindow):
        window.setGeometry(0, 0, 800, 600)
        window.setWindowTitle("Message List")

        self.retbtn = QtWidgets.QPushButton(window)
        self.retbtn.setText("返回首頁")
        self.retbtn.move(10, 10)

        self.addbtn = QtWidgets.QPushButton(window)
        self.addbtn.setIcon(QIcon("./img/plus.png"))
        self.addbtn.move(120, 10)

        self.message_labels: list[QLabel, QtWidgets.QPushButton] = list()

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)


class AddMessageUI(QtWidgets.QMainWindow):
    def __init__(self, column):
        super().__init__()
        self.setGeometry(500, 150, 320, 250)
        self.setWindowTitle("Add New Item")

        self.label_list = [(QLabel(self), QLineEdit(self)) for _ in range(3)]
        for index, row in enumerate(self.label_list):
            row[0].setText(column[index])
            row[0].move(50, 50 + 30 * index)
            row[1].setFixedWidth(130)
            row[1].setFixedHeight(23)
            row[1].move(120, 55 + 30 * index)

        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("送出")
        self.submit_button.move(105, 215)
