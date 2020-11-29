"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from syllabus_maker.views import home, home_Admin, home_Instructor, home_TA, admin_CreateNewUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view()),
    path('home_Admin/', home_Admin.as_view()),
    path('home_Instructor/', home_Instructor.as_view()),
    path('home_TA/', home_TA.as_view()),
    path('admin_CreateNewUser/', admin_CreateNewUser.as_view()),
]
