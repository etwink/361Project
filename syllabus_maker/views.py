from django.shortcuts import render, redirect
from django.views import View
from .models import MyUser, Course, Section
from typing import Dict, Type
from django.http import QueryDict, HttpRequest, HttpResponse

from typing import Dict, Type

from django.http import QueryDict, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import MyUser, Course, Section

class home(View):
    def get(self,request):
        request.session.pop("Uname", None)
        return render(request,"home.html",{})

    def post(self,request):
        print(request.POST['Uname'] + request.POST['Pass'])
        m = None
        try:
            m = MyUser.objects.get(username=request.POST['Uname'])
            request.session["name"] = m.name
        except:
            pass
        if m is not None and m.password == request.POST['Pass']:
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
        Username = request.session.get("name")
        return render(request, "home_Admin.html", {"home_Admin": home_Admin, "Username": Username})

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

    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": "", "user": MyUser()}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        return render(request, "admin_CreateNewUser.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        (validUser, error, user) = validate_user(request.POST)
        if (validUser):
            user.save()
            ret = redirect("home_Admin.html")
        else:
            ctx["error"] = error
            ctx["user"] = user
            ret = render(request, "admin_CreateNewUser.html", ctx)

        return ret


class admin_EditUser1(View):

    def get_base_ctx(self) -> Dict[str, any]:

        ctx = {}

        all_users = MyUser.objects.all()

        user_names = map(lambda user: (user.id, user.name), all_users)
        usernames = map(lambda user: (user.id, user.username), all_users)

        ctx["user_names"] = list(user_names)
        ctx["usernames"] = list(usernames)

        return ctx

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        all_users = MyUser.objects.all()
        user_names = map(lambda user: (user.id, user.name), all_users)
        usernames = map(lambda user: (user.id, user.username), all_users)

        ctx = self.get_base_ctx()

        return render(request, "admin_EditUser1.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        (username, user_name) = (request.POST["username"], request.POST["user_name"])

        if (username != '' and user_name != ''):
            username, user_name = '', ''

        user_id = username if user_name == '' else user_name

        ctx = self.get_base_ctx()

        if (user_id == ''):
            ctx["error"] = "please select either username or user name"
            ret = render(request, "admin_EditUser1.html", ctx)
        else:
            request.session["selectedUser"] = user_id
            ret = redirect("admin_EditUser2.html")

        return ret


class admin_EditUser2(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        user_id = request.session.get("user_id", None)
        if (user_id is None):
            ret = redirect("admin_EditUser1.html")
        else:
            ctx["user"] = MyUser.objects.get(id=user_id)
            ret = render(request, "admin_EditUser2.html", ctx)
        return ret

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        user_id = request.session.get("user_id", None)
        if (user_id is None):
            ret = redirect("admin_EditUser1.html")
        else:
            (validUser, error, user) = validate_user(request.POST)
            if (validUser):
                user.save()
                ret = redirect("home_Admin.html")
            else:
                ctx["error"] = error
                ctx["user"] = user
                ret = render(request, "admin_EditUser2.html", ctx)

        return ret


class admin_CreateCourse(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"error": "", "course": Course()}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        return render(request, "admin_CreateCourse.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        (validCourse, error, course) = validate_course(request.POST)
        if (validCourse):
            course.save()
            ret = redirect("home_Admin.html")
        else:
            ctx["error"] = error
            ctx["course"] = course
            ret = render(request, "admin_CreateCourse.html", ctx)

        return ret

class admin_AddCourseSection(View):

    def get_base_ctx(self) -> Dict[str, str]:
        return {"error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass


class admin_EditCourse1(View):

    def get_base_ctx(self) -> Dict[str, str]:
        return {"error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass


class admin_EditCourse2(View):

    def get_base_ctx(self) -> Dict[str, str]:
        return {"error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        pass


# --- HELPER METHODS ---
# *** NEED UNIT TESTS ***


def verify_request(req: HttpRequest, access: str) -> (bool, MyUser, HttpResponse):
    uname = req.session.get("Uname", None)

    if (uname is None):
        return (False, None, redirect("/"))

    user = MyUser.objects.get(username=uname)

    if (user.access == access):
        return (True, user, None)

    return (False, None, redirect(home_page(user.access)))


def home_page(access: str) -> str:
    ret = "/"

    if (access == "a"):
        ret += "home_Admin"
    elif (access == "b"):
        ret += "InstructorPage"
    elif (access == "c"):
        ret += "TAPage"

    return ret


def validate_user(post: Type[QueryDict]) -> (bool, str, MyUser):
    fields = {"name": None, "username": None, "password": None, "access": None, "office": None, "phoneNum": None,
              "email": None, "officeHours": None, "course": None}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    if ('' in fields.values()):
        return (False, "all fields are required", None)

    if (fields["role"] not in ["a", "b", "c"]):
        return (False, "invalid role", None)

    u = MyUser(
        name=fields["name"],
        username=fields["username"],
        password=fields["password"],
        access=fields["access"],
        office=fields["office"],
        phoneNum=fields["phoneNum"],
        email=fields["email"],
        officeHours=fields["officeHours"],
    )

    return (True, None, u)


def validate_course(post: Type[QueryDict]) -> (bool, str, Course):
    fields = {"name": None, "number": None, "department": None, "info": None, "instructor_id": None}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    if ('' in fields.values()):
        return (False, "all fields are required", None)

    c = Course(
        name=fields["name"],
        number=fields["number"],
        # department?
        info=fields["info"],
        instructor_id=fields["instructor_id"]
    )

    return (True, None, c)

def validate_section(post: Type[QueryDict]) -> (bool, str, Section):
    fields = {"number": None}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    if ('' in fields.values()):
        return (False, "all fields are required", None)

    s = Section(
        number=fields["number"]
    )

    return (True, None, s)