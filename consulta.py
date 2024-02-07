import sqlite3

# Conectar ao banco de dados ou criar um novo
conexao = sqlite3.connect('banco') #conect ao arquivo biblioteca

cursor = conexao.cursor()
#ATIVIDADE1 FEITA
# - Listar todos os livros disponíveis
# dados = cursor.execute('SELECT * FROM livros')
# for livros in dados:
#     print(livros)

# Encontrar todos os livros emprestados no momento

dados2 = cursor.execute('SELECT * FROM Emprestimos WHERE Estado_do_Exemplar= "Emprestado"')
for livros in dados2:
     print(livros)

# Localizar os livros escritos por um autor específico
# dados = cursor.execute('SELECT * FROM Livros WHERE autor= "Anne Frank"')
# for livros in dados:
#     print(livros)

# Verificar o número de cópias disponíveis de um determinado livro
# dados1 = cursor.execute('SELECT cópias FROM livros WHERE título="Dom Casmurro"')
# for livros in dados1:
#     print(livros)
# Mostrar os empréstimos em atraso.
# cursor.execute('SELECT livros.título, usuários.nome,empréstimos.data_de_empréstimo, empréstimos.data_de_devolução,\
#                 FROM emprestimos\
#                 INNER JOIN empréstimos ON livros.id_do_livro = empréstimos.id_do_livro')
# delete remover um autor
# cursor.execute('DELETE  FROM Livros WHERE autor ="Clarice Lispector"')
# remover um livro

# cursor.execute('DELETE FROM livros WHERE título="O menino azul"')
# marcar um livro como devolvido

# cursor.execute('UPDATE Livros SET Estado_do_Exemplar = "devolvido" WHERE título=""')

# cursor.execute('UPDATE Livros SET Exemplares_disponiveis = Exemplares_disponiveis - 1 WHERE titulo="SENHOR DOS ANEIS"')

conexao.commit()
conexao.close()