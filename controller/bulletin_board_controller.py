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

from ui.bulletin_board_ui import BulletinBoardUI, AddMessageUI

from src.bulletin_board import BulletinBoard


class BulletinBoardController(QMainWindow):
    backSignal = QtCore.pyqtSignal()
    pinned_signal = QtCore.pyqtSignal(str)

    def __init__(self, member):
        super().__init__()

        self.bulletin_board = BulletinBoard(member)
        self.ui = BulletinBoardUI(self)
        self.member = member

        self.column = {0: "發布人：", 1: "時間：", 2: "內容："}

        # Init add item window
        self.add_message_ui = AddMessageUI(self.column)
        self.add_message_ui.submit_button.clicked.connect(self.addMessageCheck)

        # Connect retbtn with return event
        self.ui.retbtn.clicked.connect(self.changeToHomePage)

        # Connect addbbtn with add item event
        self.ui.addbtn.clicked.connect(self.addMessageWindow)

        self.drawMessageLabel()

    def addMessageWindow(self):
        self.add_message_ui.show()

    def drawDeleteButton(self):
        temp = QPushButton(self)
        temp.setIcon(QIcon("./img/minus.png"))
        temp.setFixedWidth(50)
        temp.setFixedHeight(30)
        return temp

    def drawPinningButton(self, message_id):
        temp = QPushButton(self)
        temp.setFixedWidth(50)
        temp.setFixedHeight(30)
        if message_id != self.pinnedId:
            temp.setIcon(QIcon("./img/hollow_star.png"))
        else:
            temp.setIcon(QIcon("./img/solid_star.png"))
        return temp

    def drawMessageLabel(self):
        # Clear old message labels
        if len(self.ui.message_labels) != 0:
            for label, button, button2 in self.ui.message_labels:
                label.hide()
                button.hide()
                button2.hide()

        # Clear delete message function that connectedwith each delete button
        self.deleteMessageFuncs = []
        self.pinMessageFuncs = []

        self.pinnedId = self.bulletin_board.getPinnedId()

        for index, message_id in enumerate(self.bulletin_board.id_list):
            # Set shadow effect
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)

            # Create new label
            self.ui.message_labels.append(
                [
                    QLabel(self),
                    self.drawDeleteButton(),
                    self.drawPinningButton(message_id),
                ]
            )

            # Format label
            self.ui.message_labels[-1][0].setStyleSheet(
                """
                background:#fff176;
                font-weight:bold;
                text-align:center;
                """
            )
            self.ui.message_labels[-1][0].setGraphicsEffect(shadow)
            self.ui.message_labels[-1][0].setFixedHeight(200)
            self.ui.message_labels[-1][0].setFixedWidth(200)
            self.ui.message_labels[-1][0].setAlignment(QtCore.Qt.AlignCenter)

            # Get item information
            info = self.bulletin_board.getMessageById(message_id)

            # Set text to label
            text = ""
            for i, string in enumerate(info):
                if string != info[-1]:
                    text += f"{self.column[i]}\t{string}\n"
                else:
                    text += f"{self.column[i]}\t"
                    temp = list(string)
                    for i in range(len(string) // 8):
                        temp[(i + 1) * 8 - 1] += "\n\t"
                    text += "".join(temp)

            self.ui.message_labels[-1][0].setText(text)
            self.ui.message_labels[-1][0].move(
                50 + 245 * (index % 3), 70 + 245 * (index // 3)
            )

            # Config delete button
            self.deleteMessageFuncs.append(partial(self.deleteMessageCheck, message_id))
            self.ui.message_labels[-1][1].clicked.connect(self.deleteMessageFuncs[-1])
            self.ui.message_labels[-1][1].move(
                200 + 245 * (index % 3), 75 + 245 * (index // 3)
            )

            # Config pinning button
            self.pinMessageFuncs.append(partial(self.pinMessageCheck, message_id))
            self.ui.message_labels[-1][2].clicked.connect(self.pinMessageFuncs[-1])
            self.ui.message_labels[-1][2].move(
                160 + 245 * (index % 3), 75 + 245 * (index // 3)
            )

            # Show
            self.ui.message_labels[-1][0].show()
            self.ui.message_labels[-1][1].show()
            self.ui.message_labels[-1][2].show()

    def changeToHomePage(self):
        self.hide()
        self.backSignal.emit()

    def addMessageCheck(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("送出確認")
        box.setText("確定要新增留言嗎？")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.No)
        buttonY.setText("是")
        buttonN = box.button(QMessageBox.Yes)
        buttonN.setText("否")
        box.exec_()

        if box.clickedButton() == buttonY:
            req = ""
            for _, line_edit in self.add_message_ui.label_list:
                req += line_edit.text()
                req += ","
                line_edit.clear()
            self.add_message_ui.label_list[0][1].setFocus()

            # Send request to server
            self.bulletin_board.addMessage(req)

            # Update data and close add item window
            self.add_message_ui.hide()
            self.drawMessageLabel()

    def deleteMessageCheck(self, id: int):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("刪除確認")
        box.setText(f"確定要刪除這則由 {self.bulletin_board.getMessageById(id)[0]} 發出的公告嗎？")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.No)
        buttonY.setText("是")
        buttonN = box.button(QMessageBox.Yes)
        buttonN.setText("否")
        box.exec_()

        if box.clickedButton() == buttonY:
            self.deleteMessage(id)

    def pinMessageCheck(self, id: int):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("釘選確認")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.No)
        buttonY.setText("是")
        buttonN = box.button(QMessageBox.Yes)
        buttonN.setText("否")
        if id != self.pinnedId:
            box.setText(f"確定要釘選這則由 {self.bulletin_board.getMessageById(id)[0]} 發出的公告嗎？")
        else:
            box.setText(f"確定要取消釘選嗎？")
        box.exec_()

        if box.clickedButton() == buttonY:
            if id != self.pinnedId:
                self.pinMessage(id)
            else:
                self.pinMessage(-1)

    def deleteMessage(self, id: int):
        self.bulletin_board.deleteMessage(id)
        self.drawMessageLabel()

    def pinMessage(self, id: int):
        self.bulletin_board.setPinnedMessage(id)
        self.drawMessageLabel()
        if id == -1:
            self.pinned_signal.emit("remove")
        else:
            self.pinned_signal.emit("new")

    def closeEvent(self, event):
        self.add_message_ui.close()
