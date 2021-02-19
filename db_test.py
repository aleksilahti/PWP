import os
import pytest
import tempfile

# import db
import db as app
from db import Topic

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
    
# from course material and last years project    
    
# Topic table test

def test_Topics(db_handle):
    
    # Test creating
    topic = Topic(name='nametest')
    db_handle.session.add(topic)
    db_handle.session.commit()
    assert Topic.query.count() == 1

    # Test the name
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
    
    