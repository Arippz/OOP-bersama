from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QPushButton,
)

import sys
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainContainer = QHBoxLayout()
        
        self.label1 = QLabel("Welcome text")

        self.mainContainer.addWidget(self.label1)
        
        self.widget = QWidget()
        self.setFixedSize(600, 300)
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.mainContainer)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()