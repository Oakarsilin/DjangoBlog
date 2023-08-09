from django import forms
from .models import todoList

class Styling:
    title = {
        'placeholder' : 'Enter Title',
        'class' : 'form-control w-25',
        'id' : 'todolist-title'
    }

    task = {
        'placeholder' : 'Description',
        'id' : 'todolist-description',
        'class' : 'form-control w-25'
    }

    action = {
        'placeholder' : 'Action',
        'id' : 'todolist-action',
        'class' : 'form-control w-25'
    }

class todolistForm (forms.Form):
    title = forms.CharField (max_length=30, min_length=4, strip=True, required=True, label='Title', 
                                widget=forms.TextInput(attrs=Styling.title))
    description = forms.CharField (max_length=100, min_length=4, required=True, label='Task',
                                widget=forms.Textarea(attrs=Styling.task))
    action = forms.ChoiceField (choices=todoList.ACTION_CHOICES, required=True, label='Action',
                                widget=forms.Select(attrs=Styling.action))