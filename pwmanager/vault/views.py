from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm
from .models import Entry, encrypt_password, decrypt_password


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
    # FLAW (Identification and Authentication Failures)
    # FIX:
    #logout(request)
    return redirect('login')


@login_required
def index(request):
    query = request.GET.get('q', '')
    if query:
        # FLAW (Injection)
        sql = "SELECT * FROM vault_entry WHERE owner_id = {} AND site_url LIKE '%{}%'".format(request.user.id, query)
        entries = Entry.objects.raw(sql)
        # FIX:
        # entries = Entry.objects.filter(owner=request.user, site_url__icontains=query)
    else:
        entries = Entry.objects.filter(owner=request.user)
    # FLAW (Cryptographic Failures) 1/2
    # FIX:
    # for entry in entries:
    #     entry.password = decrypt_password(entry.password)
    return render(request, 'index.html', {'entries': entries, 'query': query})


@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            # FLAW (Cryptographic Failures) 2/2
            # FIX:
            # entry.password = encrypt_password(entry.password)
            entry.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'add_entry.html', {'form': form})


@login_required
def delete_entry(request, pk):
    # FLAW (Broken Access Control)
    # FIX:
    # entry = get_object_or_404(Entry, pk=pk, owner=request.user)
    entry = get_object_or_404(Entry, pk=pk)
    # FLAW (CSRF)
    # FIX:
    # if request.method == 'POST':
    #     entry.delete()
    #     return redirect('index')
    # return render(request, 'delete_entry.html', {'entry': entry})
    entry.delete()
    return redirect('index')