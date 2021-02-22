import os
import pytest
import tempfile

# import db
import db as app
from db import Topic, Question, Answer, Comment, User, Quiz

# import integrityerror
from sqlalchemy.exc import IntegrityError



# from course material

@pytest.fixture
def db_handle():
    db_fd, db_fname = tempfile.mkstemp()
    app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.app.config["TESTING"] = True
    
    with app.app.app_context():
        app.db.create_all()
        
    yield app.db
    
    app.db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)
    
# from course material (and last years project)
    
# Topic table test

def test_Topic(db_handle):
    """
    Topic has:
    class Topic(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(256), nullable=True)

        questions = db.relationship("Question", back_populates="topic")
    """
    # Test creating
    topic = Topic(name='nametest')
    db_handle.session.add(topic)
    db_handle.session.commit()
    assert Topic.query.count() == 1

    # Check the name
    topic = Topic.query.filter_by(name='nametest').first()
    assert topic.name == 'nametest'
    
    # Test deleting
    topic = Topic(name='addtest')
    db_handle.session.add(topic)
    db_handle.session.commit()
    # should be 2 now
    assert Topic.query.count() == 2
    
    topic = Topic.query.filter_by(name='addtest').first()
    db_handle.session.delete(topic)
    db_handle.session.commit()
    # deleted?
    assert Topic.query.count() == 1
    topic = Topic.query.first()
    assert topic.name == 'nametest'
    
def test_Question(db_handle):
    """
    class Question(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        topic_id = db.Column(db.Integer, db.ForeignKey("topic.id", ondelete="SET NULL"))
        question_text = db.Column(db.String(256), nullable=False)
        image_src = db.Column(db.String(256), nullable=True)
        
        topic = db.relationship("Topic", back_populates="questions")
        
        answers = db.relationship("Answer", cascade="all, delete-orphan", back_populates="question")
        comments = db.relationship("Comment", cascade="all, delete-orphan", back_populates="question")
    """
    
    # Test creating
    question = Question(question_text='test_question_text')
    db_handle.session.add(question)
    db_handle.session.commit()
    assert Question.query.count() == 1
    
    # Check the question_text
    question = Question.query.filter_by(question_text='test_question_text').first()
    assert question.question_text == 'test_question_text'
    
    # Test deleting
    question = Question(question_text='add_question_text')
    db_handle.session.add(question)
    db_handle.session.commit()
    # should be 2 now
    assert Question.query.count() == 2
    
    question = Question.query.filter_by(question_text='add_question_text').first()
    db_handle.session.delete(question)
    db_handle.session.commit()
    # deleted?
    assert Question.query.count() == 1
    question = Question.query.first()
    assert question.question_text == 'test_question_text'
    
    