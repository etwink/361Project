from django.shortcuts import render, redirect
from django.views import View
from .models import MyUser, Course, Section
from typing import Dict, Type
from django.http import QueryDict, HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist


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
            ret = redirect("/home_Admin")
        else:
            ctx["error"] = error
            ctx["user"] = user
            print(ctx)
            ret = render(request, "admin_CreateNewUser.html", ctx)

        return ret


class admin_EditUser1(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"users": MyUser.objects.all(), "error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

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
            ret = redirect("/admin_EditUser2.html")

        return ret


class admin_EditUser2(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        user_id = request.session.get("selectedUser", None)
        if (user_id is None):
            ret = redirect("/home_Admin/admin_EditUser1.html")
        else:
            ctx["user"] = MyUser.objects.get(id=user_id)
            ret = render(request, "admin_EditUser2.html", ctx)

        return ret

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        user_id = request.session.get("selectedUser", None)
        if (user_id is None):
            ret = redirect("/home_Admin/admin_EditUser1.html")
        else:
            (validUser, error, user) = validate_user(request.POST)
            if (validUser):
                user.id = user_id
                user.save()
                ret = redirect("/home_Admin")
            else:
                ctx["error"] = error
                ctx["user"] = user
                ret = render(request, "admin_EditUser2.html", ctx)

        return ret


class admin_CreateCourse(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"error": "", "course": Course(), "instructors": MyUser.objects.all() }

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
            ret = redirect("/home_Admin")
        else:
            ctx["error"] = error
            ctx["course"] = course
            ret = render(request, "admin_CreateCourse.html", ctx)

        return ret

class admin_AddCourseSection1(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": ""}

    def get_two_ctx(self, course_id) -> Dict[str, any]:
        return {"course": Course.objects.get(id=course_id)}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        return render(request, "admin_AddCourseSection1.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        course_id = request.POST["course_id"]
        ctx = self.get_base_ctx()
        if (course_id == ''):
            ctx["error"] = "please select a course"
            ret = render(request, "admin_AddCourseSection1.html", ctx)
        else:
            request.session["selectedCourse"] = course_id
            ret = redirect("/home_Admin/admin_AddCourseSection2.html")
            # ret = render(request, "admin_AddCourseSection2.html", {"course":course_id})

        return ret


class admin_AddCourseSection2(View):

    def get_base_ctx(self, course_id) -> Dict[str, any]:
        return {"course": "", "section": Section(), "teachingAssistants": MyUser.objects.filter(access="c"), "instructors": MyUser.objects.filter(access="b"), "sections": Section.objects.filter(course=course_id), "error": ""}



    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        course_id = request.session.get("selectedCourse", None)
        # course_id = request.POST.get("course", None)
        ctx = self.get_base_ctx(course_id)


        if (course_id is None):
            ret = redirect("/home_Admin/admin_AddCourseSection1.html")
        else:
            ctx["course"] = Course.objects.get(id=course_id)
            ret = render(request, "admin_AddCourseSection2.html", ctx)

        return ret


    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        course_id = request.session.get("selectedCourse", None)
        ctx = self.get_base_ctx(course_id)
        course = Course.objects.get(id=course_id)

        (validSection, error, section) = validate_section(request.POST, course)
        if (validSection):
            section.save()
            request.session["selectedCourse"] = course_id
            ret = redirect("/home_Admin/admin_AddCourseSection2.html")
            # ret = render(request, "admin_AddCourseSection2.html", {"course":course_id})
        else:

            ctx["error"] = error
            ctx["course"] = course
            # request = request.session["selectedCourse"] = course_id
            ret = render(request, "admin_AddCourseSection2.html", ctx)
            # ret = render(request, "admin_AddCourseSection2.html", ctx,)

        return ret




class admin_EditCourse1(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        return render(request, "admin_EditCourse1.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        course_id = request.POST["course_id"]

        ctx = self.get_base_ctx()

        if (course_id == ''):
            ctx["error"] = "please select a course"
            ret = render(request, "admin_EditCourse1.html", ctx)
        else:
            request.session["selectedCourse"] = course_id
            ret = redirect("/home_Admin/admin_EditCourse2.html")

        return ret


class admin_EditCourse2(View):

    def get_base_ctx(self) -> Dict[str, any]:
        return {"error": ""}

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        course_id = request.session.get("selectedCourse", None)
        if (course_id is None):
            ret = redirect("/home_Admin/admin_EditCourse1.html")
        else:
            ctx["course"] = Course.objects.get(id=course_id)
            ret = render(request, "admin_EditCourse2.html", ctx)

        return ret

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, _, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        course_id = request.session.get("selectedCourse", None)
        if (course_id is None):
            ret = redirect("/admin_EditCourse1.html")
        else:
            (validCourse, error, course) = validate_course(request.POST)
            if (validCourse):
                course.save()
                ret = redirect("/home_Admin")
            else:
                ctx["error"] = error
                ctx["course"] = course
                ret = render(request, "admin_EditCourse2.html", ctx)

        return ret

class edit_information(View):
    def get_base_ctx(self) -> Dict[str, any]:
        return {"courses": Course.objects.all(), "error": "", "user": MyUser(), }

    def get(self, request: HttpRequest) -> HttpResponse:

        (validReq, user, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        ctx["user"] = user

        return render(request,"edit_information.html", ctx)

    def post(self, request: HttpRequest) -> HttpResponse:

        (validReq, c, redirectAction) = verify_request(request, "a")
        if (not validReq):
            return redirectAction

        ctx = self.get_base_ctx()

        (validUser, error, user) = validate_edit_user(request.POST)
        if (validUser):
            user.id = c.id
            user.save()
            ctx["user"] = user
            ret = render(request, "edit_Information.html", ctx)
        else:
            ctx["error"] = error
            ctx["user"] = user
            print(ctx)
            ret = render(request, "edit_Information.html", ctx)

        return ret


# --- HELPER METHODS ---
# *** NEED UNIT TESTS ***


def verify_request(req: HttpRequest, access: str) -> (bool, MyUser, HttpResponse):
    uname = req.session.get("Uname", None)

    if (uname is None):
        return (False, None, redirect("/"))

    user = MyUser.objects.get(username=uname)

    if (user.access in access):
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

def validate_edit_user(post: Type[QueryDict]) -> (bool, str, MyUser):
    fields = {"Name": None, "Username": None, "Password": None, "Office": None, "Phone Number": None,
              "Email": None, "Office Hours": None,}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()



    u = MyUser(
        name=fields["Name"],
        username=fields["Username"],
        password=fields["Password"],
        office=fields["Office"],
        phoneNum=fields["Phone Number"],
        email=fields["Email"],
        officeHours=fields["Office Hours"],
    )

    if ('' in fields.values()):
        return (False, "all fields are required", u)

    return (True, None, u)

def validate_user(post: Type[QueryDict]) -> (bool, str, MyUser):
    fields = {"Name": None, "Username": None, "Password": None, "Access": None, "Office": None, "Phone Number": None,
              "Email": None, "Office Hours": None,}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    u = MyUser(
        name=fields["Name"],
        username=fields["Username"],
        password=fields["Password"],
        access=fields["Access"],
        office=fields["Office"],
        phoneNum=fields["Phone Number"],
        email=fields["Email"],
        officeHours=fields["Office Hours"]
    )

    if ('' in fields.values()):
        return (False, "all fields are required", u)

    if (fields["Access"] not in ["a", "b", "c"]):
        return (False, "invalid role", u)

    return (True, None, u)


def validate_course(post: Type[QueryDict]) -> (bool, str, Course):
    fields = {"name": None, "number": None, "department": None, "info": None,}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    # if ('' in fields.values()):
    #      return (False, "all fields are required", None)
    if ('' in fields.values()):
         return (False, "all fields are required", None)
    try:
        Course.objects.get(name=fields["name"], number=fields["number"])
        return (False, fields["name"] + " " + fields["number"] + " already exists", None)
    except ObjectDoesNotExist:
        pass

    # if(fields["number"] == str(Course.objects.filter(name=fields["name"]).filter(number=int(fields["number"])).number)):
    #     return (False, fields["name"] + fields["number"] + " already exists", None)
    c = Course(
        name=fields["name"],
        number=fields["number"],
        # instructor_id=fields["Instructor"],
        info=fields["info"],
    )

    return (True, None, c)

def validate_section(post: Type[QueryDict], course_id) -> (bool, str, Section):
    fields = {"number": None, "teachingAssistant": None}

    for field_key in fields.keys():
        fields[field_key] = post.get(field_key, '').strip()

    if ('' in fields.values()):
        return (False, "all fields are required", None)

    s = Section(
        number=fields["number"],
        teachingAssistant_id=fields["teachingAssistant"],
        course=course_id,
    )

    return (True, None, s)