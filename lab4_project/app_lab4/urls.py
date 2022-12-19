#from Django.contrib import admin
#from Django.URLs import path

from django.urls import path,re_path
from . import views
#from django.conf.urls import url 
#from django.conf.urls import url 

urlpatterns = [
    # path('update/',views.show_user_update,name='show_user_update'),
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('list_student/', views.list_student, name='list_student'),
    path('action_student/', views.action_student, name='action_student'),
    path('edit_action/', views.edit_action, name='edit_action'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_action/', views.add_action, name='add_action'),
    path('search_student/', views.search_student, name='search_student'),
    path('search_validate/', views.search_validate, name='search_validate'),
    path('api/students/<int:pk>/', views.student_details, name='student_details'),
    path('api/students/', views.student_list, name='student_list'),
    

]