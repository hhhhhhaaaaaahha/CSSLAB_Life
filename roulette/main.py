from PyQt5 import QtWidgets
from roulette_controller import RouletteController
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RouletteController()
    window.show()
    sys.exit(app.exec_())
