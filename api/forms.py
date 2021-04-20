from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Schedule

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class searchForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['train_from', 'train_to', 'date']
