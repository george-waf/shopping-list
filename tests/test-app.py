import unittest
import app
 
class TddInShoppist(unittest.TestCase):
    def setUp(self):
        '''Setup the app for testing'''
        app.app.testing = True
        self.app = app.app.test_client()

    def test_get_root_route(self):
        '''Test access to the GET '/' route'''
        response = self.app.get('/')
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def test_get_sign_up(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/sign-up')
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def test_get_login(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/login')
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def test_get_logout(self):
        '''Test access to the GET 'sign-up/' route'''
        response = self.app.get('/logout', follow_redirects=True)
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def  test_post_sign_up(self):
        '''Test if user can sign up'''
        response = self.app.post('/sign-up', data=dict(
            email="user2@shoppist.com",
            password="123456"
            ), follow_redirects=True)
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def  test_post_login(self):
        '''Test if user can login'''
        response = self.app.post('/login', data=dict(
            email="user@shoppist.com",
            password="qwerty"
            ), follow_redirects=True)
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def  test_sh_list_add(self):
        '''Test if user can add list'''
        response = self.app.post('/sh_list', data=dict(
            email="user@shoppist.com",
            title = "Breakfast",
            items=["Coffee", "Bacon", "Milk", "Bread"]
            ))
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def  test_sh_list_update(self):
        '''Test if user can update a list'''
        response = self.app.put('/sh_list', data=dict(
            email="user@shoppist.com",
            sh_list_id = 4,
            title = "Breakfast",
            items=["Coffee", "Bacon", "Milk", "Bread"]
            ))
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

    def  test_sh_list_delete(self):
        '''Test if user can add list'''
        response = self.app.delete('/sh_list', data=dict(
            sh_list_id = 4
            ))
        #test if it returns something
        self.assertEqual(str(response), "<Response streamed [200 OK]>")

if __name__ == '__main__':
    unittest.main()
