from django.test import TestCase
from django.test import Client

from syllabus_maker.models import Course


class TestSyllabus(TestCase):
    def setUp(self):
        # create clients with different access levels
        self.noCli = Client()
        self.adminCli = Client()
        self.instructorCli = Client()
        self.taCli = Client()

        # assign access levels
        self.adminCli.session["Uname"] = "admin"
        self.instructorCli.session["Uname"] = "instructor"
        self.taCli.session["Uname"] = "ta"

        self.adminCli.session.save()
        self.instructorCli.session.save()
        self.taCli.session.save()

    """
    tests for access
    """

    def test_noAccess(self):
        # someone who isn't logged in should get redirected
        # all response codes should be 302 (redirect)
        # should then be redirected to the login page
        access_res = self.noCli.get('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.get('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")
        access_res = self.noCli.post('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/")

    def test_noAdminAccess(self):
        # admins should get redirected
        # all response codes should be 302 (redirect)
        # should then be redirected to the admin home page
        access_res = self.adminCli.get('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.get('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")
        access_res = self.adminCli.post('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_Admin.html")

    def test_noTaAccess(self):
        # TAs should get redirected
        # all response codes should be 302 (redirect)
        # should then be redirected to the ta home page
        access_res = self.taCli.get('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.get('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")
        access_res = self.taCli.post('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 302)
        self.assertEqual(access_res.url, "/home_TA.html")

    def test_yesInstructorAccess(self):
        # instructors should not get redirected
        access_res = self.instructorCli.get('/create_syllabus.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/edit_syllabus.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/add_class_syllabus.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/add_grading_scale.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/add_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/add_calendar_entries.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/edit_class_syllabus.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/edit_grading_scale.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/edit_weighted_assessment.html')
        self.assertEqual(access_res.status_code, 200)
        access_res = self.instructorCli.get('/edit_calendar_entries.html')
        self.assertEqual(access_res.status_code, 200)
        # will test the post requests below

    """
    tests for GET requests
    """

    def test_getCreateSyllabusContents(self):
        # want to ensure that all courses are in the course list
        res = self.instructorCli.get('/create_syllabus.html')
        courses = res.context.get("courses", None)
        self.assertNotEqual(courses, None, "courses should be in context")
        if (len(courses) > 0):
            self.assertTrue(isinstance(courses[0], Course))
        else:
            raise Warning("len(courses) is 0. ensure courses are in database")

    def test_getEditSyllabusContents(self):
        # want to ensure that all courses are in the course list
        res = self.instructorCli.get('/create_syllabus.html')
        courses = res.context.get("courses", None)
        self.assertIsNotNone(courses, "courses should be in context")
        for course in courses:
            self.assertIs(type(course), Course, "course should be a list of courses")

    def test_getAddClassSyllabusContents(self):
        # static page
        pass

    def test_getAddGradingScaleContents(self):
        # static page
        pass

    def test_getAddWeightedAssessmentContents(self):
        # static page
        pass

    def test_getAddCalendarEntriesContents(self):
        # static page
        pass

    def test_getEditClassSyllabusContents(self):
        # static page
        pass

    def test_getEditGradingScaleContents(self):
        res = self.instructorCli.get('/edit_grading_scale.html')
        scale = res.context.get("scale", None)
        self.assertIsNotNone(scale, "scale should be in context")
        self.assertIs(scale, list, "scale should be of type list")
        self.assertEqual(len(scale), 24, "scale length should be 24")
        for s in scale:
            self.assertis(type(s), tuple, "scale should be a list of tuples")
            self.assertEqual(len(s), 2, "tuples should be of length 2")
            lo,hi = s
            self.assertIs(type(lo), float, "tuples should be two floats")
            self.assertIs(type(hi), float, "tuples should be two floats")

    def test_getEditWeightedAssessmentContents(self):
        res = self.instructorCli.get('/edit_weighted_assessment.html')
        weighted_assessments = res.context.get("weighted_assessments", None)
        self.assertIsNotNone(weighted_assessments, "weighted_assessments should be in context")
        self.assertIs(type(weighted_assessments), list, "weighted_assessments should be of type list")

    def test_getEditCalendarEntriesContents(self):
        res = self.instructorCli.get('/edit_calendar_entries.html')
        entries = res.context.get("entries", None)
        self.assertIsNotNone(entries, "entries should be in context")
        self.assertIs(type(entries), list, "entries should be of type list")

    """
    tests for POST requests
    """

    def test_postCreateSyllabusContents(self):
        pass

    def test_postEditSyllabusContents(self):
        pass

    def test_postAddClassSyllabusContents(self):
        pass

    def test_postAddGradingScaleContents(self):
        pass

    def test_postAddWeightedAssessmentContents(self):
        pass

    def test_postAddCalendarEntriesContents(self):
        pass

    def test_postEditClassSyllabusContents(self):
        pass

    def test_postEditGradingScaleContents(self):
        pass

    def test_postEditWeightedAssessmentContents(self):
        pass

    def test_postEditCalendarEntriesContents(self):
        pass
