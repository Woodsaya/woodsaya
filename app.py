from flask  import Flask
from views import mods
from models import db

def create_app():
    app = Flask(__name__)
    for mod in  mods:
        app.register_blueprint(mod)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://visual:writecleancode@localhost:5432/flaskproj'
    db.init_app(app)
    return app