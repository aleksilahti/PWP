from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
quiz_questions = db.Table("QuizQuestions",
    db.Column("quiz_id", db.Integer, db.ForeignKey("quiz.id"), primary_key=True),
    db.Column("question_id", db.Integer, db.ForeignKey("question.id"), primary_key=True)
)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True)

    questions = db.relationship("Question", back_populates="topic")
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id", ondelete="SET NULL"))
    question_text = db.Column(db.String(256), nullable=False)
    image_src = db.Column(db.String(256), nullable=True)
    
    topic = db.relationship("Topic", back_populates="questions")
    
    answers = db.relationship("Answer", cascade="all, delete-orphan", back_populates="question")
    comments = db.relationship("Comment", cascade="all, delete-orphan", back_populates="question")

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"))
    answer_text = db.Column(db.String(256), nullable=False)
    explanation_text = db.Column(db.String(256), nullable=True)
    is_correct = db.Column(db.Integer, nullable=False) #Boolean value 1 or 0
    
    question = db.relationship("Question", back_populates="answers")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"), nullable=False)
    comment_text = db.Column(db.String(256), nullable=False)

    user = db.relationship("User", back_populates="comments")
    question = db.relationship("Question", back_populates="comments")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    pw_hash = db.Column(db.String(256), nullable=False)

    comments = db.relationship("Comment", back_populates="user")
    quizzes = db.relationship("Quiz", back_populates="user")

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    created = db.Column(db.DateTime, nullable = False) 
    completed = db.Column(db.DateTime, nullable = False)
    result = db.Column(db.String(256), nullable=False)
    number_of_questions = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="quizzes")
    
db.create_all()