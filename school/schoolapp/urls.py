from django.urls import path
from.views import *

urlpatterns=[
    path('homepage/',homepage,name='homepage'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('courses/',courses,name='courses'),
    path('contact/',contact,name='contact'),
    path('pricing/',pricing,name='pricing'),
    path('events/',events,name='events'),
    path('course_details/',course_details,name='course_details'),
    path('trainers/',trainers,name='trainers'),
    path('addteacher/',addteacher,name='addteacher'),
    path('addcourse/',addcourse,name='addcourse'),
    path('detailcourse/',detailcourse,name='detailcourse'),
    path('detailteacher/',detailteacher,name='detailteacher'),
    path('loginview/',loginview,name='loginview'),
    path('coursedetail/<int:id>/',coursedetail,name='coursedetail'),
    path('updatecourse/<int:id>/',updatecourse,name='updatecourse'),
    path('teacherdetail/<int:id>/',teacherdetail,name='teacherdetail'),
    path('updateteacher/<int:id>/',updateteacher,name='updateteacher'),
    path('deleteteacher/<int:id>/',deleteteacher,name='deleteteacher'),
    path('deletecourse/<int:id>/',deletecourse,name='deletecourse'),
    path('',base,name='base'),
    path('register/',register_view,name='register'),
    path('homeview/', HomeView.as_view(), name='HomeView')

]