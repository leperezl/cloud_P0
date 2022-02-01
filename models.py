from app import db

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




