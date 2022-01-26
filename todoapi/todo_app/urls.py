from django.urls import path
from todo_app import views

urlpatterns = [
    path('task_list/', views.task_list),
    path('task_create/', views.task_create),
    path('task_detail/<int:pk>/', views.task_detail),
    path('task_delete/<int:pk>/', views.task_delete),
]
