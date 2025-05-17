from django.urls import path
from.views import *

urlpatterns=[
    path('homepage/',homepage,name='homepage'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('courses/',courses,name='courses'),
    path('trainers/',trainers,name='trainers'),
    path('addteacher/',addteacher,name='addteacher'),
    path('addcourse/',addcourse,name='addcourse'),
    path('coursedetail/<int:id>/',coursedetail,name='coursedetail'),
    path('updatecourse/<int:id>/',updatecourse,name='updatecourse'),
    path('teacherdetail/<int:id>/',teacherdetail,name='teacherdetail'),
    path('updateteacher/<int:id>/',updateteacher,name='updateteacher'),
    path('deleteteacher/<int:id>/',deleteteacher,name='deleteteacher'),
    path('deletecourse/<int:id>/',deletecourse,name='deletecourse'),
    path('',base,name='base'),
]