from PyQt5.QtWidgets import QApplication, QtWidgets
import sys  # Только для доступа к аргументам командной строки
#   import design  # Здесь должен быть конвертированный файл ui
import os

class ExmpleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр класса QApplication
    window = ExmpleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()



