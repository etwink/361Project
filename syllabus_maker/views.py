from django.shortcuts import render, redirect
from django.views import View
from .models import MyUser

class home(View):
    def get(self,request):
        request.session.pop("Uname", None)
        return render(request,"home.html",{})

    def post(self,request):
        m = None
        try:
            m = MyUser.objects.get(name=request.POST['Uname'])
        except:
            pass
        if m is not None and m.login.password == request.POST['Pass']:
            request.session["Uname"] = request.POST["Uname"]
            if m.access == 'a':
                return redirect("/home_Admin/")
            if m.access == 'b':
                return redirect("/home_Instructor/")
            if m.access == 'c':
                return redirect("/home_TA/")
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