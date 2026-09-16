from flask import Blueprint, render_template, request, redirect, url_for, session
from models.produto import Produto

loja_route = Blueprint('loja', __name__)

@loja_route.route('/loja', methods=['GET', 'POST'])
def exibir_loja():
    if 'usuario' not in session:
        return redirect(url_for('login.acessar'))

    if request.method == 'POST':
        preco_item = float(request.form.get('preco'))
        session['carrinho'] += preco_item
        session.modified = True

    produtos_db = Produto.query.limit(5).all()
    total = session.get('carrinho', 0.0)
    
    return render_template('loja.html', produtos=produtos_db, total=total)

@loja_route.route('/caixa')
def caixa():
    if 'usuario' not in session:
        return redirect(url_for('login.acessar'))
        
    total_final = session.get('carrinho', 0.0)
    session.clear()
    return render_template('caixa.html', total=total_final)