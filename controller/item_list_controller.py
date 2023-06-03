from functools import partial
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QLabel,
    QGraphicsDropShadowEffect,
    QPushButton,
)

from ui.item_list_ui import ItemListUI, AddItemUI
from src.item_list import ItemList


class ItemListController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()

        self.item_list = ItemList(member)
        self.ui = ItemListUI(self)
        self.member = member

        # Define item information columns
        self.column = {0: "登記者：", 1: "日期：", 2: "物品名稱：", 3: "價錢：", 4: "理由："}

        # Init add item window
        self.add_item_ui = AddItemUI(self.column)
        self.add_item_ui.submit_button.clicked.connect(self.addItemCheck)

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

        # Connect addbbtn with add item event
        self.ui.addbtn.clicked.connect(self.addItemWindow)

        # Setup item labels
        self.drawItemLabel()

    def addItemWindow(self):
        self.add_item_ui.show()

    def drawDeleteButton(self):
        temp = QPushButton(self)
        temp.setIcon(QIcon("./img/minus.png"))
        temp.setFixedWidth(50)
        temp.setFixedHeight(30)
        return temp

    def drawItemLabel(self):
        # Clear old item labels
        if len(self.ui.item_labels) != 0:
            for label, button in self.ui.item_labels:
                label.hide()
                button.hide()

        # Clear delete item function that connectedwith each delete button
        self.deleteItemFuncs = []

        for index, item_id in enumerate(self.item_list.id_list):
            print(item_id)
            # Set shadow effect
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)

            # Create new label
            self.ui.item_labels.append([QLabel(self), self.drawDeleteButton()])

            # Format label
            self.ui.item_labels[-1][0].setStyleSheet(
                """
                background:#fff176;
                font-weight:bold;
                text-align:center;
                """
            )
            self.ui.item_labels[-1][0].setGraphicsEffect(shadow)
            self.ui.item_labels[-1][0].setFixedHeight(200)
            self.ui.item_labels[-1][0].setFixedWidth(200)
            self.ui.item_labels[-1][0].setAlignment(QtCore.Qt.AlignCenter)

            # Get item information
            info = self.item_list.getItemById(item_id)

            # Set text to label
            text = ""
            for i, string in enumerate(info):
                text += f"{self.column[i]}\t{string}\n"
            self.ui.item_labels[-1][0].setText(text)
            self.ui.item_labels[-1][0].move(
                50 + 245 * (index % 3), 70 + 245 * (index // 3)
            )

            # Config delete button
            self.deleteItemFuncs.append(partial(self.deleteItemCheck, item_id))
            self.ui.item_labels[-1][1].clicked.connect(self.deleteItemFuncs[-1])
            self.ui.item_labels[-1][1].move(
                200 + 245 * (index % 3), 75 + 245 * (index // 3)
            )

            # Show
            self.ui.item_labels[-1][0].show()
            self.ui.item_labels[-1][1].show()
        print("\n")

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()

    def addItemCheck(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("送出確認")
        box.setText("確定要新增物品嗎？")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.No)
        buttonY.setText("是")
        buttonN = box.button(QMessageBox.Yes)
        buttonN.setText("否")
        box.exec_()

        if box.clickedButton() == buttonY:
            req = ""
            for _, line_edit in self.add_item_ui.label_list:
                req += line_edit.text()
                req += ","
                line_edit.clear()
            self.add_item_ui.label_list[0][1].setFocus()

            # Send request to server
            self.item_list.addItem(req)

            # Update data and close add item window
            self.add_item_ui.hide()
            self.drawItemLabel()

    def deleteItemCheck(self, id: int):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("刪除確認")
        box.setText(f"確定要刪除 {self.item_list.getItemById(id)[0]} 嗎？")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.No)
        buttonY.setText("是")
        buttonN = box.button(QMessageBox.Yes)
        buttonN.setText("否")
        box.exec_()

        if box.clickedButton() == buttonY:
            self.deleteItem(id)

    def deleteItem(self, id: int):
        self.item_list.deleteItem(id)
        self.drawItemLabel()

    def closeEvent(self, event):
        self.add_item_ui.close()
