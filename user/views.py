from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib.auth.models import User
from django.contrib import auth, messages

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
        User.objects.create (**cleaned_form)
        return render (request, 'home.html')
    return render (request, 'register.html', {'form' : form})

def login_view (request):
    form = Login(request.POST) if request.method == "POST" else Login()
    if form.is_valid():
        get_credential = form.clean()
        user = auth.authenticate (**get_credential)
        if user is not None:
            auth.login (request, user)
            return render (request, 'userhomepage.html')
        messages.error (request, 'wrong credential')
    return render (request, 'login.html', {'form' : form})

def logout_view (request):
    auth.logout(request)
    return redirect('blog.home')