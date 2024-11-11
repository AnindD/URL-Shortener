from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.db import models 
 


class RegisterForm(UserCreationForm):
    email = models.EmailField
    class Meta: 
        model = User 
        fields = ["username", "email", "password1", "password2"] 
    username = forms.CharField(widget=forms.TextInput(attrs={'style': 'height: 42px; width: 550px', 'class': 'form-control rounded-0'}), max_length=100, label="Username", label_suffix="") 
    email = forms.CharField(widget=forms.TextInput(attrs={'style': 'height: 42px; width: 550px', 'class': 'form-control rounded-0'}), max_length=100, label="Email Address", label_suffix="") 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'height: 42px; width: 550px', 'class': 'form-control rounded-0'}), max_length=100, label="Password", label_suffix="") 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'height: 42px; width: 550px', 'class': 'form-control rounded-0'}), max_length=100, label="Password Confirmation", label_suffix="") 
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None



