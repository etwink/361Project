from django.test import TestCase
from django.test import Client
from django.urls import resolve
from syllabus_maker.models import *

class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = MyUser.objects.create(name="admin", username="admin", password="test1",  access="a", office="N/A", phoneNum="N/A", email="N/A", officeHours="N/A")

        self.admin2 = MyUser.objects.create(name="admin2", username="admin2", password="test1.2", access="a", office="N/A", phoneNum="N/A", email="N/A", officeHours="N/A")

        # below is not needed for sprint 1, but being created to help when we add instructor and TA log in potential, as well as ensuring that log in goes to the right location.
        self.instructor = MyUser.objects.create(name="instructor", username="instructor", password="test2", access="b", office="N/A", phoneNum="N/A", email="N/A", officeHours="N/A")

        self.ta = MyUser.objects.create(name="ta", username="ta", password="test3", access="c", office="N/A", phoneNum="N/A", email="N/A", officeHours="N/A")

    # test invalid password and name
    def test_invalid_login_wrong_name_and_password(self):
        response = self.client.post('/', {'Uname': 'conner', "Pass": "bad"})
        self.assertEqual(response.context['error'], 'Invalid name/password')

    # test valid password, invalid name
    def test_invalid_login_wrong_name(self):
        response = self.client.post('/', {'Uname': 'conner', "Pass": "test1"})
        self.assertEqual(response.context['error'], 'Invalid name/password')

    # test correct admin name, bad password
    def test_invalid_login_right_name_wrong_password(self):
        response = self.client.post('/', {'Uname': 'admin', "Pass": "bad"})
        self.assertEqual(response.context['error'], 'Invalid name/password')

    # test to see if valid admin log in goes to admin home page
    def test_valid_login_admin(self):
        response = self.client.post('/', {'Uname': 'admin', 'Pass': 'test1'})
        self.assertEqual(response.url, '/home_Admin/')
        response2 = self.client.get('/home_Admin/')
        print(response2.context['home_Admin'])
        things = list(response2.context['home_Admin'])
        for project in things:
            self.assertEqual(project.name, self.admin.name)

    # test to see if a valid login doesn't take to admin home page, for sprint one will just go to the login page
    # NEEDS UPDATING FOR SPRINT 2
    def test_valid_login_instructor_doesnt_go_admin_page(self):
        response = self.client.post('/', {'Uname': 'instructor', "Pass": "test2"})
        self.assertEquals(response.url, '/home_Instructor/')

    # test to see if a valid login doesn't take to admin home page, for sprint one will just go to the login page
    # NEEDS UPDATING FOR SPRINT 2
    def test_valid_login_ta_doesnt_go_admin_page(self):
        response = self.client.post('/', {'Uname': 'ta', "Pass": "test3"})
        self.assertEquals(response.url, '/home_TA/')

    # test that no valid session returns to home menu when trying to access a page deeper in the website
    def no_session(self):
        response = self.client.get('/home_Admin/')
        self.assertEquals(response.url, '/')

    # test that different logins result in different sessions
    def test_different_sessions_different_logins(self):
        response = self.client.post('/', {'Uname': 'admin', 'Pass': 'test1'})
        response2 = self.client.get('/home_Admin/')
        print(response2.context['home_Admin'])
        things = list(response2.context['home_Admin'])
        for project in things:
            self.assertNotEquals(project.name, self.admin2.name)

    def test_logout(self):
        response = self.client.post('/', {'Uname': 'admin', 'Pass': 'test1'})
        response2 = self.client.get('/home_Admin/')
        things = list(response2.context['home_Admin'])
        for project in things:
            self.assertNotEquals(project.name, self.admin2.name)
