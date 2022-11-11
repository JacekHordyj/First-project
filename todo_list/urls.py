from django.urls import path
from . views import TaskCreate, TaskDelete, TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView
from . import views

urlpatterns = [
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name = 'task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('test/',views.test_view, name = 'test')
]
