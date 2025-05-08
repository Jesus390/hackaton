from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Crear las tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()

    # Puedes seguir registrando más blueprints, como main, etc.
    return app
