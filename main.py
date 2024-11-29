import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from biblioteca.controller.emprestimo_controller import ControllerEmprestimo

ui_file = 'layouts/cadastro_livro.ui'

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
                      
        print(cadLivro)

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec())
    ControllerEmprestimo.fazerEmprestimo(2, 2)



