from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyUser, Course, Section, Syllabus, WeightedAssessment, GradingScale, CalendarEntry

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Syllabus)
admin.site.register(WeightedAssessment)
admin.site.register(GradingScale)
admin.site.register(CalendarEntry)
