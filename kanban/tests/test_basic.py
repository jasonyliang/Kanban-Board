# kanban/test_basic.py
 
 
import os
import unittest

import sys
topdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(topdir)

from kanban import app, db
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

 

 
    # executed after each test
    def tearDown(self):
        pass
    
    # user authentication methods
     
    def register(self, username, email, password, confirm):
        return self.app.post(
            '/register',
            data=dict(username=username, email=email, password=password, confirm=confirm),
            follow_redirects=True
        )
     
    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )
     
    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )
 
    #basic tests
    # User authentication tests
    def test_valid_user_registration(self):
        response = self.register('test', 'test@test.com', 'test1', 'test1')
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        response = self.login('test@test.com', 'test1')
        self.assertEqual(response.status_code, 200)

    def test_valid_user_logout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)

    # page tests
    def test_main_page(self):
        #response = self.register('test@test.com', 'test1', 'test')
        #self.login('test@test.com', 'test1')
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_todo_page(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()