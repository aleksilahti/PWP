from db import db, Topic

db.create_all()
print('Database created succesfully!')
print('Populating database...')

tmp = Topic(
    name='Testing'
    )
db.session.add(tmp)
db.session.commit()