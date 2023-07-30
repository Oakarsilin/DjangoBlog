from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('registration/', register_view, name='blog.register'),
    path('login/', login_view, name='blog.login'),
    path('logout/', logout_view, name='blog.logout')
]