from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import todolistForm, WidgetOR, Styling
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
        messages.success(request, message='New Task Added Successfully!!', fail_silently=True)
        return redirect ('todolist.all')
    return render (request, 'todolistCreate.html', {'form':form})

# @login_required(login_url='/account/login/')
# def todoListUpdate(request, pk):
#     todolist = todoList.objects.get(pk=pk)
#     if request.method == "POST":
#         form = todolistForm (request.POST)
#         if form.is_valid():
#             get_data = form.clean()
#             todolist.title = get_data['title']
#             todolist.description = get_data['description']
#             todolist.action = get_data['action']
#             todolist.save()
#             update_message = f'Title : {todolist.title} Updated Successfully!!'
#             messages.success(request, message=update_message, fail_silently=True)
#             return redirect ('todolist.all')
#     form = todolistForm()
#     form.fields['title'].widget = WidgetOR(forms.TextInput, Styling.title).createFormObj(value=todolist.title)
#     form.fields['description'].widget = WidgetOR(forms.Textarea, Styling.task, 'textarea').createFormObj(value=todolist.description)
#     return render (request, 'todoListUpdate.html', {'form':form})

class todoListUpdate (LoginRequiredMixin, UpdateView):
    login_url = '/account/login/'
    model = todoList
    template_name = 'todoListUpdate.html'
    form_class = todolistForm
    success_url = '/todolist/allitem/'
    # fields = ['title', 'description', 'action']

# @login_required(login_url='/account/login/')
# def todoListDelete(request, pk):
#     if request.method == "POST":
#         item = todoList.objects.get(id=pk)
#         del_message = f'Title : {item.title} Deleted Successfully!!'
#         messages.success(request, message=del_message, fail_silently=True)
#         item.delete()
#         return redirect ('todolist.all')
#     return redirect ('todolist.all')

class todoListDelete (LoginRequiredMixin, DeleteView):
    login_url = '/account/login/'
    model = todoList
    template_name = 'userhomepage.html'
    success_url = '/todolist/allitem/'