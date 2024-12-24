import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from main_form import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.pushButton.clicked.connect(self.find)

    def find(self):
        self.tableWidget.setRowCount(0)
        cur = self.db.cursor()
        result = cur.execute('SELECT * FROM info').fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Тип зерен', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        for index, elem in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for i, item in enumerate(elem):
                self.tableWidget.setItem(index, i, QTableWidgetItem(str(item)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
