# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1><b>Avaliação contínua: Aula 030</b></h1><ul><li><a href="https://giovanna1.pythonanywhere.com/">Home</a></li><li><a href="https://giovanna1.pythonanywhere.com/user/GiovannaKarolline/PT303304X/IFSP">Identificação</a></li><li><a href="https://giovanna1.pythonanywhere.com/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route('/user/GiovannaKarolline/PT303304X/IFSP')
def identificacao():
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Aluna: Giovanna Karolline Menezes Ribeiro</h2><h2>Prontuário: PT303304X</h2><h2>Instituição: IFSP</h2><p><a href="https://giovanna1.pythonanywhere.com/">Voltar</a></p>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

from flask import request
@app.route('/contextorequisicao')
def contextorequisicao():
    requisicao = request.headers.get('User-Agent')
    IP = request.remote_addr
    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {requisicao}</h2><h2>O IP do computador remoto é: {IP}</h2><h2>O host da aplicação é: https://giovanna1.pythonanywhere.com/</h2><p><a href="https://giovanna1.pythonanywhere.com/">Voltar</a></p>'

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    codigo = request.args['codigo']
    return f'<p>{codigo}</p>'

from flask import make_response
@app.route('/objetoresposta')
def objetoresposta():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

from flask import redirect
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

from flask import abort
@app.route('/abortar')
def abortar():
    abort(404)