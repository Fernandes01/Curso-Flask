#inicia a migração quando se atualiza o banco de dados

from flask_migrate import Migrate
from delivery.ext.db import db


migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
