from db import db, Topic, Question

db.create_all()
print('Database created!')
print('Populating...')


## create Topics resource to db
tmp = Topic(
    name='Test_topic_name'
    )
db.session.add(tmp)
db.session.commit()
print('Added Topic')

## create Questions resource to db
tmp = Question(
    quiz_id='Test_quiz_id'
    )
db.session.add(tmp)
db.session.commit()
print('Added Question')