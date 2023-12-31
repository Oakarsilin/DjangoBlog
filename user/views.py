from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def register_view (request):
    form = Registration(request.POST) if request.method == "POST" else Registration()
    # if request.method == 'POST':
    #     username = request.POST.get ('username')
    #     password = request.POST['password']
    #     user.username = username
    #     user.password = password
    #     user.save()
    #     print (username, password)
    #     return render (request, 'register.html', {'form' : form})
    if form.is_valid():
        cleaned_form = form.clean()
        cleaned_form['password'] = make_password (cleaned_form['password'])
        User.objects.create (**cleaned_form)
        return redirect ('blog.home')
    return render (request, 'register.html', {'form' : form})

def login_view (request):
    form = Login(request.POST) if request.method == "POST" else Login()
    context = {'title' : 'Login'}
    if form.is_valid():
        get_credential = form.clean()
        user = auth.authenticate (**get_credential)
        if user is not None:
            auth.login (request, user)
            return redirect ('todolist.all')
        messages.error (request, 'Wrong username or password !!')
    return render (request, 'login.html', {'form' : form})

def logout_view (request):
    auth.logout(request)
    messages.success(request, message='You have been logged out', fail_silently=True)
    return redirect('blog.home')