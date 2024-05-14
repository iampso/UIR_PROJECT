import sys

from PyQt5 import QtWidgets
from design_ui import Ui_MainWindow
import design_ui

class Regi(QtWidgets.QMainWindow, design_ui.Ui_MainWindow):
    def __init__(self):
        super(Regi, self).__init__()
        self.setupUi(self)

app = QtWidgets.QApplication([])  # передаем пустой список
window = Regi()
window.show()

app.exec()
