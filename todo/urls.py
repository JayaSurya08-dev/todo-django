from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),  # Home route shows the task list
    path('complete/<int:task_id>',views.complete_task,name='complete-task'),
    path('delete/<int:task_id>',views.delete_task,name='delete-task'),
    path('edit/<int:task_id>',views.edit_task,name='edit-task'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]