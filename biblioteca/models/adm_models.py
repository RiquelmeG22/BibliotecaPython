import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

ui_file = 'view/cadastro_livro.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.btnCadastrar: QPushButton
        self.label: QLabel
        self.btnCadastrar.setText('Cadastrar')
        self.btnCadastrar.clicked.connect(self.clicked)

    def clicked(self):
        cadLivro = {
            'nomeLivro': self.lineNcompleto.text(),
            'e-mail': self.lineEmail.text(),
            'senha': self.lineSenha.text(),
            'cpf': self.linecpf.text(),
        }