import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Global Variables

TEMPLATE_FOLDER='../templates'
STATIC_ROOT='../static'

# Application

app = Flask(__name__, template_folder = TEMPLATE_FOLDER, static_folder = STATIC_ROOT)

app.config['SECRET_KEY'] = "askdjf$23aaskjASDF231"

DEBUG = os.getenv('DEBUG', True)

DEBUG = False

# Database
if DEBUG:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask-postgres.c8bgqppoeakl.us-west-1.rds.amazonaws.com:5432'

db = SQLAlchemy(app)

