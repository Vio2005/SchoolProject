from django.shortcuts import render,redirect,HttpResponse
from.models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View



def homepage(request):
    teacher_data=Teacher.objects.all()
    course_data=Course.objects.all()
    context={'teacher_data':teacher_data,'course_data':course_data}
    
    return render(request,'index.html',context)

def base(request):
    return render(request,'base.html')

def pricing(request):
    return render(request,'pricing.html')

def course_details(request):
    return render(request,'course-details.html')

@login_required(login_url='/loginview/')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def events(request):
    return render(request,'events.html')


def courses(request):
    course_data=Course.objects.all()
    context={'course_data':course_data}
    return render(request,'courses.html',context)

def trainers(request):
    teacher_data=Teacher.objects.all()
    context={'teacher_data':teacher_data}
    return render(request,'trainers.html',context)

def detailcourse(request):
    course_data=Course.objects.all()
    context={'course_data':course_data}
    return render(request,'detailcourse.html',context)

def detailteacher(request):
    teacher_data=Teacher.objects.all()
    context={'teacher_data':teacher_data}
    return render(request,'detailteacher.html',context)


def addteacher(request):
    
   teacher=TeacherModelForm()
   if request.method=="POST":
        teacher=TeacherModelForm(request.POST,request.FILES)
        if teacher.is_valid():
           
            teacher.save()
          
            return redirect('/trainers')
        else:
           
            return HttpResponse('Error')
   return render(request,'addteacher.html',{'teacher':teacher})

def addcourse(request):
    
    course=CourseModelForm()
    if request.method=="POST":
        course=CourseModelForm(request.POST,request.FILES)
        if course.is_valid():
          
            course.save()
          
            return redirect('/courses')
        else:
           
            return HttpResponse('Error')
    return render(request,'addcourse.html',{'course':course})


def coursedetail(request,id):
    data=Course.objects.filter(id=id)
    
    context={"data":data}
    return render(request,'updatecourse.html',context)

def updatecourse(request, id):

    data =Course.objects.get(id=id)
    obj = CourseModelForm(request.POST, request.FILES, instance=data)
    if obj.is_valid():
        obj.save()
    return redirect('/courses')


def teacherdetail(request,id):
    data=Teacher.objects.filter(id=id)
    
    context={"data":data}
    return render(request,'updateteacher.html',context)

def updateteacher(request, id):

    data =Teacher.objects.get(id=id)
    obj = TeacherModelForm(request.POST, request.FILES, instance=data)
    if obj.is_valid():
        obj.save()
    return redirect('/trainers')


def deleteteacher(request,id):
    data=Teacher.objects.filter(id=id).delete()
    return redirect('/trainers')


def deletecourse(request,id):
    data=Course.objects.filter(id=id).delete()
    return redirect('/courses')

def loginview(request):
    if request.method == 'POST':
    
        usr = request.POST.get('username')
        pas = request.POST.get('password')
        usr_auth=authenticate(username=usr,password=pas)
        if usr_auth:
            login(request, usr_auth)
            return redirect('/homepage')
        else:
            return redirect('/loginview')
    else:

        return render(request, 'login.html')
    
def logout(request):
    logout()
    return redirect('login/')

def register_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        user=User.objects.filter(username=username)
        if user.exists():
            return redirect('register/')
        else:
            usr=User.objects.create_user(username=username,first_name=firstname,last_name=lastname)
            usr.set_password(password)
            usr.is_staff=True
            usr.save()
            return redirect ('/loginview')
          
    else:
           
        
        return render(request,'register.html')

class LoginRequire(object):
    def dispatch(self,request,*arg,**kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect('/register')
        return super().dispatch(request,*arg,**kwargs)
    
class HomeView(LoginRequire,View):
    def get(self,request):
        return render(request,'index.html')



   
