from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm
from .models import Entry


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    entries = Entry.objects.filter(owner=request.user)
    return render(request, 'index.html', {'entries': entries})


@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'add_entry.html', {'form': form})


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, owner=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('index')
    return render(request, 'delete_entry.html', {'entry': entry})