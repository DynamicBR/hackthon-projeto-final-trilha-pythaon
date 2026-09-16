from flask import Flask

from models.banco import db, iniciar_banco
from models.produto import Produto

from views.login import login_route
from views.loja import loja_route

app = Flask(__name__)

iniciar_banco(app)

app.register_blueprint(login_route)
app.register_blueprint(loja_route)

app.app_context().push()
db.create_all()

if not Produto.query.first():
    itens = [
        Produto(nome="Teclado Mecânico", preco=250.0),
        Produto(nome="Mouse Sem Fio", preco=85.0),
        Produto(nome="Monitor Portátil", preco=800.0),
        Produto(nome="Headset Bluetooth", preco=320.0),
        Produto(nome="Suporte de Notebook", preco=45.0)
    ]
    db.session.add_all(itens)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)