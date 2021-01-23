from flask import abort, render_template
from app.models import Proyecto
from app.models import Post
from . import public_bp


@public_bp.route("/")
def index():
    proyectos = Proyecto.query.all()
    return render_template("public/index.html", proyectos=proyectos)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("public/post_view.html", post=post)  