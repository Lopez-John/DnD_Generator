from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Character(DB.Model):
    