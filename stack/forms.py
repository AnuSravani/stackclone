from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stack.models import Questions,UserProfile


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=["description","image"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["profile_pic","bio"]
