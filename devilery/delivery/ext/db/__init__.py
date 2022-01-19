from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy () #registrando o db

def init_app(app):
    db.init_app(app)

