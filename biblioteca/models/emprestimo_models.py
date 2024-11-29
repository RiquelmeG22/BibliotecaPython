class Emprestimo:

    maxLivro = 3
    @staticmethod
    def maximoLivro():
        return Emprestimo.maxLivro

    @staticmethod
    def fazerEmprestimo():
        return 'insert into emprestimo (id_livro, id_usuario, devolucao) values (%s,%s,false)'
    
    @staticmethod
    def fazerDevolucao():
        return 'update emprestimo set devolucao = true where id_emprestimo = %s'

