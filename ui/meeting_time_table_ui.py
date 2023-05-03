from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont


class MeetingTimeTableUI:
    def style(self):
        self.style_box = """
            background:#fff;
            border:1px solid #000;
        """
        self.style_firstrowLabel = """
            background:#fff;
            font-weight:bold;
            border:1px solid #000;
            text-align:center;
        """
        self.style_firstcolLabel = """
            font-weight:bold;
            border:0px solid #000;
            text-align:center;
        """
        self.initstyle_Labels = """
            background:#fff;
            border:0px solid #000;
            text-align:center;
        """

    def __init__(self, window: QtWidgets.QMainWindow, meeting_time):
        self.style()

        window.setGeometry(0, 0, 1000, 600)

        self.retbtn = QtWidgets.QPushButton(window)
        self.retbtn.setText("返回首頁")
        self.retbtn.move(10, 10)

        self.label = QtWidgets.QLabel(window)
        self.label.setFixedWidth(200)
        self.label.setText("meeting時間表")
        font = QFont("Arial", 25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.move(50, 70)

        x = 70
        y = 120
        w = 170
        h = 50

        self.vboxs = {}
        self.v_layouts = {}
        self.Labels = {}
        self.firstrowLabels = {}

        col_time = list(set([member[1][1] for member in meeting_time]))
        col_time.sort()
        for i in range(1, len(col_time) + 1):  # first col
            label_name = "-1," + str(i)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(window)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstcolLabel)
            self.firstrowLabels[label_name].setText(col_time[i - 1])
            self.firstrowLabels[label_name].setGeometry(15, y + i * h, 50, h)
        first_row_table = {
            "0,0": "Mon.",
            "0,1": "Tue.",
            "0,2": "Wed.",
            "0,3": "Thu.",
            "0,4": "Fri.",
        }
        for j in range(5):  # first row
            label_name = "0," + str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(window)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j * w, y, w, h)
        for i in range(1, len(col_time) + 1):
            for j in range(1, 6):
                label_name = str(i) + "," + str(j)
                self.vboxs[label_name] = QtWidgets.QWidget(window)
                self.vboxs[label_name].setGeometry(x + (j - 1) * w, y + i * h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(
                    self.vboxs[label_name]
                )

                self.Labels[label_name] = QtWidgets.QLabel(window)
                self.Labels[label_name].setWordWrap(True)
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Labels[label_name])
        for member in meeting_time:
            meeting_day_time = (
                member[1][0] + "," + str(col_time.index(member[1][1]) + 1)
            )
            self.Labels[meeting_day_time[len(meeting_day_time) :: -1]].setText(
                member[0]
            )  # reverse
