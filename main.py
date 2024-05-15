'''
pushButton - база подрядчиков
pushButton_2 - добавить оплату
pushButton_3 - проекты
pushButton_4 - клиенты
pushButton_5 - база артистов
'''

import sys
import sqlite3
import interface_ui
import second_ui
from interface_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor() #создаем курсор для выполнения SQL-запросов и операций с БД

# создание дочернего окна
class Second_Window(QtWidgets.QMainWindow, second_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Regi(QtWidgets.QMainWindow, interface_ui.Ui_MainWindow):
    def __init__(self):
        super(Regi, self).__init__()
        self.setupUi(self)
        self.twoWindow = None
        self.pushButton.clicked.connect(self.check)

        self.pushButton_3.clicked.connect(self.open_projects_link) # добавления перехода по ссылке на кнопку "Проекты"

    # функция открытия ссылки на папку с проектами в браузере по умолчанию
    def open_projects_link(self):
        url = QUrl("https://drive.google.com/drive/u/1/folders/14-9pH8GVzPcU5XcOBE46rl6Uvt-J2TQs")
        QDesktopServices.openUrl(url)

    def check(self):
        self.twoWindow = Second_Window()
        self.twoWindow.show()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

"""# Создаем индекс для столбца "email"
cursor.execute('CREATE INDEX idx_email ON Users (email)')

# Добавляем нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

# Обновляем возраст пользователя "newuser"
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

# Удаляем пользователя "newuser"
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Выводим результаты
for user in users:
  print(user)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()"""

app = QtWidgets.QApplication([])  # передаем пустой список
window = Regi()
window.show()

app.exec()
