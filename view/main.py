import test
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from notifypy import Notify
import datetime as dt

from controller.authController import AuthController as ac

import os

class MainUi(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the .ui file
        loadUi('view/mainUi.ui', self)
        self.show()