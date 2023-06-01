from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QLabel,
    QGraphicsDropShadowEffect,
    QApplication,
)

from ui.item_list_ui import ItemListUI, AddItemUI
from src.item_list import ItemList


class ItemListController(QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self, member):
        super().__init__()

        self.item_list = ItemList(member)
        self.member = member
        self.ui = ItemListUI(self)

        self.column = {0: "登記者：", 1: "日期：", 2: "物品名稱：", 3: "價錢：", 4: "理由："}

        # Init add item window
        self.add_item_ui = AddItemUI(self.column)
        self.add_item_ui.submit_button.clicked.connect(self.checkEvent)

        #
        self.item_id_list: list = self.item_list.getItemList()

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

        # Connect addbbtn with add item event
        self.ui.addbtn.clicked.connect(self.addItem)

        self.drawItemLabel()

    def addItem(self):
        self.add_item_ui.show()
        # self.item_list.addItem(self.member, [name, date, item_name, price, reason])

    def syncItemLabelList(self):
        self.item_id_list: list = self.item_list.getItemList()

    def drawItemLabel(self):
        self.ui.item_labels: list[QLabel] = []
        for index, item_id in enumerate(self.item_id_list):
            # Set shadow effect
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)

            # Create new label
            self.ui.item_labels.append(QLabel(self))

            # Format label
            self.ui.item_labels[-1].setStyleSheet(
                """
                background:#fff176;
                font-weight:bold;
                text-align:center;
                """
            )
            self.ui.item_labels[-1].setGraphicsEffect(shadow)
            self.ui.item_labels[-1].setFixedHeight(200)
            self.ui.item_labels[-1].setFixedWidth(200)
            self.ui.item_labels[-1].setAlignment(QtCore.Qt.AlignCenter)

            # Get item information
            info = self.item_list.getItemById(item_id)

            # Set text to label
            text = ""
            for i, string in enumerate(info):
                text += f"{self.column[i]}\t{string}\n"
            self.ui.item_labels[-1].setText(text)
            self.ui.item_labels[-1].move(50 + 230 * index, 70)
            self.ui.item_labels[-1].show()

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()

    def checkEvent(self):
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
            self.syncItemLabelList()
            self.drawItemLabel()

    def closeEvent(self, event):
        self.add_item_ui.close()
