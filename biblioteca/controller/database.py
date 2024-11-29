import mysql.connector

class DataBase:
    def __init__(self) -> None:

        self.conexao = mysql.connector.connect(
        host = '10.28.2.71',
        database = 'biblioteca',
        user = 'suporte',
        password = 'suporte'
        )

        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

if __name__ == '__main__':
    oi = DataBase()
    oi.cursor.execute('select * from livro;')
    tchau = oi.cursor.fetchone()
    print(tchau)





