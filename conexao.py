import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# Criando tabela na biblioteca

# cursos.execute('CREATE TABLE biblioteca(id INT, autor VARCHAR(100), livro VARCHAR(100), editora VARCHAR(100), ISBN INT);')

# Inserindo VALUES na tabela Biblioteca

# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(1,"Gabriel García Márquez","Cem anos de solidão",50)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(2,"Clarice Lispector","Água Viva",30)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(3,"Clarice Lispector","A hora da estrela",45)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(4,"Machado de Assis","Dom Casmurro",22)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(4,"Machado de Assis","Memórias Póstumas de Brás Cubas",15)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(5,"Fiódor Dostoévski","Crime e Castigo",10)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(6,"Djamila Ribeiro","Pequeno manual Antirracista",50)')
# cursor.execute('UPDATE biblioteca SET id=2 WHERE autor="Clarice Lispector"')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(3,"Anne Frank","O diário de Anne Frank",5)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(7,"J. K. Rowling","Harry Potter. E a pedra Filosofal",3)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(8,"Cecília Meirelles","O menino azul",2)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(9,"Sêneca","De Ira",5)')
# cursor.execute('INSERT INTO biblioteca(id, autor, livro, cópias) VALUES(10,"Aldous Huxley","Admirável mundo novo",6)')

# Adicionando chave secundária ISBN:

# dados = cursor.execute('UPDATE biblioteca SET ISBN=011222333 WHERE livro="Cem anos de solidão"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=00023211111 WHERE livro="Água Viva"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=1223312 WHERE livro="Ninguém escreve ao coronel"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002003 WHERE livro="A hora da estrela"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002004 WHERE livro="Dom Casmurro"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002005 WHERE livro="Memórias Póstumas de Brás Cubas"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002006 WHERE livro="Crime e Castigo"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002007 WHERE livro="Pequeno manual Antirracista"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002008 WHERE livro="O diário de Anne Frank"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002009 WHERE livro="Harry Potter. E a pedra Filosofal"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002010 WHERE livro="O menino azul"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002011 WHERE livro="De Ira"')
# dados = cursor.execute('UPDATE biblioteca SET ISBN=001002012 WHERE livro="Admirável mundo novo"')

# Adicionando editora:

# dados = cursor.execute('UPDATE biblioteca SET editora="RECORD" WHERE livro="Cem anos de solidão"')
# dados = cursor.execute('UPDATE biblioteca SET editora="RECORD" WHERE livro="Ninguém escreve ao coronel"')
# dados = cursor.execute('UPDATE biblioteca SET editora="ROCCO" WHERE livro="Água Viva"')
# dados = cursor.execute('UPDATE biblioteca SET editora="ROCCO" WHERE livro="A hora da estrela"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Thoth" WHERE livro="Dom Casmurro"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Antofágica" WHERE livro="Memórias Póstumas de Brás Cubas"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Editora 34" WHERE livro="Crime e Castigo"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Companhia das Letras" WHERE livro="Pequeno manual Antirracista"')
# dados = cursor.execute('UPDATE biblioteca SET editora="RECORD" WHERE livro="O diário de Anne Frank"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Bloomsbury Publishing" WHERE livro="Harry Potter. E a pedra Filosofal"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Global Editora" WHERE livro="O menino azul"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Camelot Editora" WHERE livro="De Ira"')
# dados = cursor.execute('UPDATE biblioteca SET editora="Biblioteca Azul" WHERE livro="Admirável mundo novo"')


dados = cursor.execute('SELECT * FROM biblioteca')
for biblioteca in dados:
    print(biblioteca)

conexao.commit()
conexao.close

