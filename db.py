from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

quiz_questions = db.Table("QuizQuestions",
    db.Column("quiz_id", db.Integer, db.ForeignKey("quiz.id"), primary_key=True),
    db.Column("question_id", db.Integer, db.ForeignKey("question.id"), primary_key=True)
)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)

    questions = db.relationship("Question", back_populates="topic")
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id", ondelete="SET NULL"), nullable=True)
    question_text = db.Column(db.String(256), nullable=False)
    image_src = db.Column(db.String(256), nullable=True)
    
    topic = db.relationship("Topic", back_populates="questions")
    
    quizzes = db.relationship("Quiz", secondary=quiz_questions, back_populates="questions")

    answers = db.relationship("Answer", cascade="all, delete-orphan", back_populates="question")
    comments = db.relationship("Comment", cascade="all, delete-orphan", back_populates="question")

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"), nullable=False)
    answer_text = db.Column(db.String(256), nullable=False)
    explanation_text = db.Column(db.String(256), nullable=True)
    is_correct = db.Column(db.Integer, nullable=False) #Boolean value 1 or 0
    
    question = db.relationship("Question", back_populates="answers")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"), nullable=False)
    comment_text = db.Column(db.String(256), nullable=False)

    user = db.relationship("User", back_populates="comments")
    question = db.relationship("Question", back_populates="comments")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    pw_hash = db.Column(db.String(256), nullable=False)

    comments = db.relationship("Comment", back_populates="user")
    quizzes = db.relationship("Quiz", back_populates="user")

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    created = db.Column(db.DateTime, nullable = False) 
    completed = db.Column(db.DateTime, nullable = False)
    result = db.Column(db.String(256), nullable=False)
    
    questions = db.relationship("Question", secondary=quiz_questions, back_populates="quizzes")

    user = db.relationship("User", back_populates="quizzes")
    
db.create_all()