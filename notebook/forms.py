from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-green-300'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-green-300'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-green-300'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-green-300'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
