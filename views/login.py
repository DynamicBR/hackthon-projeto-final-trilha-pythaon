from flask import Blueprint, render_template, request, redirect, url_for, session
from models.banco import db
from models.usuario import Usuario

login_route = Blueprint('login', __name__)

@login_route.route('/', methods=["GET", "POST"])
def acessar():
    if request.method == 'POST':
        acao = request.form.get('acao')
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if acao == 'cadastrar':
            novo_usuario = Usuario(nome=nome, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()

            session['usuario'] = usuario.nome
            session['carrinho'] = 0.0
            return redirect(url_for())

        elif acao == 'entrar':
            usuario = Usuario.query.filter_by(nome=nome).first()
            if usuario and usuario.senha == senha:
                session['usuario'] = usuario.nome
                session['carrinho'] = 0.0
                return redirect(url_for())

    return render_template('login.html')