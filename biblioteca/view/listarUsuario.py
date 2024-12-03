import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


ui_file = 'biblioteca\\view\\listarUsuario.ui'

class listarUsuario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

