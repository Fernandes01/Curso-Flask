import imp
from xmlrpc.client import boolean
from werkzeug.security import (
    generate_password_hash, # recebe texto puro e cria um hash incriptado
    check_password_hash # verifica se o texto gerado é igual ao incriptado
)
from delivery.ext.auth.models import User
from delivery.ext.db import db

ALG = "pbkdf2:sha256"

def create_user(email:str, password: str, admin:boolean = False) -> User:
    password = generate_password_hash(
        password, ALG
    )
    user = User(
        email=email,
        passwd=password,
        admin=admin)
    
    db.session.add(user)
    # TODO: tratar exception caso usuario ja exista
    db.session.commit()
    return user
