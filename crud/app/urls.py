from django.urls import path
from . import views

urlpatterns = [
    path('', views.listTask, name="home"),
    path('create-task/', views.createTask, name="create_task"),
    path('update-task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete_task"),
]
