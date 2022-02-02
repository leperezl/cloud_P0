from app import app
from models import *
from flask_jwt import JWT, jwt_required, current_identity

@app.route('/')
def home():
    true

@app.route('/user/<email>')
def profile(email):
    true

@app.route('/home')
def profile(email):
    true

@app.route('/detail')
def profile(email):
    true