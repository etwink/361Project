
from django.test import TestCase
from django.test import Client
from syllabus_maker.models import *


class TestEditUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin1 = MyUser.objects.create(name='admin', username='admin', password='admin', access='a',
                                            office='', phoneNum='', email='', officeHours='')
        self.user1 = MyUser.objects.create(name='John Doe', username='jdoe', password='password123', access='b',
                                           office='EMS 500', phoneNum='1234567890', email='jdoe@uwm.edu',
                                           officeHours='MW 2-4')
        self.user2 = MyUser.objects.create(name='Jane Smith', username='jsmith', password='password', access='c',
                                           office='EMS 232', phoneNum='5555555555', email='jsmith@uwm.edu',
                                           officeHours='TR 11AM-1PM')
        self.user3 = MyUser.objects.create(name='Steve Bennet', username='sbennet', password='password', access='d',
                                           office='EMS 232', phoneNum='55555', email='sbennet@uwm.edu',
                                           officeHours='MW 11-12')
        self.course1 = Course.objects.create(name='test_course', number=100, info='test course 1',
                                             instructor=self.user1)
        self.section1 = Section.objects.create(number=801, course=self.course1, teachingAssistant=self.user2)

    def test_admin_home_editUser(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/', {'adminButton': 'Edit User'})
        self.assertEqual(response.status_code, 200)

    def test_admin_home_editUser_back_button(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {'BackButton': 'Back'})
        self.assertEqual(response.status_code, 200)

    def test_admin_home_editUser_logout_button(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {'logoutButton': 'home'})
        self.assertEqual(response.status_code, 200)

    # Should this throw an error due to invalid input?
    def test_admin_home_editUser_no_input(self):
        session = self.client.session
        session['Uname'] = self.user3.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {"User's Name": '',
                                                                          "Username": '', "Password": '', "Office": '',
                                                                          "Phone Number": '', "Email": '',
                                                                          "Office Hours": ''})
        self.assertEqual(response.status_code, 200)

    def test_admin_home_editUser_save_changes1(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {"User's Name": 'John Doe',
                                                                          "Username": 'jdoe', "Password": 'llamas',
                                                                          "Office": 'EMS 500',
                                                                          "Phone Number": '1234567890',
                                                                          "Email": 'jdoe@uwm.edu',
                                                                          "Office Hours": 'MW 2-4'})

        session.save()
        self.assertEqual('llamas', MyUser.objects.get(username='jdoe').password)
        self.assertEqual(response.status_code, 200)

    def test_admin_home_editUser_invalid_access_level(self):
        session = self.client.session
        session['Uname'] = self.user3.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {"User's Name": 'Steve'})
        self.assertEqual(response.status_code, 200)


    '''def test_admin_home_editUser_invalid_access_level(self):
        session = self.client.session
        session['Uname'] = self.user3.username
        session.save()
        response = self.client.post('/home_Admin/edit_information.html', {"User's Name": 'Steve'})
        self.assertEqual(response.status_code, 200)'''
