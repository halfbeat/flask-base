from flask import render_template
from . import proyectos_bp
from app.models import Proyecto

@proyectos_bp.route("/proyectos/")
def index():
    proyectos = Proyecto.query.all()
    return render_template("proyectos/index.html", proyectos=proyectos)