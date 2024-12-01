from .database import DataBase
from ..models.emprestimo_models import Emprestimo

class ControllerEmprestimo:


    @staticmethod
    def fazerEmprestimo(id_livro, id_usuario):
        db = DataBase()
        
        db.cursor.execute(Emprestimo.fazerEmprestimo(), (id_livro, id_usuario))

        db.conexao.commit()

        db.desconectar()


    @staticmethod
    def fazerDevolucao(id_livro, id_usuario):
        db = DataBase()

        db.cursor.execute(Emprestimo.fazerDevolucao(), (id_livro, id_usuario))

        db.conexao.commit()

        db.desconectar()


    @staticmethod
    def exibirLivro(id_livro, id_usuario):
        db = DataBase()

        db.cursor.exucete(Emprestimo.exibirLivro(), (id_livro, id_usuario))

        db.cursor.fetchall()

        db.conexao.commit()

        db.desconectar()

        


      

    