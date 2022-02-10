from flask import Blueprint, render_template, current_app, redirect
from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("entrei na funcao main")
    return render_template("index.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit(): #passa os valores do formulario se tudo estiver ok
        create_user(
            email=form.email.data,
            password=form.password.data
        )
        return redirect("/")
    
    return render_template("userform.html", form=form)


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

    