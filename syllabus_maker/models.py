from django.db import models


# Create your models here.

# Login Username and Password
class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


# For Users
class User(models.Model): 
    name = models.CharField(max_length=20)
    login = models.ForeignKeyLogin(Login, on_delete=models.CASCADE)
    access = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    # Each course has one instructor, but instructors can have multiple courses.
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=20)
    # Each section has one course, but courses can have multiple sections.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Each section has one TA, but TA's can have multiple sections.
    teachingAssistant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
