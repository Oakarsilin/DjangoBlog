from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import todolistForm
from .models import todoList

# Create your views here.
@login_required(login_url='/account/login/')
def todoListView(request):
    model = todoList.objects.all()
    context = {'items' : model}
    return render(request, 'userhomepage.html', context)

@login_required(login_url='/account/login/')
def todoListCreate(request):
    form = todolistForm (request.POST) if request.method == "POST" else todolistForm()
    if form.is_valid():
        get_data = form.clean()
        model = todoList.objects.create (**get_data)
        messages.success(request, message='Create Successful', fail_silently=True)
        return redirect ('todolist.all')
    return render (request, 'todolistCreate.html', {'form':form})