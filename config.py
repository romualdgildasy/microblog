import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #configuration de la clé secrète pour la sécurité des formulaires
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #connexion à la base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')