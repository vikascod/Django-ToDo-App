from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('delete/<int:id>/', views.delete_data, name='deletedata')
]
