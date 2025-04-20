from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

'''
db = SQLAlchemy()
admin = Admin()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="posts")


class PostView(ModelView):
    can_delete = False
    form_columns = ["title", "body", "user"]
    column_list = ["title", "body", "user"]

admin.add_view(ModelView(User, db.session))
admin.add_view(PostView(Post, db.session))
'''

def create_app():
    from .models import db, admin
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "mysecret"

    db.init_app(app)
    with app.app_context():
        db.create_all()
    admin.init_app(app)

    return app



"""
import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
      pass
db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    '''
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    '''

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    #from . import db
    #db.init_app(app)

    #from . import auth
    #app.register_blueprint(auth.bp)

    #from . import blog
    #app.register_blueprint(blog.bp)
    #app.add_url_rule('/', endpoint='index')

    #from .models import db, User, Question, Test, TestQuestion, Submission

    #from sqlalchemy import (
    #    Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP,
    #    UniqueConstraint, Index, create_engine
    #)
    #from sqlalchemy.orm import DeclarativeBase



    from sqlalchemy import (
        Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP,
        UniqueConstraint, Index, create_engine
    )
    from sqlalchemy import Integer, String
    from sqlalchemy.orm import Mapped, mapped_column



    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + app.config['DATABASE'] # 'sqlite:///test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tdb4'
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    class XUser(db.Model):
        __tablename__ = 'yuser'
        id: Mapped[int] = mapped_column(primary_key=True)
        username: Mapped[str] = mapped_column(unique=True)
        email: Mapped[str]
    with app.app_context():
        db.create_all()

    admin = Admin(app, name='AI Gullibility Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(XUser, db.session))
    return app
"""
