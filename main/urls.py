from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy/del/', views.del_vacancy, name='del_vacancy'),
    path('vacancy/send_vacancy/', views.send_vacancy, name='update'),
    path('resume/', views.resume, name='resume'),
    path('resume/del/', views.del_resume, name='del_resume'),
    path('resume/send_resume/', views.send_resume, name='update'),
    path('questions/', views.questions, name='questions'),
    path('questions/make_answer/', views.make_answer, name='make_answer'),
    path('questions/make_answer/send_answer/', views.send_answer, name='send_answer'),
    path('questions/del/', views.del_question, name='del'),
]