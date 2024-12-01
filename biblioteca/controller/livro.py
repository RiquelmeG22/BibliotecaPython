from .database import DataBase
from ..controller.livro import Livros


class ControllerLivro:

    @staticmethod
    def castradarLivro(id_livro = None, titulo = None, autor =  None, genero = None, isbn =  None):
        db = DataBase()

        db.cursor.execute(Livros.cadastrarLivro(), (id_livro, titulo, autor, genero, isbn))

        db.conexao.commit()

        db.desconectar()

    @staticmethod
    def excluirLivro(id_livro, titulo):
        db = DataBase()

        db.cursor.execute(Livros.excluirLivro(), (id_livro, titulo))

        db.cursor.commit()

        db.desconectar()

    @staticmethod
    def atualizarLivro(id_livro = None, titulo = None, autor =  None, genero = None, isbn =  None):
        db = DataBase()

        db.cursor.execute(Livros.atualizarLivro(), (id_livro, titulo, autor, genero, isbn))

        db.cursor.commit()

        db.desconectar()


    @staticmethod
    def consultaLivro(id_livro= None, titulo=None, autor=None, genero=None, isbn=None):
        db = DataBase()
        
        lista = []
        db.cursor.execute(Livros.consultaLivro(id_livro, titulo, autor, genero, isbn), tuple(lista))

        db.cursor.commit()

        db.desconectar()





    
    



    


