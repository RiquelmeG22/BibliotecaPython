
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
        return 'delete from livro where id_livr = 1'
    
    def atualizarLivro(self):
        return 'uptade livro set email = %s, titulo = %s, autor = %s, isbn = %s, genero = %s where id_livro = %s'
    
    @staticmethod
    def consultaLivro(self, id_livro= None, titulo=None, autor=None, genero=None, isbn=None):
        query = "SELECT * FROM livro"
        conditions = []

        if id_livro:
            conditions.append("id_livro = %s")
         
        if titulo:
            conditions.append("titulo = %s")
    
        if autor:
            conditions.append("autor = %s")
           
        if genero:
            conditions.append("genero = %s")
           
        if isbn:
            conditions.append("isbn = %s")
             
        if conditions:
            query += " WHERE " + " AND ".join(conditions)  
     
        return query

