import test
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from notifypy import Notify
import datetime as dt

from controller.authController import AuthController as ac

import os

class LoginUi(QDialog):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__number = 0
        # Load the .ui file

        loadUi('view/loginPage.ui', self)
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
        result = authLogin.authenticate(login, keyPass)

        if result is True:
            self.Notify("Login", "Login made!")
            self.accept()
        else:
            self.Notify("Login", "Login error!")

    def Notify(self, title, msg):
        notification = Notify()
        notification.title = title
        notification.icon = "./template/dog.jpg"
        notification.message = msg
        notification.send()
