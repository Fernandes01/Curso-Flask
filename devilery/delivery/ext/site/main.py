from flask import Blueprint
from flask import request, render_template

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template(
        "index.html",
        name=request.args['name']
    )
