from django.db import models

# For Users
class MyUser(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # access level
    access = models.CharField(max_length=1)
    office = models.CharField(max_length=20, blank=True, null=True)
    phoneNum = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    officeHours = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    # For holding course info
    info = models.CharField(max_length=300)
    department = models.CharField(max_length=20)
    # Each course has one instructor, but instructors can have multiple courses.
    # Instructor should be assigned to sections not courses
    #   (e.g. 361-401:Lecture:Instructor: Rock       361-803:Lab:Instructor: Apoorv)

    # Sections should be assigned to Courses, (e.g. 337-401, 361-401)

    def __str__(self):
        return self.name


class Section(models.Model):
    number = models.IntegerField()
    # Each section has one course, but courses can have multiple sections.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Each section has one TA, but TA's can have multiple sections.
    teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # Rename teachingAssistant to Instructor as sections are both for labs and lectures
    #   (e.g. 337-401:Lecture 333-801:Lab)

    def __str__(self):
        return self.course.name


class Syllabus(models.Model):
    # Each syllabus has one course, but courses can have multiple syllabi.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    policy = models.CharField(max_length=256)
    year = models.IntegerField()
    semester = models.CharField(max_length=10)
    gradingScale = models.ForeignKey("GradingScale", on_delete=models.CASCADE)
    def __str__(self):
        return self.course.name
#probably redundant, might just want to apply Grade directly to Syllabus
#A set of (integer between 0 and 100, letter grade) pairs


class GradingScale(models.Model):
    # Each grade has one grading scale, but grading scales can have multiple grades.
    #letter grade
    # letter = models.CharField(max_length=1)
    #upper bound of letter grade with 2 decimal places (i.e. 89.99 or 100.00)
    # upperBound = models.DecimalField(unique=True, max_digits=5, decimal_places=2)
    #lower bound of letter grade with 2 decimal places (i.e. 89.99 or 100.00)
    aLowerBound = models.IntegerField()
    bLowerBound = models.IntegerField()
    cLowerBound = models.IntegerField()
    dLowerBound = models.IntegerField()
    fLowerBound = models.IntegerField()
    def __str__(self):
        pass

#A set of (integer between 0 and 100, description) pairs.
class WeightedAssessment(models.Model):
    # Each weighted assessment has one syllabus, but syllabi can have multiple weighted assessments.
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    #The integers are the weights each grading category, and must add up to 100
    weight = models.IntegerField()
    #Description may include html markup which should be rendered as normal.
    description = models.CharField(max_length=20)
    def __str__(self):
        pass

#Each calendar entry is of (date, topic, activity)
class CalendarEntry(models.Model):
    # Each calendar entry has one syllabus, but syllabi can have multiple calendar entries.
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, blank=True, null=True)
    #used for storing calendar objects
    calendarArray = []
    #The dates in a calendar can be updated by changing the start date and keeping all offsets between dates, or by editing dates of individual entries.
    calendarDate = models.DateField()
    calendarTopic = models.CharField(max_length=20)
    calendarActivity = models.CharField(max_length=300)
    def __str__(self):
        pass

