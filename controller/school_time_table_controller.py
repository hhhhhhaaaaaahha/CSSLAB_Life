from PyQt5.QtWidgets import QMainWindow
from ui.school_time_table_ui import ShoolTimeTableUI
from src.school_time_table import SchoolTimeTable

class SchoolTimeTableController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 850, 850)
        self.setWindowTitle("School Time Table")

        self.schoolTimeTable = SchoolTimeTable()
        self.ui = ShoolTimeTableUI(self)

        #button lisener
        self.ui.setComboBoxLisener(self.changeClassTimeScedualLissener)
        
        # initail 顯示yuko課表
        self.ui.initailize(self.schoolTimeTable.ClassTimeScedual.keys(), self.schoolTimeTable.ClassTimeScedual['子瑩'])

    def changeClassTimeScedualLissener(self):
        name = self.ui.ComboBoxGetter()
        self.ui.change(self.schoolTimeTable.ClassTimeScedual[name])

if __name__ == '__main__':
    import sys
    app = QMainWindow.QApplication(sys.argv)
    Form = QMainWindow()
    Form.show()
    sys.exit(app.exec_())