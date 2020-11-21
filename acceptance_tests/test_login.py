from django.test import TestCase
from django.test import Client
from syllabus_maker.models import *

class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_admin = Login.objects.create(name="admin", password="test1")
        self.access_admin = Access.objects.create(accessLevel="a")
        self.admin = credentials.objects.create(name="admin", login =self.login_admin, access = self.access_admin)

        self.login_admin2 = Login.objects.create(name="admin2", password="test1.2")
        self.access_admin2 = Access.objects.create(accessLevel="a")
        self.admin2 = credentials.objects.create(name="admin2", login =self.login_admin2, access = self.access_admin2)

        # below is not needed for sprint 1, but being created to help when we add instructor and TA log in potential, as well as ensuring that log in goes to the right location.
        self.login_instructor = Login.objects.create(name="instructor", password="test2")
        self.access_instructor = Access.objects.create(accessLevel="b")
        self.instructor = credentials.objects.create(name="instructor", login =self.login_instructor, access = self.access_instructor)

        self.login_ta = Login.objects.create(name="ta", password="test3")
        self.access_ta = Access.objects.create(accessLevel="c")
        self.ta = credentials.objects.create(name="ta", login =self.login_ta, access = self.access_ta)

    # test invalid password and name
    def test_invalid_login_wrong_name_and_password(self):
        response = self.client.post('/', {'name': 'conner', "password": "bad"})
        self.assertEquals(response.usrl, '/')

    # test valid password, invalid name
    def test_invalid_login_wrong_name(self):
        response = self.client.post('/', {'name': 'conner', "password": "test1"})
        self.assertEquals(response.usrl, '/')

    # test correct admin name, bad password
    def test_invalid_login_right_name_wrong_password(self):
        response = self.client.post('/', {'name': 'admin', "password": "bad"})
        self.assertEquals(response.usrl, '/')

    # test to see if valid admin log in goes to admin home page
    def test_valid_login_admin(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'test1'})
        self.assertEqual(response.url, '/admin_home/')
        response2 = self.client.get('/admin_home/')
        print(response2.context['admin_home'])
        things = list(response2.context['admin_home'])
        print(things)
        for project in things:
            self.assertEqual(project.name, self.admin.name)

    # test to see if a valid login doesn't take to admin home page, for sprint one will just go to the login page
    # NEEDS UPDATING FOR SPRINT 2
    def test_valid_login_instructor_doesnt_go_admin_page(self):
        response = self.client.post('/', {'name': 'instructor', "password": "test2"})
        self.assertEquals(response.usrl, '/')

    # test to see if a valid login doesn't take to admin home page, for sprint one will just go to the login page
    # NEEDS UPDATING FOR SPRINT 2
    def test_valid_login_ta_doesnt_go_admin_page(self):
        response = self.client.post('/', {'name': 'ta', "password": "test3"})
        self.assertEquals(response.usrl, '/')

    # test that no valid session returns to home menu when trying to access a page deeper in the website
    def no_session(self):
        response = self.client.get('/admin_home/')
        self.assertEquals(response.usrl, '/')

    # test that different logins result in different sessions
    def test_different_sessions_different_logins(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'test1'})
        response2 = self.client.get('/admin_home/')
        print(response2.context['admin_home'])
        things = list(response2.context['admin_home'])
        print(things)
        for project in things:
            self.assertNotEquals(project.name, self.admin2.name)

    def test_logout(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'test1'})
        response2 = self.client.get('/admin_home/')
        things = list(response2.context['admin_home'])
        print(things)
        for project in things:
            self.assertNotEquals(project.name, self.admin2.name)
