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
from syllabus_maker import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home.as_view()),
   path('home_Admin/', views.home_Admin.as_view()),
   path('home_Instructor/', views.home_Instructor.as_view()),
   path('home_TA/', views.home_TA.as_view()),
   path('view_syllabus_pick_course.html/', views.view_syllabus_pick_course.as_view()),
   path('view_syllabus_pick_course/view_syllabus.html', views.view_syllabus.as_view()),

   path("home_Admin/admin_CreateNewUser.html", views.admin_CreateNewUser.as_view()),
   path("home_Admin/admin_EditUser1.html", views.admin_EditUser1.as_view()),
   path("home_Admin/admin_EditUser2.html", views.admin_EditUser2.as_view()),
   path("home_Admin/admin_CreateCourse.html", views.admin_CreateCourse.as_view()),
   path("home_Admin/admin_AddCourseSection1.html", views.admin_AddCourseSection1.as_view()),
   path("home_Admin/admin_AddCourseSection2.html", views.admin_AddCourseSection2.as_view()),
   path("home_Admin/admin_EditCourse1.html", views.admin_EditCourse1.as_view()),
   path("home_Admin/admin_EditCourse2.html", views.admin_EditCourse2.as_view()),
   path("home_Admin/edit_information.html", views.edit_information.as_view()),
   path("home_Instructor/edit_information.html", views.edit_information.as_view()),
   path("home_TA/edit_information.html", views.edit_information.as_view()),
   path("home_Instructor/add_syllabus_pick_class.html", views.add_syllabus_pick_class.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create.html", views.add_syllabus_create.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create/add_syllabus_subscreen.html", views.add_syllabus_subscreen.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create/add_syllabus_subscreen/add_calendar_entries.html", views.add_calendar_entries.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create/add_syllabus_subscreen/add_grading_scale.html", views.add_grading_scale.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create/add_syllabus_subscreen/add_weighted_assessment.html", views.add_weighted_assessment.as_view()),
   path("home_Instructor/add_syllabus_pick_class/add_syllabus_create/add_syllabus_subscreen/add_syllabus_final.html",
        views.add_syllabus_final.as_view()),

]
