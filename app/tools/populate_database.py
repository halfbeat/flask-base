import sqlalchemy
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from ..models import Proyecto

sys.path.append("../..")
sys.path.append("../models.py")

engine = create_engine('sqlite:///../../instance/miniblog.db', echo=True)
Session = sessionmaker(bind=engine)

proyectos = Proyecto.query.all()
for proyecto in proyectos:
    print(proyecto)