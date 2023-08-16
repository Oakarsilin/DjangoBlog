from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import todolistForm, Styling
from .models import todoList

# Create your views here.
# @login_required(login_url='/account/login/')
# def todoListView(request):
#     model = todoList.objects.all()
#     context = {'items' : model, 'title' : 'To Do List'}
#     return render(request, 'userhomepage.html', context)

class todoListView (LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    model = todoList
    template_name = 'userhomepage.html'
    context_object_name = 'items'

@login_required(login_url='/account/login/')
def todoListCreate(request):
    form = todolistForm (request.POST) if request.method == "POST" else todolistForm()
    if form.is_valid():
        get_data = form.clean()
        todoList.objects.create (**get_data)
        messages.success(request, message='New Task Added', fail_silently=True)
        return redirect ('todolist.all')
    return render (request, 'todolistCreate.html', {'form':form})

'''@login_required(login_url='/account/login/')
def todoListUpdate(request, pk):
    todolist = todoList.objects.get(pk=pk)
    form = todolistForm (request.POST) if request.method == "POST" else todolistForm()
    if form.is_valid():
        get_data = form.clean()
        todoList.objects.update (**get_data)
        messages.success(request, message='Update Successful', fail_silently=True)
        return redirect ('todolist.all')
    if todoList is not None:
        Styling.title['placeholder'] = todolist.title
        Styling.task['placeholder'] = todolist.description
        Styling.action['placeholder'] = todolist.action
        form = todolistForm()
    return render (request, 'todolistCreate.html', {'form':form})'''

class todoListUpdate (LoginRequiredMixin, UpdateView):
    login_url = '/account/login/'
    model = todoList
    template_name = 'todoListUpdate.html'
    # form_class = todolistForm
    success_url = '/todolist/allitem/'
    fields = ['title', 'description', 'action']
    