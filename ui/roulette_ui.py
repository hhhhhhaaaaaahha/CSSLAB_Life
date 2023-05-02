from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtGui import QColor, QFont

from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow,
)

import random


class RouletteUI(object):
    def setupUI(self, window: QMainWindow):
        # Set window
        window.setGeometry(100, 100, 800, 600)
        window.setWindowTitle("Roulette")

        # Define the colors for pie
        self.rgbs = [
            (195, 166, 211),
            (215, 183, 232),
            (237, 201, 255),
            (246, 207, 243),
            (254, 212, 231),
            (248, 198, 195),
            (242, 183, 159),
            (236, 183, 132),
            (229, 183, 105),
            (223, 194, 79),
            (220, 199, 66),
            (216, 204, 52),
            (220, 209, 70),
        ]
        random.shuffle(self.rgbs)
        self.colors = [QColor(r, g, b) for r, g, b in self.rgbs]

        # spin-related variables
        self.angle = 0
        self.decrease_angle = 0
        self.counter = 1000000
        self.spin_time = 100000
        self.spin_angle = 30
        self.timer = QTimer()

        # text-related variables
        self.text_radius = 150
        self.central_point = QPoint(282, 298)

        # Add return button
        self.retbtn = QPushButton(window)
        self.retbtn.setText("返回首頁")
        self.retbtn.move(10, 10)

        # Add spin button
        self.spin_button = QPushButton("Spin", window)
        self.spin_button.setFixedWidth(100)
        self.spin_button.move(220, 500)

        ## Option-related
        # Init option text field
        # self.add_option_icon = QLabel(self)
        # self.add_option_icon.setPixmap(
        #     QPixmap("img/21a921f165298b0110b80821cc5bd761.svg").scaled(25, 25)
        # )
        # self.add_option_icon.setPixmap(QPixmap("./img/add_button.png").scaled(25, 25))
        # self.add_option_icon.move(500, 8)
        self.text_field = QLineEdit(window)
        self.text_field.setFixedWidth(130)
        self.text_field.setFixedHeight(23)
        self.text_field.move(535, 10)
        self.restaurant_labels: list[QLabel] = []

        # Init chosen label
        self.chosen_option = QLabel("???", window)
        self.chosen_option.setFont(QFont("Arial", 30))
        self.chosen_option.setAlignment(Qt.AlignCenter)
        self.chosen_option.setFixedWidth(162)
        self.chosen_option.setFixedHeight(40)
        self.chosen_option.setFrameShape(QFrame.Panel)
        self.chosen_option.setFrameShadow(QFrame.Sunken)
        self.chosen_option.setLineWidth(3)
        self.chosen_option.move(189, 50)

        # Init submit button
        self.submit_button = QPushButton("新增", window)
        self.submit_button.move(670, 5)
        # icon = QIcon("img/add_button.png")
        # self.submit_button.setIcon(icon)

        # Inin clear button
        self.clear_button = QPushButton("清除", window)
        self.clear_button.move(600, 50)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    roulette_ui = RouletteUI()
    roulette_ui.setupUI(window)
    window.show()
    sys.exit(app.exec_())
