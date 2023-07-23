from django.shortcuts import render
from .forms import Registration
from .models import User

# Create your views here.
def home_view (request):
    context = {
        'title' : 'Home',
        'name' : 'Oakar',
        'age' : '30 Years',
        'job' : 'Programmer',
        'address' : 'Mandalay',
        'skills' : ['Doctor', 'MBA', 'Programmer', 'Entrepreneur']
    }
    return render (request, 'home.html', context=context)

def about_view (request):
    return render (request, 'about.html')

def register_view (request):
    form = Registration(request.POST)
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
    return render (request, 'register.html',  {'form' : form})