from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()
admin = Admin()


'''
class User(db.Model):
    __tablename__ = 'user'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    #name = db.Column(db.Text, unique=True)
    #username = db.Column(db.Text, unique=True)
    #salt = db.Column(db.Text, nullable=False)
    #password = db.Column(db.Text, nullable=False)
admin.add_view(ModelView(User, db.session))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return self.name
'''

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    model = db.Column(db.Text, nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Boolean, nullable=False)
    reference = db.Column(db.Text)


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    duration_seconds = db.Column(db.Integer)


class TestQuestion(db.Model):
    __tablename__ = 'test_question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question_index = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('test_id', 'question_index', name='uq_test_question_index'),
        Index('idx_test_question_test_id', 'test_id'),
    )


class Submission(db.Model):
    __tablename__ = 'submission'
    test_question_id = db.Column(db.Integer, db.ForeignKey('test_question.id'), primary_key=True, nullable=False)
    answer = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return self.name


"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP,
    UniqueConstraint, Index, create_engine
)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
      pass


db = SQLAlchemy(model_class=Base)



#from sqlalchemy.orm import declarative_base, sessionmaker, relationship, scoped_session
#
#Base = declarative_base()
#Session = scoped_session(sessionmaker())

'''
def get_db_session(app):
    engine = create_engine(f"sqlite:///{app.config['DATABASE']}")
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return Session()
'''


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, unique=True, nullable=False)
    salt = Column(Text, nullable=False)
    password = Column(Text, nullable=False)


class Question(db.Model):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    model = Column(Text, nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Boolean, nullable=False)
    reference = Column(Text)


class Test(db.Model):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    duration_seconds = Column(Integer)


class TestQuestion(db.Model):
    __tablename__ = 'test_question'
    id = Column(Integer, primary_key=True, autoincrement=True)
    test_id = Column(Integer, ForeignKey('test.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
    question_index = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('test_id', 'question_index', name='uq_test_question_index'),
        Index('idx_test_question_test_id', 'test_id'),
    )


class Submission(db.Model):
    __tablename__ = 'submission'
    test_question_id = Column(Integer, ForeignKey('test_question.id'), primary_key=True, nullable=False)
    answer = Column(Boolean, nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    """
