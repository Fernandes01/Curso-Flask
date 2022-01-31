from flask_admin.contrib.sqla import ModelView # modelview adiciona classe admistrativa
from flask_admin.actions import action #seleciona todos e modifica
from flask_admin.contrib.sqla import filters
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash
from sqlalchemy import column

def format_user(self, request, user, *args):
    return user.email.split('@')[0]

class UserAdmin(ModelView):
    """Interface admin de user"""

    column_formatters = {"email":format_user}

    column_list = ["email","admin"] # mostra os campos

    column_searchable_list = ["email"] # pesquisa

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]



    #can_edit = False # desativa a edição do administrador
    can_create = True # ""     "   criação ""  ""
    can_delete = True # ""     "   deleção ""  ""

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure'
    )
    def toggle_admin_status (self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash (f"{len(users)} Usuarios alterados com sucesso!", "success")


    @action(
        'send_email',
        'Send email to all users',
        'tem certeza que pode enviar?'
    )
    def send_email (self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form de mensagem de email
        # 2) enviar o email
        flash (f"{len(users)} emails enviados com sucesso!", "success")
