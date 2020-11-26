from django.shortcuts import render, redirect
from django.views import View
from .models import MyUser

class home(View):
    def get(self,request):
        request.session.pop("Uname", None)
        return render(request,"home.html",{})

    def post(self,request):
        print(request.POST['Uname'] + request.POST['Pass'])
        m = None
        try:
            m = MyUser.objects.get(username=request.POST['Uname'])
        except:
            pass
        if m is not None and m.password == request.POST['Pass']:
            request.session["Uname"] = request.POST["Uname"]
            if m.access == 'a':
                return redirect("/home_Admin/")
            if m.access == 'b':
                return redirect('/InstructorPage')
            if m.access == 'c':
                return redirect("/TAPage/")
        return render(request,"home.html",{'error': 'Invalid name/password'})


class home_Admin(View):
    def get(self,request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "home_Admin.html", {"home_Admin": home_Admin})

    def post(self,request):
        position = request.POST.get('position')
        name = request.POST.get('name')
        if name != '':
            if position == 'Instructor':
                newInstructor = MyUser(name=name, login=None, password="password")
                newInstructor.save()
            elif position == 'TA':
                newTA = MyUser(name=name, login=None, password="password")
                newTA.save()

        return render(request, "home_Admin.html", {"home_Admin": home_Admin})


class home_Instructor(View):
    def get(self,request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "home_Instructor.html", {"home_Instructor": home_Instructor})

    def post(self,request):

        return render(request, "home_Instructor.html", {"home_Instructor": home_Instructor})


class home_TA(View):
    def get(self,request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "home_TA.html", {"home_TA": home_TA})

    def post(self,request):

        return render(request, "home_TA.html", {"home_TA": home_TA})

class admin_CreateNewUser(View):
    def get(self, request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "admin_CreateNewUser.html", {"admin_CreateNewUser": admin_CreateNewUser})

    def post(self,request):
        return render(request, "home_Admin", {"home_Admin": home_Admin})


class admin_EditUser1(View):
    def get(self, request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "admin_EditUser1.html", {"admin_EditUser1": admin_EditUser1})

    def post(self,request):
        return render(request, "home_Admin", {"home_Admin": home_Admin})

class admin_EditUser2(View):
    def get(self, request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "admin_EditUser2.html", {"admin_EditUser2": admin_EditUser2})

    def post(self,request):
        return render(request, "home_Admin", {"home_Admin": home_Admin})


class admin_CreateCourse(View):
    def get(self, request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "admin_CreateCourse.html", {"admin_CreateCourse": admin_CreateCourse})

    def post(self,request):
        return render(request, "home_Admin", {"home_Admin": home_Admin})

class admin_EditCourse1(View):
    def get(self, request):
        if not request.session.get("Uname"):
            return redirect('/')
        return render(request, "admin_EditCourse1.html", {"admin_EditCourse1": admin_EditCourse1})

    def post(self,request):
        return render(request, "home_Admin", {"home_Admin": home_Admin})