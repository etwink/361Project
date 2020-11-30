from django.test import TestCase
from django.test import Client
from syllabus_maker.models import *

class TestTracker(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin1 = MyUser.objects.create(name = 'admin', username = 'admin', password = 'admin', access = 'a',
                                            office = '', phoneNum = '', email = '', officeHours = '')
        self.user1 = MyUser.objects.create(name = 'John Doe', username = 'jdoe', password = 'password123', access = 'b',
                                            office = 'EMS 500', phoneNum = '1234567890', email = 'jdoe@uwm.edu', officeHours = 'MW 2-4')
        self.user2 = MyUser.objects.create(name = 'Jane Smith', username = 'jsmith', password = 'password', access = 'c',
                                            office = 'EMS 232', phoneNum = '5555555555', email = 'jsmith@uwm.edu', officeHours = 'TR 11AM-1PM')
        self.course1 = Course.objects.create(name = 'test_course', number = 100, info = 'test course 1', instructor = self.user1)
        self.section1 = Section.objects.create(number = 801, course = self.course1, teachingAssistant = self.user2)

    # def test_invalid_login(self):
    #     response = self.client.post('/', {'Uname': 'admin', 'Pass': 'admin123'})
    #     self.assertEqual(response.url, '/')
    #
    # def test_valid_login(self):
    #     response = self.client.post('/', {'Uname': 'admin', 'Pass': 'admin'})
    #     self.assertEqual(response.url, '/home_Admin/')

    def test_admin_home_createUser(self):
        response = self.client.post('/home_Admin/', {'adminButton': 'Create User'})
        self.assertEqual(response.url, '/home_Admin/admin_CreateNewUser.html')

    def test_admin_home_editUser(self):
        response = self.client.post('/home_Admin/', {'adminButton': 'Edit User'})
        self.assertEqual(response.url, '/home_Admin/admin_EditUser1.html')

    def test_admin_home_createCourse(self):
        response = self.client.post('/home_Admin/', {'adminButton': 'Create Course'})
        self.assertEqual(response.url, '/home_Admin/admin_CreateCourse.html')

    def test_admin_home_editCourse(self):
        response = self.client.post('/home_Admin/', {'adminButton': 'Edit Course'})
        self.assertEqual(response.url, '/home_Admin/admin_EditCourse1.html')

    def test_admin_home_logout(self):
        response = self.client.post('/home_Admin/', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')

    # def test_create_new_user_get(self):
    #     response = self.client.get('/admin_CreateNewUser/')
    #     courses = list(response.context['courses'])
    #     print(courses)
    #     for course in courses:
    #         self.assertEqual(course.number, self.course1.number)
    #         self.assertEqual(course.name, self.course1.name)

    def test_create_new_user_bad_post(self):
        response = self.client.post('/home_Admin/admin_CreateNewUser.html', {'name': '', 'username': '', 'password': '', 'role': '', 'office': '',
                                                    'phoneNum': '', 'email': '', 'officeHours': '', 'course': ''})
        self.assertEqual(response.url, '/home_Admin/admin_CreateNewUser.html')

    def test_create_new_user_good_post(self):
        response = self.client.post('/home_Admin/admin_CreateNewUser.html', {'name': 'Carl Weezer', 'username': 'cweezer', 'password': 'llamas',
                                                     'role': 'b', 'office': 'EMS 100',
                                                     'phoneNum': '1111111111', 'email': 'cweezer@uwm.edu',
                                                     'officeHours': 'MW 3:00-5:00', 'course': self.course1})
        self.assertEqual(response.url, '/home_Admin/')

    def test_create_new_user_back(self):
        response = self.client.post('/home_Admin/admin_CreateNewUser.html', {'backButton': 'Back'})
        self.assertEqual(response.url, '/home_Admin/')

    def test_create_new_user_logout(self):
        response = self.client.post('/home_Admin/admin_CreateNewUser.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')


    # def test_edit_user_page1_get(self):
    #     response = self.client.get('/home_Admin/admin_EditUser1.html')
    #     users = list(response.context['users'])
    #     print(users)
    #     for user in users:
    #         self.assertEqual(user.username, self.user1.username)
    #         self.assertEqual(user.name, self.user1.name)

    def test_edit_user_page1_post(self):
        response = self.client.post('/home_Admin/admin_EditUser1.html', {'username': 'admin123'})
        self.assertEqual(response.url, '/home_Admin/admin_EditUser2.html')

    def test_edit_user_page1_back(self):
        response = self.client.post('/home_Admin/admin_EditUser1.html', {'backButton': 'Back'})
        self.assertEqual(response.url, '/home_Admin/')

    def test_edit_user_page1_logout(self):
        response = self.client.post('/home_Admin/admin_EditUser1.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')

    # def test_edit_user_page2_get(self):
    #     response = self.client.get('/home_Admin/admin_EditUser2.html')
    #     user = MyUser(response.context['user']) #passes a user object to edit user page 2
    #     self.assertEqual(user.name, self.user1.name) #checking to see if the user object passed in is the user in the database
    #     self.assertEqual(user.username, self.user1.username)
    #     self.assertEqual(user.access, self.user1.access)

    def test_edit_user_page2_post(self):
        response = self.client.post('/home_Admin/admin_EditUser2.html', {'name': 'John Doe', 'username': 'jdoe', 'password': 'password123',
                                                     'role': 'instructor', 'office': 'EMS 100',
                                                     'phoneNum': '(123)456-7890', 'email': 'jdoe@uwm.edu',
                                                     'officeHours': 'MW 3:00-5:00', 'course': self.course1})
        self.assertEqual(response.url, '/home_Admin/')

    def test_edit_user_page2_back(self):
        response = self.client.post('/home_Admin/admin_EditUser2.html', {'backButton': 'Back'})
        self.assertEqual(response.url, '/home_Admin/admin_EditUser1.html')

    def test_edit_user_page2_logout(self):
        response = self.client.post('/home_Admin/admin_EditUser2.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')


    def test_create_course_bad_post(self):
        response = self.client.post('/home_Admin/admin_CreateCourse.html', {'name': '', 'number': '', 'department': '', 'info': ''})
        self.assertEqual(response.url, '/home_Admin/admin_CreateCourse.html')

    def test_create_course_good_post(self):
        response = self.client.post('/home_Admin/admin_CreateCourse.html', {'name': 'History of Llamas', 'number': '720',
                                                        'department': 'History', 'info': 'Brief history of llamas'})
        self.assertEqual(response.url, '/home_Admin/admin_AddCourseSection.html')

    def test_create_course_back(self):
        response = self.client.post('/home_Admin/admin_CreateCourse.html', {'backButton': 'Back'})
        self.assertEqual(response.url, '/home_Admin/')

    def test_create_course_logout(self):
        response = self.client.post('/home_Admin/admin_CreateCourse.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')

    def test_create_add_course_sections_bad_post(self):
        response = self.client.post('/home_Admin/admin_AddCourseSection.html', {'number': ''})
        self.assertEqual(response.url, '/home_Admin/admin_AddCourseSection.html')

    def test_create_add_course_sections_good_post(self):
        response = self.client.post('/home_Admin/admin_AddCourseSection.html', {'number': 804})
        self.assertEqual(response.url, '/home_Admin/admin_AddCourseSection.html')

    def test_create_add_course_sections_back(self):
        response = self.client.post('/home_Admin/admin_AddCourseSection.html', {'backButton': 'Back'})
        self.assertEqual(response.url, '/home_Admin/admin_CreateCourse.html')

    def test_create_add_course_sections_logout(self):
        response = self.client.post('/home_Admin/admin_AddCourseSection.html', {'logoutButton': 'Logout'})
        self.assertEqual(response.url, '/')

    def test_edit_course_page1(self):
        pass
        #resposne = self.clent.get()

    def test_edit_course_page2(self):
        pass
        #response = self.client.get()

    def test_edit_add_course_sections_page(self):
        pass
        #response = self.client.get()