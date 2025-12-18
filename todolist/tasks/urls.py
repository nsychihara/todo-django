from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskToggleView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('toggle/<int:pk>/', TaskToggleView.as_view(), name='task_toggle'),
]
