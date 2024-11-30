from .database import DataBase
from ..controller.livro import Livros


class ControllerLivro:

    @staticmethod
    def castradarLivro(id_livro = None, titulo = None, autor =  None, genero = None, isbn =  None):
        db = DataBase()

        db.cursor.execute(Livros.cadastrarLivro(), (id_livro, titulo, autor, genero, isbn))
        




