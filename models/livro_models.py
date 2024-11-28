
class Livros():
    def __init__(self, titulo, autor, genero, isbn) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
    
   
    def EmprestarLivro(self, usuario):
        if self.status != "Disponivel":
            return 
        
        self.usuario = usuario
        self.status = 'Emprestado'


    def DevolverLivro(self):
        if self.status != "Emprestado":
            return 'Não pode ser devolvido!!'
        
        self.usuario = None
        self.status = "Disponivel"

    def castradarLivro(self):
        return 'INSERT INTO livro (titulo, autor, genero, status, codigo) VALUES(%s,%s,%s,%s,%s)'

    def excluirLivro(self):
        return 'delete from livro where id_usuario = 1'
    
    def atualizarLivro(self):
        return 'uptade livro set email = %s, titulo = %s, autor = %s, isbn = %s, genero = %s where id_livro = %s'
    
    def consultaLivro(self, titulo = None, autor = None, isbn = None, genero= None):
        if titulo:
            return 'select * from livro where titulo = (%s)'
        elif autor:
            return 'select * from livro where autor = (%s)'
        elif isbn:
            return 'select * from livro where autor = (%s)'
        elif genero:
            return 'select * from livro where genero = (%s)'
        
    
