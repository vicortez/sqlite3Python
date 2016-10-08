import sqlite3

# sqlite3.connect conecta conn a um database "music.sqlite3" ou cria ele se nao existir.
conn = sqlite3.connect('music.sqlite3')

# um cursor é usado para fazer as operacoes necessarias no database.
cur = conn.cursor()

#DROP TABLE remove a tabela. nomes minusculos sao nomes de variaveis, tracks é nossa tabela.
cur.execute('DROP TABLE IF EXISTS Tracks ')

#cria uma tabela chamada Tracks, com duas colunas: title do tipo TEXT e plays do tipo INTEGER
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()