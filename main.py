from PyQt5.QtWidgets import QApplication
from controller.home_page_controller import HomePageController

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePageController()
    window.show()
    sys.exit(app.exec_())
