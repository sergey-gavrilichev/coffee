import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem


class CoffeeInformation(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_table()

    def load_table(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM coffee_information').fetchall()
        if not result:
            return
        self.tableWidget.setColumnCount(7)
        labels = ['ID',
                  'название сорта',
                  'степень обжарки',
                  'молотый/в зёрнах',
                  'описание вкуса',
                  'цена(руб)',
                  'объём упаковки(г)'
                  ]
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 247)
        self.tableWidget.setColumnWidth(5, 70)
        self.tableWidget.setColumnWidth(6, 120)
        n = 0
        for elem in result:
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1
            )
            self.tableWidget.setItem(n, 0, QTableWidgetItem(str(elem[0])))
            self.tableWidget.setItem(n, 1, QTableWidgetItem(str(elem[1])))
            self.tableWidget.setItem(n, 2, QTableWidgetItem(str(elem[2])))
            self.tableWidget.setItem(n, 3, QTableWidgetItem(str(elem[3])))
            self.tableWidget.setItem(n, 4, QTableWidgetItem(str(elem[4])))
            self.tableWidget.setItem(n, 5, QTableWidgetItem(str(elem[5])))
            self.tableWidget.setItem(n, 6, QTableWidgetItem(str(elem[6])))
            n += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeInformation()
    ex.show()
    sys.exit(app.exec())
