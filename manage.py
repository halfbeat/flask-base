from flask_script import Manager
from entrypoint import app
from app.models import Proyecto,TipoProyecto
from app import db
manager = Manager(app)

@manager.command
def populate_database():    
    tipo = TipoProyecto(id=1, descripcion="INTERNO")
    tipo.save()
    proyecto = Proyecto(nombre='AYCI', descripcion='Prueba de proyecto', tipo=tipo.id)
    proyecto.save()
    proyectos = Proyecto.query.all()
    for proyecto in proyectos:
        print(proyecto.nombre)


@manager.command
def delete_database():    
    proyectos = Proyecto.query.all()
    for proyecto in proyectos:
        db.session.delete(proyecto)        

    tipos_proyecto = TipoProyecto.query.all()
    for tipo_proyecto in tipos_proyecto:
        db.session.delete(tipo_proyecto)
                
    db.session.commit()

if __name__ == "__main__":
    manager.run()