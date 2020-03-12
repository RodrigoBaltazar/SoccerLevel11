from soccerlevel11.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Video(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    post_date = db.Column(db.DateTime())
    rating = db.Column(db.Integer)
    size = db.Column(db.Integer)

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140), index=True, unique=True)
    password = db.Column(db.String(512))
    #email = db.Column(db.String(120), index=True, unique=True)