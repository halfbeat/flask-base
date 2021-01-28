from flask_restful import Resource
from app import oidc
from flask import request

from .schemas import InfoSchema, PeriodoSchema


class InfoResource(Resource):
    def get(self):
        info_schema = InfoSchema()
        info = {"version": "1.3.2", "author": "adejes@gmail.com"}
        result = info_schema.dump(info,  many=False)
        return result


class PeriodoResource(Resource):
    @oidc.accept_token(require_token=True)
    def get(self):
        print(request.headers['Authorization'])
        periodos = [{"anio": 2020, "programa": "CARNAVAL",
                     "nombre": "CONCILIAMOS CARNAVAL 2020",
                     "anioRenta": 2020, "fechaInicioInscripcion": 0,
                     "fechaFinInscripcion": 0, "fechaInicioInscripcionExtraordinaria": 0},
                    {"anio": 2021, "programa": "CARNAVAL",
                     "nombre": "CONCILIAMOS CARNAVAL 2021",
                     "anioRenta": 2021, "fechaInicioInscripcion": 0,
                     "fechaFinInscripcion": 0, "fechaInicioInscripcionExtraordinaria": 0}]
        return periodos
