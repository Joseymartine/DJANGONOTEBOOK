from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
import datetime
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import CustomRegisterForm

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-date_created')
    today = datetime.date.today()
    return render(request, 'notebook/note_list.html', {'notes': notes, 'today': today})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notebook/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        if 'delete' in request.POST:
            note.delete()
            messages.success(request, 'Note deleted successfully!')
            return redirect('note_list')
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notebook/note_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'notebook/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('note_list')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'notebook/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def landing_page(request):
    return render(request, 'notebook/landing.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'notebook/password_reset.html'
    email_template_name = 'notebook/password_reset_email.html'
    subject_template_name = 'notebook/password_reset_subject.txt'
    success_url = '/password-reset/done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'notebook/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'notebook/password_reset_confirm.html'
    success_url = '/login/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'notebook/password_reset_complete.html'

