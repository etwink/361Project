from django.test import TestCase
from django.test import Client
from syllabus_maker.models import MyUser, Course, Section

class TestTracker(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin1 = MyUser.objects.create(name = 'admin', username = 'admin', password = 'admin', access = 'a',
                                            office = '', phoneNum = '', email = '', officeHours = '')
        self.user1 = MyUser.objects.create(name = 'John Doe', username = 'jdoe', password = 'password123', access = 'b',
                                            office = 'EMS 500', phoneNum = '1234567890', email = 'jdoe@uwm.edu', officeHours = 'MW 2-4')
        self.user2 = MyUser.objects.create(name = 'Jane Smith', username = 'jsmith', password = 'password', access = 'c',
                                            office = 'EMS 232', phoneNum = '5555555555', email = 'jsmith@uwm.edu', officeHours = 'TR 11AM-1PM')
        self.course1 = Course.objects.create(name = 'test_course', number = 100, info = 'test course 1', user = self.user1)
        self.section1 = Section.objects.create(number = 801, course = self.course1, teachingAssistant = self.user2)

    def test_invalid_login(self):
        response = self.client.post('/', {'name': 'admin', 'password': 'admin123'})
        self.assertEqual(response.url, '/')

    def test_valid_login(self):
        #response1 = self.client.get('/adminHome/')
        response2 = self.client.post('/', {'name': 'admin', 'password': 'admin'})
        self.assertEqual(response2.url, '/home_Admin/')

    def test_admin_home(self):
        response1 = self.client.post('/home_Admin/', {'adminButton': 'Create User'})
        self.assertEqual(response1.url, '/home_Admin/admin_CreateNewUser.html')

        response2 = self.client.post('/home_Admin/', {'adminButton': 'Edit User'})
        self.assertEqual(response2.url, '/home_Admin/admin_EditUser1.html')

        response3 = self.client.post('/home_Admin/', {'adminButton': 'Create Course'})
        self.assertEqual(response3.url, '/home_Admin/admin_CreateCourse.html')

        response4 = self.client.post('/home_Admin/', {'adminButton': 'Edit Course'})
        self.assertEqual(response4.url, '/home_Admin/admin_EditCourse1.html')

        response5 = self.client.post('/home_Admin/', {'logoutButton': 'Logout'})
        self.assertEqual(response5.url, '/')

    def test_create_new_user(self):
        response5 = self.client.get('/admin_CreateNewUser/')
        courses = list(response5.context['courses'])
        print(courses)
        for course in courses:
            self.assertEqual(course.number, self.course1.number)
            self.assertEqual(course.name, self.course1.name)
        response1 = self.client.post('/home_Admin/admin_CreateNewUser.html', {'name': '', 'username': '', 'password': '', 'role': '', 'office': '',
                                                    'phoneNum': '', 'email': '', 'officeHours': '', 'course': ''})
        self.assertEqual(response1.url, '/home_Admin/admin_CreateNewUser.html')

        response2 = self.client.post('/home_Admin/admin_CreateNewUser.html', {'name': 'Carl Weezer', 'username': 'cweezer', 'password': 'llamas',
                                                     'role': 'b', 'office': 'EMS 100',
                                                     'phoneNum': '1111111111', 'email': 'cweezer@uwm.edu',
                                                     'officeHours': 'MW 3:00-5:00', 'course': self.course1})
        self.assertEqual(response2.url, '/home_Admin/')

        response3 = self.client.post('/home_Admin/admin_CreateNewUser.html', {'backButton': 'Back'})
        self.assertEqual(response3.url, '/home_Admin/')

        response4 = self.client.post('/home_Admin/admin_CreateNewUser.html', {'logoutButton': 'Logout'})
        self.assertEqual(response4.url, '/')


    def test_edit_user_page1(self):
        response1 = self.client.get('/home_Admin/admin_EditUser1.html')
        users = list(response1.context['users'])
        print(users)
        for user in users:
            self.assertEqual(user.username, self.user1.username)
            self.assertEqual(user.name, self.user1.name)
        response2 = self.client.post('/home_Admin/admin_EditUser1.html', {'username': 'admin123'})
        self.assertEqual(response2.url, '/home_Admin/admin_EditUser2.html')
        response3 = self.client.post('/home_Admin/admin_EditUser1.html', {'backButton': 'Back'})
        self.assertEqual(response3.url, '/home_Admin/')

        response4 = self.client.post('/home_Admin/admin_EditUser1.html', {'logoutButton': 'Logout'})
        self.assertEqual(response4.url, '/')

    def test_edit_user_page2(self):
        response1 = self.client.get('/admin_EditUser2/')
        user = MyUser(response1.context['user']) #passes a user object to edit user page 2
        self.assertEqual(user.name, self.user1.name) #checking to see if the user object passed in is the user in the database
        self.assertEqual(user.username, self.user1.username)
        self.assertEqual(user.access, self.user1.access)

        response2 = self.client.post('/admin_EditUser2/', {'name': 'John Doe', 'username': 'jdoe', 'password': 'password123',
                                                     'role': 'instructor', 'office': 'EMS 100',
                                                     'phoneNum': '(123)456-7890', 'email': 'jdoe@uwm.edu',
                                                     'officeHours': 'MW 3:00-5:00', 'course': self.course1})
        self.assertEqual(response2.url, '/home_Admin/')
        response3 = self.client.post('/admin_EditUser2/', {'goto': 'back'})
        self.assertEqual(response3.url, '/admin_EditUser1/')

        response4 = self.client.post('/admin_EditUser2/', {'goto': 'logOut'})
        self.assertEqual(response4.url, '/')


    def test_create_course_page(self):
        response1 = self.client.post('/admin_CreateCourse/', {'name': '', 'number': '', 'department': '', 'info': ''})
        self.assertEqual(response1.url, '/admin_CreateCourse/')

        response2 = self.client.post('/admin_CreateCourse/', {'name': 'History of Llamas', 'number': '720',
                                                        'department': 'History', 'info': 'Brief history of llamas'})
        self.assertEqual(response2.url, '/admin_AddSection/') #This url will probably be changed

        response3 = self.client.post('/admin_CreateCourse/', {'goto': 'back'})
        self.assertEqual(response3.url, '/home_Admin/')

        response4 = self.client.post('/admin_CreateCourse/', {'goto': 'logOut'})
        self.assertEqual(response4.url, '/')

    def test_create_add_course_sections_page(self):
        response1 = self.client.post('/addSection/', {'number': ''})
        self.assertEqual(response1.url, '/addSection/')

        response2 = self.client.post('/addSection/', {'number': 804})
        self.assertEqual(response2.url, '/addSection/')

        response3 = self.client.post('/addSection/', {'goto': 'back'})
        self.assertEqual(response3.url, '/admin_CreateCourse/')

        response4 = self.client.post('/addSection/', {'goto': 'logOut'})
        self.assertEqual(response4.url, '/')

    def test_edit_course_page1(self):
        resposne = self.clent.get()

    def test_edit_course_page2(self):
        response = self.client.get()

    def test_edit_add_course_sections_page(self):
        response = self.client.get()