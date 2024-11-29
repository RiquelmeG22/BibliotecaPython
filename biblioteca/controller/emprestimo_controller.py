from .database import DataBase
from ..models.emprestimo_models import Emprestimo

class ControllerEmprestimo:


    @staticmethod
    def fazerEmprestimo(id_livro, id_usuario):
        db = DataBase()
        
        db.cursor.execute(Emprestimo.fazerEmprestimo(), (id_livro, id_usuario))

        db.conexao.commit()
