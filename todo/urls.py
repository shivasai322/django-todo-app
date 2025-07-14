
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete-all/', views.delete_all_tasks, name='delete_all_tasks'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),

]
