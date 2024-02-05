import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('banco') #conect ao arquivo biblioteca

cursor = conexao.cursor()


# #conexao.execute('CREATE TABLE Emprestimos (\
#                 id INTEGER PRIMARY KEY,\
#                 ISBN INTEGER,\
#                 id_usuario INTEGER,\
#                 data_emprestimo DATE,\
#                 data_devolucao DATE,\
#                 Estado_do_Exemplar VARCHAR(30),\
#                 FOREIGN KEY(ISBN) REFERENCES livros(id),\
#                 FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

cursor.execute('INSERT INTO Emprestimos(id_usuario,data_emprestimo,data_devolucao,Estado_do_Exemplar) VALUES()')

conexao.commit() #envia as informações

conexao.close() #bom deixar para nao dar conflito