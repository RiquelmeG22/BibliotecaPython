import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from biblioteca.controller.emprestimo_controller import ControllerEmprestimo
from biblioteca.view.listarUsuario import listarUsuario


ui_file = 'biblioteca\\view\\cadastro_livro.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.BtnCadastrarLivro: QPushButton
        self.label: QLabel
        self.BtnCadastrarLivro.setText('Cadastrar')
        self.BtnCadastrarLivro.clicked.connect(self.clicked)

    def clicked(self):
        self.tela_listar = listarUsuario()
        self.tela_listar.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    # ControllerEmprestimo.fazerEmprestimo(2, 2)



