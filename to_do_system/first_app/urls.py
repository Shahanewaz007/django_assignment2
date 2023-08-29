from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo_store/', views.todo_store, name='todo_store'),
    path('show_todo/', views.show_todo, name='show_todo'),
    path('edit_todo/<int:id>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:id>', views.complete_todo, name='complete_todo'),
    path('complete_task_view/', views.complete_task_view, name='complete_task_view'),
    path('complete_task_delete/<int:id>', views.complete_task_delete, name='complete_task_delete'),
]