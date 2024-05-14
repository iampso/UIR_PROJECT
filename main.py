'''
pushButton_3 - проекты
'''


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from design_ui import Ui_MainWindow
import design_ui
import webbrowser

class Regi(QtWidgets.QMainWindow, design_ui.Ui_MainWindow):
    def __init__(self):
        super(Regi, self).__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.open_projects_link) # добавления перехода по ссылке на кнопку "Проекты"


    # открытие ссылки на папку с проектами в браузере по умолчанию
    def open_projects_link(self):
        url = QUrl("https://drive.google.com/drive/u/1/folders/14-9pH8GVzPcU5XcOBE46rl6Uvt-J2TQs")
        QDesktopServices.openUrl(url)


app = QtWidgets.QApplication([])  # передаем пустой список
window = Regi()
window.show()

app.exec()
