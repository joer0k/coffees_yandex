import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

import addEditCoffeeForm
import main_form


class Widget(QMainWindow, main_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.button_show.clicked.connect(self.find)
        self.button_add.clicked.connect(self.adding)
        self.button_change.clicked.connect(self.changing)

    def find(self):
        self.tableWidget.setRowCount(0)
        cur = self.db.cursor()
        result = cur.execute('SELECT * FROM info').fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Тип зерен', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        for index, elem in enumerate(result[::-1]):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for i, item in enumerate(elem):
                self.tableWidget.setItem(index, i, QTableWidgetItem(str(item)))

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()

    def changing(self):
        if self.tableWidget.selectedItems():
            id = [i.row() for i in self.tableWidget.selectedItems()]
            elems = [self.tableWidget.item(*id, j).text() for j in range(0, 7)]
            self.statusbar.showMessage('')
            self.add_form = AddWidget(self, elems=elems)
            self.add_form.show()
        else:
            self.statusbar.showMessage('Ничего не выбрано')


class AddWidget(QMainWindow, addEditCoffeeForm.Ui_MainWindow):
    def __init__(self, parent=None, elems=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.data = elems
        if self.data:
            self.edit_name.setText(self.data[1])
            self.edit_roasted.setText(self.data[2])
            self.edit_type.setText(self.data[3])
            self.edit_taste.setText(self.data[4])
            self.edit_cost.setText(self.data[5])
            self.edit_amount.setText(self.data[6])
            self.pushButton.setText('Изменить')
            self.pushButton.clicked.connect(self.change_info)
        else:
            self.pushButton.setText('Добавить')
            self.pushButton.clicked.connect(self.add_info)
        self.main = parent

    def get_adding_verdict(self):
        try:
            if not all([self.edit_name.text(), self.edit_cost.text(), self.edit_type.text(), self.edit_taste.text(),
                        self.edit_amount.text(), self.edit_roasted.text()]):
                raise TypeError
            if self.edit_name.text().replace(' ', '') == '' or self.edit_roasted.text().replace(' ', '') == '':
                raise TypeError
            elif not self.edit_cost.text().isdigit():
                raise TypeError
            else:
                return True
        except TypeError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False

    def add_info(self):
        if self.get_adding_verdict():
            cur = self.db.cursor()
            last_id = len(cur.execute('SELECT DISTINCT id FROM info').fetchall())
            cur.execute('INSERT INTO info VALUES (?, ?, ?, ?, ?, ?, ?)', (
                str(last_id + 1), self.edit_name.text(), self.edit_roasted.text(), self.edit_type.text(),
                self.edit_taste.text(), self.edit_cost.text(), self.edit_amount.text()))
            self.db.commit()
            self.main.find()
            self.close()

    def change_info(self):
        if self.get_adding_verdict():
            cur = self.db.cursor()
            cur.execute(
                f'UPDATE info SET name = "{self.edit_name.text()}",'
                f' roasted = "{self.edit_roasted.text()}",'
                f' type = "{self.edit_type.text()}",'
                f' taste = "{self.edit_taste.text()}",'
                f' cost = "{self.edit_cost.text()}",'
                f' amount = "{self.edit_amount.text()}" '
                f'WHERE id = "{self.data[0]}"')
            self.db.commit()
            self.main.find()
            self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
