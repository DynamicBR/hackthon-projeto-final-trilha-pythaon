from flask import Blueprint, render_template, request, redirect, url_for, session
from models.banco import db
from models.usuario import Usuario

login_route = Blueprint('login', __name__)

@login_route.route('/', methods=['GET', 'POST'])
def acessar():
    if request.method == 'POST':
        acao = request.form.get('acao')
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if acao == 'cadastrar':
            novo_usuario = Usuario(nome=nome, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            
            session['usuario'] = novo_usuario.nome
            session['carrinho'] = 0.0
            return redirect(url_for('loja.exibir_loja'))
            
        elif acao == 'entrar':
            user = Usuario.query.filter_by(nome=nome).first()
            if user and user.senha == senha:
                session['usuario'] = user.nome
                session['carrinho'] = 0.0
                return redirect(url_for('loja.exibir_loja'))
                
    return render_template('login.html')