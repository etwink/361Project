from django.test import TestCase
from django.test import Client
from syllabus_maker.models import *

class TestAddCourseSection(TestCase):
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
        self.course1 = Course.objects.create(name='test_course', number=100, info='test course 1')
        self.section1 = Section.objects.create(number=804, course=self.course1, teacher=self.user2)

    def test_create_add_course_sections1_bad_post(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/admin_AddCourseSection1.html', {'course_id': ''})
        self.assertEqual(response.status_code, 200)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections1_good_post(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/admin_AddCourseSection1.html', {'course_id': 100})
        self.assertEqual(response.status_code, 302)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections1_back(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/admin_AddCourseSection1.html', {'course_id': '', 'backButton': 'Back'})
        self.assertEqual(response.status_code, 200)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections1_logout(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/admin_AddCourseSection1.html', {'course_id': '', 'logoutButton': 'Logout'})
        self.assertEqual(response.status_code, 200)


    def test_create_add_course_sections2_bad_post(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/home_Admin/admin_AddCourseSection2.html', {'course_id': ''})
        self.assertEqual(response.status_code, 200)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections2_good_post(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/admin_AddCourseSection2.html', {'number': 804})
        self.assertEqual(response.status_code, 200)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections2_back(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/admin_AddCourseSection2.html/', {'backButton': 'Back'})
        self.assertEqual(response.status_code, 200)

    # unimplemented -- for sprint 2
    def test_create_add_course_sections2_logout(self):
        session = self.client.session
        session['Uname'] = self.admin1.username
        session.save()
        response = self.client.post('/admin_AddCourseSection2.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.status_code, 200)