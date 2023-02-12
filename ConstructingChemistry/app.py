import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()
DB_NAME = "compound_database.db"

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ["secret_key"]
    app.config["UPLOAD_FOLDER"] = os.path.join("static", "compound_images") 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    from .models import Compound

    with app.app_context():
        create_database()

    return app

def create_database():
    if not os.path.exists(DB_NAME):
        db.create_all()
