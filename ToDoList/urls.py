from django.urls import path
from .views import todoListView, todoListCreate

urlpatterns = [
    path ('allitem/', todoListView, name='todolist.all'),
    path ('', todoListView),
    path ('new/', todoListCreate, name='todolist.new')
]