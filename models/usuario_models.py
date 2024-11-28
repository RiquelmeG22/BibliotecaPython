class Usuario():
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
    
    def castradarUsuario(self):
        return 'INSERT INTO usuario (nome_completo, email, senha, cpf) VALUES (%s,%s,%s,%s)'

    def excluirUsuario(self):
        return 'delete from usuario where id_usuario = %s'
    
    def atualizarUsuario(self):
        return 'update usuario set email = %s, nome_completo = %s, senha = %s, cpf = %s, where id_usuario = %s'
    
    def consultaUsuario(self, nome, email):
        if nome:
            return 'select * from usuario where nome = (%s)'
        elif email:
            return 'select * from usuario where email = (%s)'
          
