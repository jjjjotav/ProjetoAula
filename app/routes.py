from app import app
from flask import render_template, request, flash, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
import sqlite3
from app.forms import Cadastro



@app.route('/')
def index():
    return render_template('index.html', title = 'Pagina inicial')

@app.route('/PaginaInicial')
def PaginaInicial():
    return render_template('index.html', title = 'Pagina inicial')

@app.route('/Projetos')
def Projetos():
    return render_template('Projetos.html', title = 'Projetos')

@app.route('/Blog')
def Blog():
    return render_template('Blog.html', title = 'Blog')

@app.route('/Sobre')
def Sobre():
    return render_template('Sobre.html', title = 'Sobre')

@app.route('/CadastreUsuario')
def CadastreUsuario():
    cadastro = Cadastro()
    nome = cadastro.nome.data
    email = cadastro.email.data
    senha = cadastro.senha.data

    if cadastro.validate_on_submit():
        flash('Cadastrado')

    return render_template('CadastreUsuario.html', title = 'Cadastar Usuario', cadastro = cadastro)

@app.route('/Login')
def Login():
    return render_template('Login.html', title = 'Login')

@app.route('/dados', methods=['POST'])
def dados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    conn = sqlite3.connect('BancoDB.sqlite')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cadastroUser(nome, email, senha)
            VALUES (?, ?, ?)
        ''', (f'{nome}', f'{email}', f'{senha}'))
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

    if len(senha) != 0:
        flash('DADOS CADASTRADO!!')
    return redirect('/CadastreUsuario')






@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    data = request.get_json(force=True)
    name = data['name']
    password = data['password']

    print(f'Nome: {name}\nPassword: {password}')



@app.route('/teste')
def teste():
    return render_template('testeee.html')






