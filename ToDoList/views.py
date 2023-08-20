from typing import Dict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
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
        item = todoList.objects.create (**get_data)
        new_message = f'Title : {item.title} New Task Added Successfully!!'
        messages.success(request, message=new_message, fail_silently=True)
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

class todoListUpdate (LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/account/login/'
    model = todoList
    template_name = 'todoListUpdate.html'
    form_class = todolistForm
    success_url = '/todolist/allitem/'
    success_message =  'Task Edited Successfully!!'
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

class todoListDelete (LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/account/login/'
    model = todoList
    form_class = todolistForm
    template_name = 'todolistDelete.html'
    # success_url = '/todolist/allitem/'
    success_url = reverse_lazy('todolist.all')
    success_message =  "Title : %(title)s was Deleted Successfully!!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context['form'] = self.form_class (instance=item)
        return context
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )