import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Global Variables

TEMPLATE_FOLDER='../templates'
STATIC_ROOT='../static'

# Application

app = Flask(__name__, template_folder = TEMPLATE_FOLDER, static_folder = STATIC_ROOT)

app.config['SECRET_KEY'] = "askdjf$23aaskjASDF231"

DEBUG = os.getenv('DEBUG', True)

print("DEBUG: " + str(DEBUG))

# Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if DEBUG == "True":
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brady:Xde782bUP6m1F@flask-postgres.c8bgqppoeakl.us-west-1.rds.amazonaws.com:5432/flaskapp'

db = SQLAlchemy(app)

migrate = Migrate(app, db)