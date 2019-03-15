import os
import unittest

import sys
topdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(topdir)

from flask_testing import TestCase


from kanban import app, db
from kanban.models import Todo, User
from flask_login import login_user
from datetime import datetime

TEST_DB = 'test.db'
 
 
class FunctionTests(unittest.TestCase):
 
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        self.user = User(username="Test", email="Test@test.com", password="password")
        db.session.add(self.user)
        todo = Todo(title="Title", description="Description", deadline=datetime(2019, 3, 16, 0, 0), creator=self.user)
        db.session.add(
            todo)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    # functions tests
    def test_add_todo(self):
        response = self.app.post('/add', 
            data=dict(title="Title", 
            description="Description", 
            deadline="2018-01-01", 
            creator=self.user),
            follow_redirects=True)
        #print(Todo.query.all())
        self.assertEqual(response.status_code, 200)

    def test_do(self):
        response = self.app.get('/do/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_done(self):
        response = self.app.get('/done/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo(self):
        response = self.app.get('/todo/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo(self):
        self.app.get('/done/1', follow_redirects=True)
        response = self.app.get('/delete/1', follow_redirects=True)
        print(Todo.query.all())
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()