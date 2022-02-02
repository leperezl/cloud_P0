import os
SECRET_KEY = 'Justthe2ofus'# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))# Enable debug mode.
DEBUG = True# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False