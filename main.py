import PyQt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/database.ui', self)
        self.set_up_ui()
        self.show()

    def set_up_ui(self):
        self.setWindowTitle('Database')
        self.insert_data_button.clicked.connect(self.go_to_insert_data)
        self.insert_button.clicked.connect(self.get_input)
        self.home_button.clicked.connect(self.go_to_home)

    def go_to_insert_data(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_to_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def get_input(self):
        name = self.name_input.text()
        page_amount = self.amount_input.text()
        category = self.category_input.currentText()
        cover_type = self.cover_type_input.text()
        self.clear_input_fields()
        return name, page_amount, category, cover_type

    def clear_input_fields(self):
        self.name_input.setText('')
        self.amount_input.setValue(0)
        self.category_input.setCurrentIndex(0)
        self.cover_type_input.setText('')


app = QApplication(sys.argv)
window = MyWindow()
app.exec_()
