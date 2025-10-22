from view.counterClick import MainScreen
from PyQt5.QtWidgets import QApplication
import os

if __name__ == "__main__":
    
    app = QApplication([])

    screen = MainScreen()

    app.exec_()