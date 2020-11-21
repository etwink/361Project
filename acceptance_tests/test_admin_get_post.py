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
        #response1 = self.client.get('/adminHome/')
        response2 = self.client.post('/', {'name': 'admin', 'password': 'admin'})
        self.assertEqual(response2.url, '/adminHome/')

    def test_admin_home(self):
        response1 = self.client.post('/adminHome/', {'goto': 'createUser'})
        self.assertEqual(response1.url, '/createUser/')
        response2 = self.client.post('/adminHome/', {'goto': 'editUser'})
        self.assertEqual(response2.url, '/editUser1/')
        response3 = self.client.post('/adminHome/', {'goto': 'createCourse'})
        self.assertEqual(response3.url, '/createCourse1/')
        response4 = self.client.post('/adminHome/', {'goto': 'editCourse'})
        self.assertEqual(response4.url, '/editCourse1/')
        response5 = self.client.post('/adminHome/', {'goto': 'logOut'})
        self.assertEqual(response5.url, '/')

    def test_create_new_user(self):
        response1 = self.client.post('/createUser/', {'name': '', 'username': '', 'password': '', 'role': '', 'office': '',
                                                    'phoneNum': '', 'email': '', 'officeHours': '', 'course': ''})
        self.assertEqual(response1.context['error'], 'fill in all mandatory information')
        response2 = self.client.post('/createUser/', {'name': 'John Doe', 'username': 'jdoe', 'password': 'password123',
                                                     'role': 'instructor', 'office': 'EMS 100',
                                                     'phoneNum': '(123)456-7890', 'email': 'jdoe@uwm.edu',
                                                     'officeHours': 'MW 3:00-5:00', 'course': self.course1})
        self.assertEqual(response2.url, '/adminHome/')
        response3 = self.client.post('/createUser/', {'goto': 'back'})
        self.assertEqual(response3.url, '/adminHome/')
        response4 = self.client.post('/createUser/', {'goto': 'logOut'})
        self.assertEqual(response4.url, '/')
        response5 = self.client.get('/createUser/')
        courses = list(response5.context['courses'])
        print(courses)
        for course in courses:
            self.assertEqual(course.name, self.course1.name)


    def test_edit_user_page1(self):
        response1 = self.client.get('/editUser1/')
        users = list(response1.context['users'])
        print(users)
        for user in users:
            self.assertEqual(user.username, self.user1__name.name)
            self.assertEqual(user.name, self.user1.name)
        response2 = self.client.post('')

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