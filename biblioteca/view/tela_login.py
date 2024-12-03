import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from biblioteca.view.home import Home


ui_file = 'biblioteca\\view\\tela_login.ui'


class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.line_Email: QLineEdit
        self.line_Senha: QLineEdit
        self.Button_login: QPushButton
        self.ButtonCadastrar: QPushButton
        self.Button_login.clicked.connect(self.clicked)

    def clicked(self):
        if(not hasattr(self, 'tela_home')):
            self.tela_home = Home()

        self.tela_home.show()

    
