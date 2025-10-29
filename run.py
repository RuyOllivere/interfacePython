from view.counterClick import MainScreen
from view.main import MainUi
from view.loginPageUi import LoginUi
from PyQt5.QtWidgets import QApplication
import os

if __name__ == "__main__":
    
    app = QApplication([])

    login = LoginUi()

    bol = login.exec_()

    if(bol):

        screen = MainUi()
        app.exec_()