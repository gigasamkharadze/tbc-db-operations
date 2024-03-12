import sys
import time
import PyQt5
import threading
import sqlite3
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self, database):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/database.ui', self)
        self.conn = sqlite3.connect(database)
        self.set_up_database()
        self.set_up_ui()
        self.show()

    def set_up_database(self):
        self.conn.cursor().execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                page_amount INTEGER,
                category TEXT,
                cover_type TEXT
            )""")

    def set_up_ui(self):
        self.setWindowTitle('Database')
        self.insert_data_button.clicked.connect(self.go_to_insert_data)
        self.insert_button.clicked.connect(self.handle_save)
        self.home_button.clicked.connect(self.go_to_home)

    def go_to_insert_data(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_to_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def handle_save(self):
        name = self.name_input.text()
        page_amount = self.amount_input.text()
        category = self.category_input.currentText()
        cover_type = self.cover_type_input.text()
        self.clear_input_fields()

        c = self.conn.cursor()
        c.execute("""
            INSERT INTO books (name, page_amount, category, cover_type)
            VALUES (?, ?, ?, ?)
        """, (name, page_amount, category, cover_type))
        self.conn.commit()

        self.add_book_to_table(name, page_amount, category, cover_type)

    def add_book_to_table(self, name, page_amount, category, cover_type):
        row_position = self.database_table.rowCount()
        self.database_table.insertRow(row_position)
        self.database_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name))
        self.database_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(page_amount))
        self.database_table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(category))
        self.database_table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(cover_type))

    def clear_input_fields(self):
        self.name_input.setText('')
        self.amount_input.setValue(0)
        self.category_input.setCurrentIndex(0)
        self.cover_type_input.setText('')

    def closeEvent(self, event):
        self.conn.close()
        print('Connection closed')


app = QApplication(sys.argv)
window = MyWindow(database='library.db')
app.exec_()
