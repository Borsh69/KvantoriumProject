from django import forms
from .models import *


class LoginForm(forms.Form):
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input', 'type': 'password'}))


class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'kvantum', 'face', 'description', 'creators', 'PDFdescription', 'contact']


class AddAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'description', 'photo', 'age', 'email',
             'login', 'password', 'size', 'city']