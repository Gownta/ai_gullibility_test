import datetime
from typing import Optional
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    created: Mapped[db.DateTime] = mapped_column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    salt: Mapped[str] = mapped_column(db.String, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=False)

    def __str__(self):
        return self.username


class Question(db.Model):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    created: Mapped[db.DateTime] = mapped_column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    model: Mapped[str] = mapped_column(db.String, nullable=False)
    prompt: Mapped[str] = mapped_column(db.Text, nullable=False)
    response: Mapped[str] = mapped_column(db.Text, nullable=False)
    question: Mapped[str] = mapped_column(db.Text, nullable=False)
    answer: Mapped[str] = mapped_column(db.String(1), nullable=False)  # [T]rue, [F]alse, [U]nknown
    reference: Mapped[Optional[str]] = mapped_column(db.Text)


class Test(db.Model):
    __tablename__ = 'test'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    created: Mapped[db.DateTime] = mapped_column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    duration_seconds: Mapped[Optional[int]] = mapped_column(db.Integer)


class TestQuestion(db.Model):
    __tablename__ = 'test_question'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    test_id: Mapped[int] = mapped_column(db.ForeignKey('test.id'), nullable=False)
    question_id: Mapped[int] = mapped_column(db.ForeignKey('question.id'), nullable=False)
    question_index: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (
        db.Index('idx_test_question_test_id', 'test_id'),
    )


class Submission(db.Model):
    __tablename__ = 'submission'
    test_id: Mapped[int] = mapped_column(db.ForeignKey('test.id'), nullable=False)
    test_question_id: Mapped[int] = mapped_column(db.ForeignKey('test_question.id'), primary_key=True, nullable=False)
    answer: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    created: Mapped[db.DateTime] = mapped_column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)

    __table_args__ = (
        db.Index('idx_submission_test_id', 'test_id'),
    )


def add_views(admin):
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Question, db.session))
    admin.add_view(ModelView(Test, db.session))
    admin.add_view(ModelView(TestQuestion, db.session))
    admin.add_view(ModelView(Submission, db.session))
