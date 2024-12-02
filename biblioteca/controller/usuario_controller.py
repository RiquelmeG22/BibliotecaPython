from .database import DataBase
from ..controller.usuario_controller import Usuario


class ControllerUsuario:

    @staticmethod
    def cadastrarUsuario(id_usuario = None, nome_completo = None, email =  None, senha = None, cpf =  None):
        db = DataBase()

        db.cursor.execute(Usuario.cadastrarUsuario(), (id_usuario, nome_completo, email, senha, cpf))

        db.conexao.commit()

        db.desconectar()


    @staticmethod
    def excluirUsuario(id_usuario = None, nome_completo = None, email =  None, senha = None, cpf =  None):
        db = DataBase()

        db.cursor.execute(Usuario.excluirUsuario())






   

