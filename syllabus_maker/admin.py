from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyUser, Course, Section

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Course)
admin.site.register(Section)