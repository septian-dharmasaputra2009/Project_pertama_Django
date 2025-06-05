from django.shortcuts import render, redirect
from .models import Artikel, Buku
from .forms import BukuForm
from .forms import ArtikelForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#home
def home(request):
    query = request.GET.get('q')
    if query:
        artikel_list = Artikel.objects.filter(judul__icontains=query)
    else:
        artikel_list = Artikel.objects.all()
    return render(request, 'home.html', {'artikel': artikel_list, 'query': query})
#perpustakaan
def daftar_buku(request):
    bukus = Buku.objects.all()
    return render(request, 'daftar_buku.html', {'bukus': bukus})

def tambah_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm()
    return render(request, 'tambah_buku.html', {'form': form})

def baca_buku(request, buku_id):
    buku = Buku.objects.get(pk=buku_id)
    return render(request, 'baca_buku.html', {'buku': buku})
#tambah komen
def tambah_artikel(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect ke halaman utama
    else:
        form = ArtikelForm()
    return render(request, 'halaman/tambah.html', {'form': form})
#hanya admin yang bisa edit & hapus
@login_required
def edit_artikel(request, id):
    artikel = get_object_or_404(Artikel, id=id)
    if request.method == 'POST':
        form = ArtikelForm(request.POST, instance=artikel)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtikelForm(instance=artikel)
    return render(request, 'halaman/edit.html', {'form': form, 'artikel': artikel})

@login_required
def hapus_artikel(request, id):
    artikel = get_object_or_404(Artikel, id=id)
    artikel.delete()
    return redirect('home')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def edit_buku(request, buku_id):
    buku = Buku.objects.get(pk=buku_id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm(instance=buku)
    return render(request, 'edit_buku.html', {'form': form, 'buku': buku})