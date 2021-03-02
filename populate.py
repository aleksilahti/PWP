from db import db, Topic, Question, Answer, Comment, User, Quiz, quiz_questions
from datetime import datetime

db.create_all()
print('Database created!')
print('Populating...')

## create Topic resource to db
topic1 = Topic(
    name = 'Test_topic_name'
    )
db.session.add(topic1)
db.session.commit()
print('Added Topic')

## create User resource to db
user1 = User(
    username = 'test_username',
    email = 'test_email',
    pw_hash = 'test_pw_hash'
    )
db.session.add(user1)
db.session.commit()
print('Added User')

## create Question resource to db
question1 = Question(
    topic_id = 1, # has to exist
    question_text = 'test_topic_id',
    image_src = 'test_img_link'
    )
db.session.add(question1)
db.session.commit()
print('Added Question')

## create Answer resource to db
answer1 = Answer(
    question_id = 1, # has to exist
    answer_text = 'test_answer_text',
    explanation_text = 'test_explanation_text',
    is_correct = 1
    )
db.session.add(answer1)
db.session.commit()
print('Added Answer')


## create Comment resource to db
comment1 = Comment(
    user_id = 1, # has to exist
    question_id = 1, # has to exist
    comment_text = 'test_comment_text'
    )
db.session.add(comment1)
db.session.commit()
print('Added Comment')

## create Quiz resource to db
quiz1 = Quiz(
    user_id = 1,
    created = datetime.now(),
    completed = datetime.now(),
    result = 'test_result',
    number_of_questions = 1
    )
db.session.add(quiz1)
db.session.commit()
print('Added Quiz')

## appending to table
# TODO fix this
#QuizQuestions.questions.append(quiz1)

