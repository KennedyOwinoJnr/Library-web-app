from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

#cleating a class to allow user to register on the registration page
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#creating user forms where the user can update their email and username on the frontend

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#creating a class to allow userr to update their profile picture

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = profile
        fields = ['image']