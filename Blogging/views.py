from django.shortcuts import render
from django.contrib.auth.models import User

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