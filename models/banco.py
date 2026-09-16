from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def iniciar_banco(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    app.secret_key = '01-hackthon'
    db.init_app(app)
