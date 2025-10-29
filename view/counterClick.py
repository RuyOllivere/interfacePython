import test
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from notifypy import Notify
import datetime as dt

from controller.authController import AuthController as ac

import os

class MainScreen(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__number = 0
        # Load the .ui file

        loadUi('view/pythonInterface.ui', self)
        self.show()
        # self.btnClick.clicked.connect(self.showInfo)
        self.btnExit.clicked.connect(self.finishProgram)

    @pyqtSlot()
    def on_btnClick_pressed(self):
        self.showInfo()
        self.getText()

    def showInfo(self):
        print(f"Btn clicked: {self.__number}")
        self.counterScreen.setText(str(self.__number))
        self.__number += 1

    def finishProgram(self):

        print(f"Program finished: {dt.datetime.now()}")
        os._exit(0)
    
    def getText(self):

        login = self.textBox.text()
        keyPass = self.keypassBox.text()

        authLogin = ac()
        authLogin.authenticate(login, keyPass)

        if authLogin:
            self.Notify("Login", "Login made!")
        else:
            self.Notify("Login", "Login error!")

    def Notify(self, title, msg):
        notification = Notify()
        notification.title = title
        notification.message = msg
        notification.send()




        # print(f"Login: {login}")
        # print(f"Password: {keyPass}")

        #         # Debug: show raw values and strip whitespace
        # login = self.textBox.text().strip()
        # keyPass = self.keypassBox.text().strip()
        # print("DEBUG: login repr:", repr(login))
        # print("DEBUG: keyPass repr:", repr(keyPass))

        # # Validate before calling authenticate
        # if not login:
        #     QMessageBox.warning(self, "Missing input", "Login is missing.")
        #     return
        # if not keyPass:
        #     QMessageBox.warning(self, "Missing input", "Password is missing.")
        #     return

        # # Call authenticate and optionally print result (depends on your controller)
        # result = ac.authenticate(login, keyPass)
        # print("authenticate returned:", repr(result))