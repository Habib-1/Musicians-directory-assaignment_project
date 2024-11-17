from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .import models
from django import forms

class register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2',]


class musician_form(forms.ModelForm):
    class Meta:
        model=models.Musicians
        fields='__all__'

class album_form(forms.ModelForm):
    class Meta:
        model=models.Album
        fields='__all__'