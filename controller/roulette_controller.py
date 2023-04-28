from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QBrush, QColor, QFont, QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QLabel, QMainWindow
from src.roulette import Roulette

import math
import numpy as np
import random

from ui.roulette_ui import RouletteUI


class RouletteController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.roulette = Roulette()
        self.ui = RouletteUI()
        self.ui.setupUI(self)
        self.setInitUI()

    def setInitUI(self):
        self.ui.spin_button.clicked.connect(self.startTimer)
        self.ui.submit_button.clicked.connect(self.addOption)
        self.ui.timer.timeout.connect(self.onTimer)

    def paintEvent(self, event):
        if self.ui.mModified:
            qp = QPainter()
            qp.begin(self)
            self.drawRoulette(qp)
            self.ui.mModified = False

    def drawRoulette(self, qp: QPainter):
        pen = QPen(
            QColor(0, 0, 0),
            1,
        )
        qp.setPen(pen)

        # Define the bounding rectangle for the wheel
        wheel_rect = QRectF(80.0, 100.0, 380.0, 380.0)

        # Define option-related variables
        if self.roulette.getRestaurantCount() < 2:
            angles = [0]
        elif (
            self.roulette.getRestaurantCount() < 7
            and self.roulette.getRestaurantCount() >= 2
        ):
            angles = np.arange(
                0, 360, 360 / (self.roulette.getRestaurantCount() * 2), dtype=int
            )
        else:
            if 360 % self.roulette.getRestaurantCount() != 0:
                ceiling = math.ceil(360 / self.roulette.getRestaurantCount())
                angles = [
                    i * ceiling for i in range(self.roulette.getRestaurantCount())
                ]
            else:
                angles = np.arange(
                    0, 360, 360 / self.roulette.getRestaurantCount(), dtype=int
                )

        if self.roulette.getRestaurantCount() != 0:
            points = self.calTextCoord(len(angles))

        # Draw the segments
        if self.roulette.getRestaurantCount() < 2:
            qp.save()
            qp.setPen(Qt.NoPen)
            qp.setBrush(QBrush(self.ui.colors[0], Qt.SolidPattern))
            qp.drawPie(wheel_rect, angles[0] * 16 - self.ui.angle, 360 * 16)
            qp.restore()
        else:
            for i in range(len(angles)):
                qp.setBrush(
                    QBrush(
                        self.ui.colors[i % self.roulette.getRestaurantCount()],
                        Qt.SolidPattern,
                    )
                )
                qp.drawPie(wheel_rect, angles[i] * 16 - self.ui.angle, angles[1] * 16)

        # Draw text
        if self.roulette.getRestaurantCount() > 0:
            for i in range(len(angles)):
                qp.save()
                qp.scale(1, 1)
                qp.setFont(QFont("Arial", 25))
                a = points[i, 2]
                x, y = (
                    self.ui.text_radius * points[i, 0],
                    self.ui.text_radius * points[i, 1],
                )
                if points[i, 0] < 0:
                    a = a - np.pi
                qp.drawText(
                    math.ceil(self.ui.central_point.x() + x),
                    math.ceil(self.ui.central_point.y() + y),
                    self.roulette.getRestaurant(i % self.roulette.getRestaurantCount()),
                )
                qp.restore()

        # Draw circles in the middle and the triangular pointer
        center_point = QPoint(270, 290)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 60, 60)

        qp.drawPolygon(QPolygon([QPoint(210, 290), QPoint(330, 290), QPoint(270, 215)]))

        qp.setBrush(QBrush(QColor(189, 189, 189), Qt.SolidPattern))
        qp.drawEllipse(center_point, 35, 35)

        qp.setBrush(QBrush(QColor(117, 117, 117), Qt.SolidPattern))
        qp.drawEllipse(center_point, 25, 25)

    def addOption(self):
        # Add text in text field to restaurant_list
        self.roulette.addRestaurant(self.ui.text_field.text())

        # Move text field and submit button
        self.ui.text_field.move(self.ui.text_field.x(), self.ui.text_field.y() + 30)
        self.ui.submit_button.move(
            self.ui.submit_button.x(), self.ui.submit_button.y() + 30
        )

        # Turn submitted text into label
        self.ui.restaurant_labels.append(QLabel(f"{self.ui.text_field.text()}", self))
        self.ui.restaurant_labels[-1].move(
            self.ui.text_field.x(), self.ui.text_field.y() - 30
        )
        self.ui.restaurant_labels[-1].show()
        self.ui.text_field.clear()

        # Update window
        self.ui.mModified = True
        self.update()

    def calTextCoord(self, n):
        arclen = ((2 * np.pi / n) * np.arange(0.5, n, 1)) + (
            (np.pi / 180) * (self.ui.angle / 16)
        )
        coordX = np.cos(arclen)
        coordY = np.sin(arclen)
        return np.c_[coordX, coordY, arclen]  # 每一個 row 代表一個點，其中三筆資料分別代表該點的 X 座標、Y 座標、

    def startTimer(self):
        self.ui.counter = 0
        self.ui.spin_time = random.randint(2000, 2500)
        self.ui.spin_angle = 60
        self.ui.decrease_angle = self.ui.spin_angle / (self.ui.spin_time // 2)
        self.ui.timer.start(1)

    def onTimer(self):
        if self.ui.counter < self.ui.spin_time:
            if math.ceil(self.ui.spin_angle) == 0:
                self.ui.spin_angle = 1
                self.ui.decrease_angle = 0
            if self.ui.counter < (self.ui.spin_time // 2):
                self.ui.angle += self.ui.spin_angle
            elif self.ui.counter >= (self.ui.spin_time // 2):
                self.ui.spin_angle -= self.ui.decrease_angle
                self.ui.angle += math.ceil(self.ui.spin_angle)
            self.ui.counter += 1
            self.ui.mModified = True
            self.update()

            # Check if chosen_option need to be update
            pixel_color = self.grab().toImage().pixelColor(540, 400).getRgb()
            if pixel_color[:3] != (0, 0, 0):
                self.ui.chosen_option.setText(
                    self.roulette.getRestaurantList()[::-1][
                        self.ui.rgbs.index((pixel_color[:3]))
                        - self.roulette.getRestaurantCount()
                    ]
                )
            self.ui.mModified = True
            self.update()
        else:
            self.ui.timer.stop()
