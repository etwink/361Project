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
        response2 = self.client.get('/adminHome/')
        sections = list(response2.context['sections'])
        print(sections)
        for section in sections:
            self.assertEqual(section.name, self.section1.name)
            self.assertEqual(section.course, self.section1.course)
            self.assertEqual(section.teachingAssistant, self.section1.teachingAssistant)