from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Text Novel Engine")

        self.text = QTextBrowser(self)
        self.text.setGeometry(0, 0, 350, 250)
        self.text.append("Text")
        layout = QVBoxLayout()
        self.setLayout(layout)


app = QApplication(sys.argv)
root = Window()
sys.exit(app.exec_())
