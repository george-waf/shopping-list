import unittest
import app
from flask import url_for
import sys


class TddInShoppist(unittest.TestCase):

    def setUp(self):
        '''Setup the app for testing'''
        app.APP.testing = True
        self.app = app.APP.test_client()

    def test_app(self):
        '''Test the app in this order'''
        self.get_root_route()
        self.get_sign_up()
        self.get_login()
        self.get_logout()
        self.post_sign_up()
        self.post_login()
        self.item_add()
        #self.shopping_list_add()
        # self.shopping_list_get()
        # self.shopping_list_get_all()
        # self.shopping_list_update()
        # self.shopping_list_delete()
        self.post_logout()

    def get_root_route(self):
        '''Test access to the GET '/' route'''
        response = self.app.get('/')
        # test if it returns something
        self.assertEqual(response.status_code, 200)

    def get_sign_up(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/sign-up')
        # test if it returns something
        self.assertEqual(response.status_code, 200)
        # test if it signs-up

    def get_login(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/login')
        # test if it returns something
        self.assertEqual(response.status_code, 200)

    def get_logout(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/logout', follow_redirects=True)
        # test if it returns something
        self.assertEqual(response.status_code, 200)

    def post_sign_up(self):
        '''Test if user can sign up'''
        response = self.app.post('/sign-up', data=dict(
            username="joshua",
            email="joshua@shoppist.com",
            password="qwerty",
            confirm_password="qwerty"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # tests if it redirects to login- then user is signed up
        self.assertIn('<title>Shoppist - Login</title>', str(response.data))
        # Test with empty fields
        response = self.app.post('/sign-up', data=dict(
            username="",
            email="",
            password="",
            confirm_password=""
        ), follow_redirects=True)
        self.assertIn('Invalid format of username, email or password',
                      str(response.data))
        # test that confirm password is working
        response = self.app.post('/sign-up', data=dict(
            username="joshua",
            email="joshua@shoppist.com",
            password="qwerty",
            confirm_password="12345"
        ), follow_redirects=True)
        self.assertIn('Passwords do not match', str(response.data))
        # test that email has to be unique
        response = self.app.post('/sign-up', data=dict(
            username="morande",
            email="joshua@shoppist.com",
            password="qwerty",
            confirm_password="qwerty"
        ), follow_redirects=True)
        self.assertIn('Another user is already using that email',
                      str(response.data))
        # test that username has to be unique
        response = self.app.post('/sign-up', data=dict(
            username="joshua",
            email="jack@shoppist.com",
            password="qwerty",
            confirm_password="qwerty"
        ), follow_redirects=True)
        self.assertIn('That username is already taken', str(response.data))

    def post_login(self):
        '''Test if user can login'''
        response = self.app.post('/login', data=dict(
            email="joshua@shoppist.com",
            password="qwerty"
        ), follow_redirects=True)
        # test if it returns something
        self.assertEqual(response.status_code, 200)
        # test if it redirects to dashboard - login successful
        self.assertIn('<title>Shoppist - Dashboard</title>',
                      str(response.data))
        # test with wrong password
        response = self.app.post('/login', data=dict(
            email="joshua@shoppist.com",
            password="12345"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # test login fails
        self.assertIn('Wrong email or password', str(response.data))
        # test with wrong email
        response = self.app.post('/login', data=dict(
            email="superman@shoppist.com",
            password="qwerty"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # test login fails
        self.assertIn('Wrong email or password', str(response.data))

    def post_logout(self):
        '''Test if user can login'''
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn('<title>Shoppist - Login</title>', str(response.data))
        response = self.app.get('/dashboard', follow_redirects=True)
        # test if it redirects to login - if user not logged in
        #self.assertIn('<title>Shoppist - Login</title>', str(response.data))

    def item_add(self):
        '''Test if user can add list'''
        response = self.app.post('/item', data=dict(
            name="Coffee",
            done=False))
        # test if it returns 201
        self.assertEqual(response.status_code, 201)
        self.assertEqual(int(response.data), 1)

    # def shopping_list_add(self):
    #     '''Test if user can add list'''
    #     response = self.app.post('/shopping_list', data=dict(
    #         title="Tomorrows breakfast",
    #         items = []
    #     ))
    #     # test if it returns 201
    #     self.assertEqual(response.status_code, 201)

    # def shopping_list_get_all(self):
    #     response = self.app.get('/shopping_list')
    #      # test if it returns 200 OK
    #     self.assertEqual(response.status_code, 200)

    # def shopping_list_get(self):
    #     response = self.app.get('/shopping_list/<id:int>')
    #      # test if it returns 200 OK
    #     self.assertEqual(response.status_code, 200)

    # def shopping_list_update(self):
    #    '''Test if user can add list'''
    #     response = self.app.post('/shopping_list', data=dict(
    #         items=["Coffee", "Bacon", "Milk", "Bread"]
    #     ))
    #     # test if it returns 201
    #     self.assertEqual(response.status_code, 201)

    # def shopping_list_delete(self):
    #     '''Test if user can add list'''
    #     response = self.app.delete('/shopping_list', data=dict(
    #         shopping_list_id=4
    #     ))
    #     # test if it returns something
    #     self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
