# config/dev.py

from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:testing@192.168.1.142:5432/miniblog'