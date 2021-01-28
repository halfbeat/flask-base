# config/prod.py

from .default import *

import os

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:testing@192.168.1.140:5432/miniblog'