from slugify import slugify
from flask import url_for
from sqlalchemy.exc import IntegrityError
from datetime import date
from app import db


class TipoProyecto(db.Model):
    __tablename__ = 'TIPO_PROYECTO'

    id = db.Column('C_TP_PROYECTO_ID', db.Integer, primary_key=True)
    descripcion = db.Column('D_DESCRIPCION', db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit() 


class LenguajeProgramacion(db.Model):
    __tablename__ = 'LENGUAJE_PROGRAMACION'

    id = db.Column('C_LENGUAJE_ID', db.String(32), primary_key=True)

lenguaje_proyecto = db.Table('LENGUAJES_PROYECTOS', db.Model.metadata,
    db.Column('C_PROYECTO_ID', db.Integer, db.ForeignKey('PROYECTOS.C_PROYECTO_ID'), primary_key=True),
    db.Column('C_LENGUAJE_ID', db.String(32), db.ForeignKey('LENGUAJE_PROGRAMACION.C_LENGUAJE_ID'), primary_key=True)
)

class Proyecto(db.Model):
    __tablename__ = 'PROYECTOS'

    id = db.Column('C_PROYECTO_ID', db.Integer,
                   primary_key=True, autoincrement=True)
    nombre = db.Column('D_PROYECTO', db.String(256), nullable=False)
    descripcion = db.Column('D_DESCRIPCION', db.String(256), nullable=True)
    tipo = db.Column(db.Integer, db.ForeignKey(
        'TIPO_PROYECTO.C_TP_PROYECTO_ID', ondelete='CASCADE'), nullable=False)
    lenguajes = db.relationship("LenguajeProgramacion", secondary=lenguaje_proyecto)
    fecha_creacion = db.Column('F_CREACION', db.DateTime, nullable=False, default = date.today())

    def __repr__(self):
        return f"<Proyecto {self.nombre}"

    @staticmethod
    def get_by_id(id):
        return Proyecto.query.get(id)

    @staticmethod
    def get_all():
        return Proyecto.query.all()
    
    def save(self):
        db.session.add(self)
        db.session.commit()   

    def delete(self):
        db.session.delete(self)
        db.session.commit()      


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{slugify(self.title)}-{count}'

    def public_url(self):
        return url_for('show_post', slug=self.title_slug)

    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(title_slug=slug).first()

    @staticmethod
    def get_all():
        return Post.query.all()
