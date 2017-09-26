import unittest
import app
from flask import url_for
import sys

class TddInShoppist(unittest.TestCase):
    def setUp(self):
        '''Setup the app for testing'''
        app.app.testing = True
        self.app = app.app.test_client()

    def test_get_root_route(self):
        '''Test access to the GET '/' route'''
        response = self.app.get('/')
        #test if it returns something
        self.assertEqual(response.status_code, 200)

    def test_get_sign_up(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/sign-up')
        #test if it returns something
        self.assertEqual(response.status_code, 200)
        #test if it signs-up


    def test_get_login(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/login')
        #test if it returns something
        self.assertEqual(response.status_code, 200)

    def test_get_logout(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/logout', follow_redirects=True)
        #test if it returns something
        self.assertEqual(response.status_code, 200)

    def  test_post_sign_up(self):
        '''Test if user can sign up'''
        response = self.app.post('/sign-up', data=dict(
            username="joshua",
            email="user@shoppist.com",
            password="qwerty"
            ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #tests if it redirects to login
        self.assertIn('<title>Shoppist - Login</title>', str(response.data))
        #Test with empty fields
        response = self.app.post('/sign-up', data=dict(
            username="",
            email="",
            password=""
            ), follow_redirects=True)
        self.assertIn('Invalid format of email or password', str(response.data))
        

    def  test_post_login(self):
        '''Test if user can login'''
        response = self.app.post('/sign-up', data=dict(
            username="joshua",
            email="user@shoppist.com",
            password="qwerty"
            ), follow_redirects=True)
        response = self.app.post('/login', data=dict(
            email="user@shoppist.com",
            password="qwerty"
            ), follow_redirects=True)
        #test if it returns something
        self.assertEqual(response.status_code, 200)
        #test if it redirects to dashboard - login successful
        self.assertIn('<title>Shoppist - Dashboard</title>', str(response.data))
        #test with wrong password
        response = self.app.post('/login', data=dict(
            email="user@shoppist.com",
            password="12345"
            ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #test login fails
        self.assertIn('Wrong email or password', str(response.data))
        #test with wrong email
        response = self.app.post('/login', data=dict(
            email="riceman@shoppist.com",
            password="qwerty"
            ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #test login fails
        self.assertIn('Wrong email or password', str(response.data))

    def  test_post_logout(self):
        '''Test if user can login'''
        response = self.app.get('/logout', follow_redirects=True)
        response = self.app.get('/dashboard', follow_redirects=True)
        #test if it redirects to login - user not logged in
        self.assertIn('<title>Shoppist - Login</title>', str(response.data))
        
    def  test_sh_list_add(self):
        '''Test if user can add list'''
        response = self.app.post('/sh_list', data=dict(
            email="user@shoppist.com",
            title = "Breakfast",
            items=["Coffee", "Bacon", "Milk", "Bread"]
            ))
        #test if it returns something
        self.assertEqual(response.status_code, 200)

    def  test_sh_list_update(self):
        '''Test if user can update a list'''
        response = self.app.put('/sh_list', data=dict(
            email="user@shoppist.com",
            sh_list_id = 4,
            title = "Breakfast",
            items=["Coffee", "Bacon", "Milk", "Bread"]
            ))
        #test if it returns something
        self.assertEqual(response.status_code, 200)

    def  test_sh_list_delete(self):
        '''Test if user can add list'''
        response = self.app.delete('/sh_list', data=dict(
            sh_list_id = 4
            ))
        #test if it returns something
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
