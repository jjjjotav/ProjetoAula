from app import app
from flask import render_template, request

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
    return render_template('CadastreUsuario.html', title = 'Cadastar Usuario')

@app.route('/Login')
def Login():
    return render_template('Login.html', title = 'Login')

@app.route('/dados', methods=['POST'])
def dados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    return f"Nome: {nome}\nEmail: {email}\nSenha: {senha}"






