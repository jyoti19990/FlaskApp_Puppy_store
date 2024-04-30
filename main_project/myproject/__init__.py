import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'mykey1'

###############DB Connection Sections################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'puppy_database1.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
from main_project.myproject.owners.views import owner_view
from main_project.myproject.puppies.views import puppies_blueprint
app.register_blueprint(owner_view, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
