from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)