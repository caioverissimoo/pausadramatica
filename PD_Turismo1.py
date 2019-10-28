from flask import Flask, render_template, request

import sqlite3

x = ""
y = ""
lista3 = []
lista4 = []
app = Flask(__name__)

connection = sqlite3.connect('database.db')


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
CREATE TABLE IF NOT EXISTS cadastros(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL

)
'''
)


#cursor.execute(
'''
INSERT INTO ponto_turistico(name, lugar)
VALUES ("Cristo Redentor", "Rio de Janeiro"), ("Sao Januario", "Rio de Janeiro"), ("Dacia Arena", "Udine");

'''
#)

#cursor.execute(
'''
INSERT INTO passeios(guia, hora, ponto_turist)
VALUES ("Jose", "12:00", "Cristo Redentor"), ("Magno", "13:00", "Sao Januario"), ("Antonio", "15:00", "Dacia Arena");
'''
#)

#cursor.execute(
'''
INSERT INTO cadastros(usuario, senha)
VALUES ("ab", "cd")

'''
#)


y = "'" + y + "'"

lista2 = cursor.execute(
'''
SELECT guia, hora FROM passeios WHERE ponto_turist = '''+ y +'''
'''
).fetchall()

print(lista2)

connection.commit()

connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/login2', methods = ['POST'])
def login2():
    h = str(request.form["info1"])
    k = str(request.form["info2"])
    lista3 = [h,k]
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    lista4 = cursor.execute(
    '''
    SELECT usuario, senha FROM cadastros WHERE usuario = ''' + "'" + h + "'" 
    ).fetchall()
    print(lista4)
    connection.commit()
    connection.close()
    print(lista3, lista4)
    if (lista4==[]):
        return render_template('hm.html')
    elif(lista3[0] == lista4[0][0] and lista3[1]==lista4[0][1] ):
        return render_template('sucesso.html', usuario = h )
    else:
        return render_template('hm.html')

@app.route('/registrar', methods = ['POST'])
def registrar():
    return render_template('registro.html')

@app.route('/registrar2', methods = ['POST'])
def registrar2():
    h = str(request.form["info3"])
    k = str(request.form["info4"])
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    haux = cursor.execute(
    '''
    SELECT usuario, COUNT() FROM cadastros WHERE usuario = ''' + "'" + h + "'"
    ).fetchall()
    print(h,haux)
    if (haux==[(None, 0)]):
        cursor.execute(
        '''
        INSERT INTO cadastros (usuario)
        VALUES (h)
        ''', (h,)
        )
        cursor.execute(
        '''
        INSERT INTO cadastros (senha) WHERE usuario = ''' + "'" + h + "'" '''
        VALUES (k)
        ''', (k,)
        )
        connection.commit()
        connection.close()
        return render_template ('sucesso2.html', usuario = h)
    else: 
        connection.commit()
        connection.close()
        return render_template ('hm.html')

@app.route('/a')
def a():
    return render_template('a.html')

@app.route('/b', methods =  ['POST'])
def b():
    x = str(request.form["x"])
    """
    cursor = connection.cursor()
    lista1 = cursor.execute(
    '''
    SELECT name FROM ponto_turistico WHERE lugar = ''' + "'" + x + "'" 
    ).fetchall()

    connection.commit()
    connection.close()
    """
    return render_template(x+'.html')

@app.route('/hm')
def hm():
    return render_template('hm.html')

if __name__ == '__main__':
    app.run(debug=True)
