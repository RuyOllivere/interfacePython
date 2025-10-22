import test
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import datetime as dt
import os

class MainScreen(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__number = 0

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
        text = self.textBox.text()
        keyPass = self.keypassBox.text()
        print(f"Login: {text}")
        print(f"Password: {keyPass}")