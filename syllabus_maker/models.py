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

    def __str__(self):
        return self.name


class Section(models.Model):
    number = models.IntegerField(unique=True)
    # Each section has one course, but courses can have multiple sections.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Each section has one TA, but TA's can have multiple sections.
    teachingAssistant = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    syllabus = models.ForeignKey("Syllabus", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Syllabus(models.Model):
    #Each syllabus should only have one course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()

class GradingScale(models.Model):
    Syllabus = models.OneToOneField(Syllabus, on_delete=models.CASCADE)

class Grade(models.Model):
    gradingScale = models.ForeignKey(GradingScale, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1)
    #upper bound of letter grade with 2 decimal places (i.e. 89.99 or 100.00)
    upperBound = models.DecimalField(unique=True, max_digits=5, decimal_places=2)
    #lower bound of letter grade with 2 decimal places (i.e. 89.99 or 100.00)
    lowerBound = models.IntegerField(unique=True, max_digits=5, decimal_places=2)

class CalendarEntry(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, blank=True, null=True)
    calendarDate = models.DateField()
    calendarTopic = models.CharField(max_length=20)
    calendarActivity = models.CharField(max_length=300)


