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


class Section(models.Model):
    number = models.IntegerField(unique=True)
    # Each section has one course, but courses can have multiple sections.
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Each section has one TA, but TA's can have multiple sections.
    instructor = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name



    # Course:Chem101
    #     -Section:401
    #         -Instructor:Will
    # Course:Bio101
    #     -Section:401
    #         -Instruction:Charlie


class Course(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    # For holding course info
    info = models.CharField(max_length=300)
    # Each course has one instructor, but instructors can have multiple courses.
    # instructor = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


