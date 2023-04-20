import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QTransform, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRectF, QTimer, QPropertyAnimation
import math
import random
import time


class Roulette(QWidget):
    def __init__(self):
        super().__init__()

        self.mModified = True
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Roulette")
        self.angle = 0
        self.counter = 1000000

        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimer)
        self.timer.start(1)

        spin_button = QPushButton("Spin", self)
        spin_button.clicked.connect(self.startTimer)

    def paintEvent(self, event):
        if self.mModified:
            qp = QPainter()
            qp.begin(self)
            self.drawRoulette(qp)
            qp.rotate(self.angle)
            # qp.end()
            self.mModified = False

    def drawRoulette(self, qp):
        pen = QPen(
            QColor(0, 0, 0),
            1,
        )  # Qt.SolidLine)
        qp.setPen(pen)

        # Define the bounding rectangle for the wheel
        wheel_rect = QRectF(10.0, 10.0, 380.0, 380.0)

        # Define the colors and angles for each segment
        colors = [QColor(251, 140, 0), QColor(229, 57, 53), QColor(253, 216, 53)]
        angles = [0, 45, 90, 135, 180, 225, 270, 315]

        # Draw the segments
        for i in range(len(angles)):
            qp.setBrush(QBrush(colors[i % 3], Qt.SolidPattern))
            qp.drawPie(wheel_rect, angles[i] * 16 - self.angle, 45 * 16)

        # Draw the center point
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        center_point = QPoint(200, 200)
        qp.drawEllipse(center_point, 60, 60)
        qp.setBrush(QBrush(QColor(189, 189, 189), Qt.SolidPattern))
        qp.drawEllipse(center_point, 35, 35)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 25, 25)

    def startTimer(self):
        self.counter = 0
        self.timer.start(1)

    # def stopTimer(self):
    #     self.timer.stop()

    def onTimer(self):
        if self.counter < 1000:
            self.counter += 1
            self.angle += 30
            self.mModified = True
            self.update()
        else:
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    roulette = Roulette()
    roulette.show()
    sys.exit(app.exec_())


# class Roulette(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.angle = 0
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update)
#         self.timer.start(10)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         width, height = self.width(), self.height()
#         x, y = width / 2, height / 2

#         # draw the roulette
#         brush = QBrush(Qt.SolidPattern)
#         brush.setColor(Qt.red)
#         painter.setBrush(brush)
#         pen = QPen(Qt.NoPen)
#         painter.setPen(pen)
#         painter.drawEllipse(x - 100, y - 100, 200, 200)

#         # draw the pointer
#         painter.translate(x, y)
#         painter.rotate(self.angle)
#         brush.setColor(Qt.blue)
#         painter.setBrush(brush)
#         painter.drawEllipse(-10, -10, 20, 20)
#         painter.drawRect(-1, -100, 2, 100)

#     def spin(self):
#         self.angle += 1


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Roulette")
#         self.setGeometry(100, 100, 400, 400)

#         self.roulette = Roulette(self)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.roulette)

#         button = QPushButton("Spin", self)
#         button.clicked.connect(self.roulette.spin)
#         layout.addWidget(button)

#         self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())
