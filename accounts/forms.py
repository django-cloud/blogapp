from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#for creating new user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

#for updating User(inbuilt model) information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

#for updating user profile
class ProfileUpdateForm(forms.ModelForm):
    #to remove the currently and clear
    image = forms.ImageField(label=('Profile Image'), required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ('image',)

