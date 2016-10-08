import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

#cria, na tabela Tracks, uma linha com valores nas colunas title e play, passados por
#meio de um tuple, por isso "( ? , ? )", usado para evitar SQL injection.
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
    ( 'Thunderstruck', 20 ) )
    
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
    ( 'Acerê', 20 ) )
    #outra linha
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
    ( 'My Way', 15 ) )
    #commit é executado por conn, e força os dados a serem escritos no database.
conn.commit()


print ('Tracks:')
#SELECT recupera os dados das linhas, com o conteudo das colunas que queremos.
#aqui, queremos o conteudo de title, e plays, da tabela Tracks.
cur.execute('SELECT title, plays FROM Tracks')
#cur é o numero total de linhas na tabela
for row in cur :
    #row é o conteudo da linha
   print (row)
print("\n")   

# * significa todas as colunas
cur.execute('SELECT * FROM Tracks WHERE plays = 20') #podemos usar <=,>=,!=, AND e OR, ...
print ("essas musicas tem 20 plays")
for row in cur :
    print (row)
print("\n") 

#SELECT usando ORDER BY
cur.execute('SELECT title,plays FROM Tracks ORDER BY title')
print("ordem alfabetica")
for row in cur :
    print (row)
print("\n")
    
#tambem é possivel atualizar o conteudo de uma coluna para uma ou mais linhas usando
#UPDATE, se nao especificado WEHERE, alterará a(s) coluna(s) para todas as linhas.
#aqui precisamos usar " para identificar o texto a ser procurado
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "My Way"')
cur.execute('SELECT title,plays FROM Tracks ORDER BY title')
for row in cur :
    print (row)
print("\n")

#DELETE deleta linhas de certa tabela, com o criteiro WHERE especificado.
#para deletar linhas, precisamos usar DELETE com um WHERE especificando as diretrizes
#da deleçao 
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()