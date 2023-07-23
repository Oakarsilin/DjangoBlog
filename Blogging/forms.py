from django import forms

class Styling:
    pwdAttrs = {
        'placeholder' : 'Enter Your Password',
        'class' : 'form-control w-25',
        'id' : 'passwordOne'
    }

    userAttrs = {
        'placeholder' : 'Enter Your Username',
        'class' : 'form-control w-25'
    }

class Registration (forms.Form):
    username = forms.CharField (max_length=16, min_length=4, strip=True, required=True, label='Username', 
                                widget=forms.TextInput(attrs=Styling.userAttrs))
    password = forms.CharField (max_length=16, min_length=8, strip=True, required=True, label='Password',
                                widget=forms.PasswordInput(attrs=Styling.pwdAttrs))