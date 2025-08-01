from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Note

class NoteForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full border border-[#a78bfa] rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-[#a78bfa] bg-[#20143a] text-[#e5e7eb]'
        })
    )
    scheduled_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'w-full border border-[#a78bfa] rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-[#a78bfa] bg-[#20143a] text-[#e5e7eb]'
        })
    )
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'w-full border border-[#a78bfa] rounded px-3 py-2 bg-[#20143a] text-[#e5e7eb] focus:outline-none focus:ring-2 focus:ring-[#a78bfa]'
    }))
    attachment = forms.FileField(required=False, help_text='Upload a file (PDF, DOCX, etc.)', widget=forms.ClearableFileInput(attrs={
        'class': 'w-full border border-[#a78bfa] rounded px-3 py-2 bg-[#20143a] text-[#e5e7eb] focus:outline-none focus:ring-2 focus:ring-[#a78bfa]'
    }))
    class Meta:
        model = Note
        fields = ['title', 'content', 'scheduled_date', 'scheduled_time', 'photo', 'attachment']


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
