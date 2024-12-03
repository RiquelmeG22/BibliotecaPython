import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

ui_flile = ui_file = 'biblioteca\\view\\home.ui'


class  Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.btnListarUsuario: QPushButton
        self.btnLivro: QPushButton
        self.btnRealizarEmprestimo: QPushButton
        self.btnCadastrarLivro: QPushButton
        self.btnCadastrarUsuario: QPushButton
        self.btnCadastrar.setText('Cadastrar')
        self.btnCadastrar.clicked.connect(self.clicked)



