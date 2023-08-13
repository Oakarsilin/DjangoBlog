from typing import Any, Dict, Optional
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

class TextareawithValue(forms.Textarea):

    def __init__(self, attrs, value) -> None:
        super().__init__(attrs)
        self.value = value

    def get_context(self, name, value, attrs) -> Dict[str, Any]:
        context = super().get_context(name, self.value, attrs)
        return context
    
class WidgetOR:

    def __init__(self, FormObj, StyleObj, type=None) -> None:
        self.form = FormObj
        self.style = StyleObj
        self.type = type

    def createFormObj (self, **kwargs):
        if self.type == None:
            self.style.update(**kwargs)
            return self.form(attrs=self.style)
        value = kwargs
        self.form = TextareawithValue(self.style, value['value'])
        return self.form
    
class todolistForm (forms.Form):
    title = forms.CharField (max_length=30, min_length=4, strip=True, required=True, label='Title', 
                                widget=forms.TextInput(attrs=Styling.title))
    description = forms.CharField (max_length=100, min_length=4, required=True, label='Task',
                                widget=forms.Textarea(attrs=Styling.task))
    action = forms.ChoiceField (choices=todoList.ACTION_CHOICES, required=True, label='Action',
                                widget=forms.Select(attrs=Styling.action))