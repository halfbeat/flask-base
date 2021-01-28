from marshmallow import fields
from app import ma

class InfoSchema(ma.Schema):
    version = fields.String(dump_only=True)
    author = fields.String()

class PeriodoSchema(ma.Schema):
    anio: fields.Integer()
    programa: fields.String()
    nombre: fields.String()
    anioRenta: fields.Integer()
    fechaInicioInscripcion: fields.Integer()
    fechaFinInscripcion: fields.Integer()
    fechaInicioInscripcionExtraordinaria: fields.Integer()