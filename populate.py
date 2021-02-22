from db import db, Topic, Question, Answer, Comment, User, Quiz
from datetime import datetime

db.create_all()
print('Database created!')
print('Populating...')

## create Topic resource to db
tmp = Topic(
    name = 'Test_topic_name'
    )
db.session.add(tmp)
db.session.commit()
print('Added Topic')

## create Question resource to db
tmp = Question(
    topic_id = 1,
    question_text = 'test_topic_id',
    image_src = 'test_img_link'
    )
db.session.add(tmp)
db.session.commit()
print('Added Question')

## create Answer resource to db
tmp = Answer(
    question_id = 1,
    answer_text = 'test_answer_text',
    explanation_text = 'test_explanation_text',
    is_correct = 1
    )
db.session.add(tmp)
db.session.commit()
print('Added Answer')

## create Comment resource to db
tmp = Comment(
    user_id = 1,
    question_id = 1,
    comment_text = 'test_comment_text'
    )
db.session.add(tmp)
db.session.commit()
print('Added Comment')

## create User resource to db
tmp = User(
    username = 'test_username',
    email = 'test_email',
    pw_hash = 'test_pw_hash'
    )
db.session.add(tmp)
db.session.commit()
print('Added User')

## create Quiz resource to db
tmp = Quiz(
    user_id = 1,
    created = datetime.now(),
    completed = datetime.now(),
    result = 'test_result',
    number_of_questions = 1
    )
db.session.add(tmp)
db.session.commit()
print('Added Quiz')



