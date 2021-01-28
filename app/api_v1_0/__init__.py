from flask import Blueprint
from flask_restful import Api, Resource

from .schemas import InfoSchema
from .resources import InfoResource, PeriodoResource

api_v1_0_bp = Blueprint('api_v1_0', __name__)

api = Api(api_v1_0_bp)

api.add_resource(InfoResource, '/api/v1.0/info/', endpoint='version')
api.add_resource(PeriodoResource, '/api/v1.0/periodos/', endpoint='obtener_periodos')