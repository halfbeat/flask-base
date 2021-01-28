from flask import render_template,redirect,url_for, abort
from . import proyectos_bp
from app.models import Proyecto
from flask_login import current_user

@proyectos_bp.route("/proyectos/")
def index():
    proyectos = Proyecto.query.all()
    return render_template("proyectos/index.html", proyectos=proyectos)

@proyectos_bp.route("/proyectos/<int:id_proyecto>")
def proyecto(id_proyecto):
    proyecto = Proyecto.get_by_id(id_proyecto)
    if proyecto is None:
        abort(404)
    return render_template("proyectos/proyecto.html", proyecto=proyecto, tab=1)

@proyectos_bp.route("/proyectos/<int:id_proyecto>/miembros")
def miembros_proyecto(id_proyecto):
    if not current_user.is_authenticated:
        return redirect(url_for('proyectos.proyecto',id_proyecto=id_proyecto))
    proyecto = Proyecto.get_by_id(id_proyecto)
    if proyecto is None:
        abort(404)
    return render_template("proyectos/miembros_proyecto.html", proyecto=proyecto, tab=2)    