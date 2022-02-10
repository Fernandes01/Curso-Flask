import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.auth.controller import create_user
    
@click.option("--email", "-e") # pegar o valor da linha de comando
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    user = create_user(
        email = email,
        password = passwd,
        admin = admin
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"Usuario {email} criado com sucesso!")



def list_users():
    users = User.query.all()
    click.echo("lista de usuarios")