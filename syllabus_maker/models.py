from django.db import models

# For Users
class MyUser(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # access level
    access = models.CharField(max_length=1)
    office = models.CharField(max_length=20)
    phoneNum = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    officeHours = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    # For holding course info
    info = models.CharField(max_length=300)
    # Each course has one instructor, but instructors can have multiple courses.
    instructor = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    # Instructor should be assigned to sections not courses
    #   (e.g. 361-401:Lecture:Instructor: Rock       361-803:Lab:Instructor: Apoorv)
    # Sections should be assigned to Courses, (e.g. 337-401, 361-401)

    def __str__(self):
        return self.name


class Section(models.Model):
    number = models.IntegerField(unique=True)
    # Each section has one course, but courses can have multiple sections.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Each section has one TA, but TA's can have multiple sections.
    teachingAssistant = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # Rename teachingAssistant to Instructor as sections are both for labs and lectures
    #   (e.g. 337-401:Lecture 333-801:Lab)

    def __str__(self):
        return self.course.name
