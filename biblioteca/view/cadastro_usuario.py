import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit


ui_file = 'biblioteca\\view\\cadastro_usuario.ui'

class CadastroUsuario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.lineNcompleto: QLineEdit
        self.lineEmail: QLineEdit
        self.lineSenha: QLineEdit
        self.lineCpf: QLineEdit
        self.btnCadastrar: QPushButton
        self.btnCadastrar.setText('Cadastrar')
        self.btnCadastrar.clicked.connect(self.clicked)

    def clicked(self):
        self.tela_home = listarUsuario()
        self.tela_home.show()




        