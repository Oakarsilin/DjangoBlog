from django.shortcuts import render
from .forms import Registration

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
    form = Registration()
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST['password']
        print (username, password)
        return render (request, 'register.html', {'form' : form})
    return render (request, 'register.html',  {'form' : form})