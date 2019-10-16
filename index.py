from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('cadastros.db')
cursor = connection.cursor()

cursor.execute(
"""
create table if not exists logins (
    id integer primary key,
    usuario text not null,
    senha text not null
)
"""
)

cursor.execute(
"""
insert into logins (usuario, senha)
values ("pausa", "dramatica");
"""
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/loginconfirmado')
def entrar():
    """global usuario
    global senha
    usuario = str(request.form["Usuario"])
    senha = str(request.form["Senha"])"""
    return render_template('index.html')


connection.commit()
connection.close()

if __name__ == '__main__':
    app.run(debug=True)