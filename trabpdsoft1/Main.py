import sqlite3

idnum = 0

conector = sqlite3.connect('databasepdsoft.sqlite3')

cur = conector.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Tabela (nome TEXT,id INTEGER, senha TEXT)')

while(1):
    idnum+=idnum
    querer=input("deseja criar um novo usuario? (s/n)\n")
    if querer in 's':
        
        usuario=input("digite um novo nome de usuario:\n")
        senha=input("digite uma senha:\n")

        cur.execute('INSERT INTO Tabela (nome, id, senha) VALUES (?, ?, ?)',
                    (usuario,idnum,senha)
                    )
                    
    else:
        break
cur.execute('SELECT * FROM Tabela')
for row in cur:
    print (row)


conector.close()
