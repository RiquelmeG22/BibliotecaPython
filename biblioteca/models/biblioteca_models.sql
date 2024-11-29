-- Active: 1732798662965@@10.28.2.71@3306@biblioteca

CREATE DATABASE biblioteca;


USE biblioteca;


CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,  
    nome_completo VARCHAR(100),
    email varchar(70) unique,
    senha varchar(50) unique,
    cpf  varchar(13) unique                       
);


CREATE TABLE livro (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,    
    titulo VARCHAR(50),                         
    autor VARCHAR(50),                          
    genero VARCHAR(50),                                            
    isbn INT                                  
);

CREATE TABLE emprestimo (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,  
    id_livro INT,                                 
    id_usuario INT,
    devolucao BOOLEAN,                               
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),   
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) 
);




INSERT INTO livro (titulo, autor, genero, isbn) VALUES
('Pequenino', 'Paulo', 'Comedia', '22');

delete from livro where id_livro = 1

update livro set titulo = 'Pequenino' where id_livro = 1;

select * from livro where titulo = 'Pequenino';


INSERT INTO usuario (nome_completo, email, senha, cpf) VALUES
('João Silva', 'paulo@oi.com', '9876543f1', '1234563891234'),
('Maria Oliveira', 'maria@oi.com', '432423424', '1234567891235'),
('Pedro Costa', 'pedro@oi.com', 'gtrtrtrtrt', '1234567891236'),
('Ana Pereira', 'ana@exemplo.com', 'hhfghfhhf', '1234567891237');

delete from usuario where id_usuario = 1;

update usuario set senha = 'gtrtrtrtrt' where id_usuario = 3;

select * from livro where titulo = 'Ana Perreira';













