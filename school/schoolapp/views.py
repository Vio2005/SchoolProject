from django.shortcuts import render,redirect,HttpResponse
from.models import *
from .forms import *

def homepage(request):
    teacher_data=Teacher.objects.all()
    course_data=Course.objects.all()
    context={'teacher_data':teacher_data,'course_data':course_data}
    
    return render(request,'index.html',context)

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    course_data=Course.objects.all()
    context={'course_data':course_data}
    return render(request,'courses.html',context)

def trainers(request):
    teacher_data=Teacher.objects.all()
    context={'teacher_data':teacher_data}
    return render(request,'trainers.html',context)



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

   
