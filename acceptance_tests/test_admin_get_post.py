from django.test import TestCase
from django.test import Client
#from syllabus_maker.models import Login, User, Course, Section

class TestTracker(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin1 = Login.objects.create(name = 'admin', password = 'admin')
        self.user1 = User.objects.create(name = 'admin', access = 3, login = self.admin1)
        self.course1 = Course.objects.create(name = 'test_course', user = self.user1)
        self.section1 = Section.objects.create(name = 'test_section', course = self.course1, teachingAssistant = None)

    def test_invalid_login(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'admin123'})
        self.assertEqual(response.context['error'], 'username/passoword incorrect')

    def test_valid_login(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'admin'})
        self.assertEqual(response.url, '/adminHome/')

    def test_admin_home(self):
        response = self.client.post('/adminHome/', {'goto': 'createUser'})
        self.assertEqual(response.url, '/createUser/')
        response = self.client.post('/adminHome/', {'goto': 'editUser'})
        self.assertEqual(response.url, '/editUser/')
        response = self.client.post('/adminHome/', {'goto': 'createCourse'})
        self.assertEqual(response.url, '/createCourse/')
        response = self.client.post('/adminHome/', {'goto': 'editCourse'})
        self.assertEqual(response.url, '/editCourse/')
        response = self.client.post('/adminHome/', {'goto': 'logOut'})
        self.assertEqual(response.url, '/')

    def test_create_new_user(self):
        response = self.client.get()

    def test_edit_user_page1(self):
        response = self.client.get()

    def test_edit_user_page2(self):
        response = self.client.get()

    def test_create_course_page(self):
        response = self.client.get()

    def test_create_add_course_sections_page(self):
        response = self.client.get()

    def test_edit_course_page1(self):
        resposne = self.clent.get()

    def test_edit_course_page2(self):
        response = self.client.get()

    def test_edit_add_course_sections_page(self):
        response = self.client.get()