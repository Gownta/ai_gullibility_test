import os
import uuid
from flask import Flask, session, render_template, url_for
    #Blueprint, flash, g, redirect, render_template, request, url_for
from flask_admin import Admin
from .models import db, add_views


def create_app(test_config=None):
    # Create the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Load the config - prod or test
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='mysecret',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite3",
        )
    else:
        app.config.from_mapping(test_config)

    # Create the database and admin views
    admin = Admin(name='AI Gullibility Admin')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    admin.init_app(app)
    add_views(admin)

    @app.before_request
    def start_session():
        if 'user_id' not in session:
            session['user_id'] = str(uuid.uuid4())

    @app.route('/')
    def index():
        return render_template('landing.html')

    @app.route('/test', methods=("POST",))
    def start_test():
        return ""

    return app
