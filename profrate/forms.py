from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Prof, School
from django.forms import ModelForm

# Add your forms here


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddProfForm(ModelForm):
    class Meta:
        model = Prof
        exclude = ['created_date']


class AddSchoolForm(ModelForm):
    class Meta:
        model = School
        exclude = ['created_date']
