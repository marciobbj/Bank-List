from lister import app

# Instanciamento de BD #

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
