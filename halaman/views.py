from django.shortcuts import render, redirect
from .models import Artikel
from .forms import ArtikelForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    query = request.GET.get('q')
    if query:
        artikel_list = Artikel.objects.filter(judul__icontains=query)
    else:
        artikel_list = Artikel.objects.all()
    return render(request, 'home.html', {'artikels': artikel_list, 'query': query})

def tambah_artikel(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect ke halaman utama
    else:
        form = ArtikelForm()
    return render(request, 'halaman/tambah.html', {'form': form})

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