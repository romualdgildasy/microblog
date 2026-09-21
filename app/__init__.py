from flask import Flask
from config import Config

app = Flask(__name__)
#appel de la methode de configuration 
app.config.from_object(Config)

from app import routes