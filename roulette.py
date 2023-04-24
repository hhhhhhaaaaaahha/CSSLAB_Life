from PyQt5.QtCore import Qt, QPoint, QRectF, QTimer
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QFont,
    QIcon,
    QPainter,
    QPen,
    QPixmap,
    QPolygon,
)
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QToolBar,
    QWidget,
)
import math
import numpy as np
import random
import sys


class Roulette(QWidget):
    def __init__(self):
        super().__init__()

        # Set window
        self.mModified = True
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Roulette")
        gridlayout = QGridLayout()

        # Define the colors for pie
        self.colors = [
            QColor(195, 166, 211),
            QColor(215, 183, 232),
            QColor(237, 201, 255),
            QColor(246, 207, 243),
            QColor(254, 212, 231),
            QColor(248, 198, 195),
            QColor(242, 183, 159),
            QColor(236, 183, 132),
            QColor(229, 183, 105),
            QColor(223, 194, 79),
            QColor(220, 199, 66),
            QColor(216, 204, 52),
            QColor(220, 209, 70),
        ]
        random.shuffle(self.colors)

        # spin-related variables
        self.angle = 0
        self.decrease_angle = 0
        self.counter = 1000000
        self.spin_time = 100000
        self.spin_angle = 30
        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimer)

        # text-related variables
        self.text_radius = 150
        self.central_point = QPoint(192, 208)

        # Add spin button
        self.spin_button = QPushButton("Spin", self)
        self.spin_button.clicked.connect(self.startTimer)

        ## Option-related
        # Init option text field

        # self.add_option_icon = QLabel(self)
        # self.add_option_icon.setPixmap(
        #     QPixmap("img/21a921f165298b0110b80821cc5bd761.svg").scaled(25, 25)
        # )
        # self.add_option_icon.setPixmap(QPixmap("./img/add_button.png").scaled(25, 25))
        # self.add_option_icon.move(500, 8)
        self.options: list[QLabel] = []

        self.text_field = QLineEdit(self)
        self.text_field.move(535, 10)

        # Init submit button
        self.submit_button = QPushButton("新增", self)
        self.submit_button.clicked.connect(self.addOption)
        self.submit_button.move(670, 5)
        # icon = QIcon("img/add_button.png")
        # self.submit_button.setIcon(icon)

    def paintEvent(self, event):
        if self.mModified:
            qp = QPainter()
            qp.begin(self)
            self.drawRoulette(qp)
            self.mModified = False

    def drawRoulette(self, qp: QPainter):
        pen = QPen(
            QColor(0, 0, 0),
            1,
        )
        qp.setPen(pen)

        # Define the bounding rectangle for the wheel
        wheel_rect = QRectF(10.0, 10.0, 380.0, 380.0)

        # Define option-related variables
        if len(self.options) < 2:
            angles = [0]
        elif len(self.options) < 7 and len(self.options) >= 2:
            angles = np.arange(0, 360, 360 / (len(self.options) * 2), dtype=int)
        else:
            if 360 % len(self.options) != 0:
                ceiling = math.ceil(360 / len(self.options))
                angles = [i * ceiling for i in range(len(self.options))]
            else:
                angles = np.arange(0, 360, 360 / len(self.options), dtype=int)

        if len(self.options) != 0:
            points = self.calTextCoord(len(angles))

        # Draw the segments
        if len(self.options) < 2:
            qp.save()
            qp.setPen(Qt.NoPen)
            qp.setBrush(QBrush(self.colors[0], Qt.SolidPattern))
            qp.drawPie(wheel_rect, angles[0] * 16 - self.angle, 360 * 16)
            qp.restore()
        else:
            for i in range(len(angles)):
                qp.setBrush(QBrush(self.colors[i % len(self.options)], Qt.SolidPattern))
                qp.drawPie(wheel_rect, angles[i] * 16 - self.angle, angles[1] * 16)

        # Draw text
        if len(self.options) > 0:
            for i in range(len(angles)):
                qp.save()
                qp.scale(1, 1)
                qp.setFont(QFont("Academy Engraved LET", 25))
                a = points[i, 2]
                x, y = (
                    self.text_radius * points[i, 0],
                    self.text_radius * points[i, 1],
                )
                if points[i, 0] < 0:
                    a = a - np.pi
                qp.drawText(
                    math.ceil(self.central_point.x() + x),
                    math.ceil(self.central_point.y() + y),
                    self.options[i % len(self.options)].text(),
                )
                qp.restore()

        # Draw circles in the middle and the triangular pointer
        center_point = QPoint(200, 200)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 60, 60)
        qp.drawPolygon(QPolygon([QPoint(140, 200), QPoint(260, 200), QPoint(200, 125)]))
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.setBrush(QBrush(QColor(189, 189, 189), Qt.SolidPattern))
        qp.drawEllipse(center_point, 35, 35)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 25, 25)

    def addOption(self):
        # Move text field and submit button
        self.text_field.move(self.text_field.x(), self.text_field.y() + 30)
        self.submit_button.move(self.submit_button.x(), self.submit_button.y() + 30)

        # Turn submitted text into label
        self.options.append(QLabel(f"{self.text_field.text()}", self))
        self.options[-1].move(self.text_field.x(), self.text_field.y() - 30)
        self.options[-1].show()
        self.text_field.clear()

        # Update window
        self.mModified = True
        self.update()

    def calTextCoord(self, N):
        arclen = ((2 * np.pi / N) * np.arange(0.5, N, 1)) + (
            (np.pi / 180) * (self.angle / 16)
        )
        coordX = np.cos(arclen)
        coordY = np.sin(arclen)
        return np.c_[coordX, coordY, arclen]  # 每一個 row 代表一個點，其中三筆資料分別代表該點的 X 座標、Y 座標、

    def startTimer(self):
        self.counter = 0
        self.spin_time = random.randint(2000, 2500)
        self.spin_angle = 30
        self.decrease_angle = self.spin_angle / ((self.spin_time // 7) * 6)
        self.timer.start(1)

    def onTimer(self):
        if self.counter < self.spin_time:
            if math.ceil(self.spin_angle) == 0:
                self.spin_angle = 1
                self.decrease_angle = 0
            if self.counter < (self.spin_time // 7):
                self.angle += self.spin_angle
            elif self.counter >= (self.spin_time // 7):
                self.spin_angle -= self.decrease_angle
                self.angle += math.ceil(self.spin_angle)
            self.counter += 1
            self.mModified = True
            self.update()
        else:
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    roulette = Roulette()
    roulette.show()
    sys.exit(app.exec_())
