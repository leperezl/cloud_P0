from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask (__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
api= Api(app)


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

@app.route('/user/<id>', methods=['GET'])
def get_user():
    return ''

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method = 'sha256')
    new_user = User(email=data['email'], password= hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created'})

if __name__=='__main__':
    app.run(debug = True)
    #, host = '0.0.0.0'