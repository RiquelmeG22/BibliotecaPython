import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

ui_file = 'layouts/emprestimo.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.btnCadastrar: QPushButton
        self.label: QLabel
        self.btnCadastrar.setText('Cadastrar')
        self.btnCadastrar.clicked.connect(self.clicked)

    def clicked(self):
        emprestimo = {
            'nomeLivro': self.lineEmprestimo.text(),
            'genero': self.lineEdit_genero.text(),
            'isbn': self.lineEdit_isbn.text(),
            'cpf': self.lineEdit_status.text(),
        }
                      
        print(emprestimo)
        print('oi')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())