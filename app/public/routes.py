from flask import abort, render_template

from . import public_bp
from app.models import posts


@public_bp.route("/")
def index():
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("public/post_view.html", slug_title=slug)    