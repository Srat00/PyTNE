from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import ImageResource_rc

form_class = uic.loadUiType("Core/GUI.ui")[0]


class Window(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Text Novel Engine v2.0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec_())
