from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# initialize flask
def create_app():
    app = Flask(__name__) # name of the file
    app.config['SECRET_KEY'] = 'secret key name'
	
	# register routes
	# register blueprints for routes

    return app # inialize flask finished