from flask import Flask
from config import Config
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#appel de la methode de configuration 
app.config.from_object(Config)
#initialisation de la base de données
db = SQLAlchemy(app)
#initialisation de la migration de la base de données
migrate = Migrate(app, db)

from app import routes,models