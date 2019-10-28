from flask import Flask, render_template

import sqlite3

#app = Flask(__name__)

connection = sqlite3.connect('database2.db')


cursor = connection.cursor()

cursor.execute(
'''
CREATE TABLE IF NOT EXISTS ponto_turistico(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lugar TEXT NOT NULL
)
'''
)

cursor.execute(
'''
CREATE TABLE IF NOT EXISTS passeios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    guia TEXT NOT NULL,
    hora TEXT NOT NULL,
    ponto_turist TEXT NOT NULL,

    FOREIGN KEY (ponto_turist) REFERENCES ponto_turistico(name)
)
'''
)

cursor.execute(
'''
INSERT INTO ponto_turistico(name, lugar)
VALUES ("Cristo Redentor", "Rio de Janeiro"), ("Sao Januario", "Rio de Janeiro"), ("Dacia Arena", "Udine");

'''
)

#cursor.execute(
'''
INSERT INTO passeios(guia, hora, ponto_turist)
VALUES ("Jose", "12:00", "Cristo Redentor"), ("Magno", "13:00", "Sao Januario"), ("Antonio", "15:00", "Dacia Arena");
'''
#)

x = str(input("Escreva o nome do lugar para checar seus pontos turisticos: "))
#x = "'" + x + "'"

lista1 = cursor.execute(
'''
SELECT name FROM ponto_turistico WHERE lugar = ''' + "'" + x + "'"
).fetchall()

print(lista1)
print(lista1[0][0])

x = str(input("Escreva o nome do ponto turistico para checar seus passeios: "))
x = "'" + x + "'"

lista2 = cursor.execute(
'''
SELECT guia, hora FROM passeios WHERE ponto_turist = '''+x+'''
'''
).fetchall()

print(lista2)

connection.commit()

connection.close()


#@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/login')
def login():
    return render_template('Login.html')

#if __name__ == '__main__':
#    app.run(debug=True)