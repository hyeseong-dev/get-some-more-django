from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo'),
]
