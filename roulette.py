from PyQt5.QtCore import Qt, QPoint, QRectF, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import math
import numpy as np
import random
import sys


class Roulette(QWidget):
    def __init__(self):
        super().__init__()

        self.mModified = True
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Roulette")

        # spin-related variable
        self.angle = 0
        self.decrease_angle = 0
        self.counter = 1000000
        self.spin_time = 100000
        self.spin_angle = 30
        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimer)

        # text-related variable
        self.text_radius = 150
        self.central_point = QPoint(192, 208)

        spin_button = QPushButton("Spin", self)
        spin_button.clicked.connect(self.startTimer)

    def paintEvent(self, event):
        if self.mModified:
            qp = QPainter()
            qp.begin(self)
            self.drawRoulette(qp)
            self.mModified = False

    def drawRoulette(self, qp):
        pen = QPen(
            QColor(0, 0, 0),
            1,
        )
        qp.setPen(pen)

        # Define the bounding rectangle for the wheel
        wheel_rect = QRectF(10.0, 10.0, 380.0, 380.0)

        # Define the colors and angles for each segment
        colors = [
            QColor(251, 140, 0),
            QColor(229, 57, 53),
            QColor(253, 216, 53),
            QColor(244, 81, 30),
        ]
        # Define optionns
        option = ["A", "B", "C"]
        angles = [60 * i for i in range(6)]
        points = self.calTextCoord(len(angles))

        # Draw the segments
        for i in range(len(angles)):
            qp.setBrush(QBrush(colors[i % len(option)], Qt.SolidPattern))
            qp.drawPie(wheel_rect, angles[i] * 16 - self.angle, 60 * 16)

        # Draw text
        for i in range(len(angles)):
            qp.save()
            qp.scale(1, 1)
            qp.setFont(QFont("Arial", 25))
            a = points[i, 2]
            x, y = (self.text_radius * points[i, 0], self.text_radius * points[i, 1])
            if points[i, 0] < 0:
                a = a - np.pi
            qp.drawText(
                math.ceil(self.central_point.x() + x),
                math.ceil(self.central_point.y() + y),
                option[i % 3],
            )
            qp.restore()

        # Draw circles in the middle
        center_point = QPoint(200, 200)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 60, 60)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.setBrush(QBrush(QColor(189, 189, 189), Qt.SolidPattern))
        qp.drawEllipse(center_point, 35, 35)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 25, 25)

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
