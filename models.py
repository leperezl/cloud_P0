from app import db
from app import ma
from app import api 
from flask_login import UserMixin
from flask_restful import Api, Resource


class User(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    email= db.Column(db.String(50))
    password= db.Column(db.String(50))

class Event(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(50))
    category= db.Column(db.String(50))
    location= db.Column(db.String(50))
    address= db.Column(db.String(250))
    iDate= db.Column(db.DateTime)
    fDate= db.Column(db.DateTime)
    presencial = db.Column(db.Boolean)


class User_Schema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password")

user_schema = User_Schema()

class ResourceOneUser(Resource):
    def get(self, id_user):
        user = User.query.get_or_404(id_user)
        return user_schema.dump(user)



