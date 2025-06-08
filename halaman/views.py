from django.shortcuts import render, redirect
from .models import Artikel, Buku, Halaman
from .forms import BukuForm, ArtikelForm, HalamanFormSet, HalamanForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from math import ceil

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
    buku_list = Buku.objects.all().order_by('judul')
    return render(request, 'daftar_buku.html', {
        'daftar_buku': buku_list
    })

def daftar_isi(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    halaman = Halaman.objects.filter(buku=buku).order_by('nomor')

    # Ambil total halaman
    total_halaman = halaman.count()
    halaman_per_group = 10
    grup_daftar_isi = []

    for i in range(0, total_halaman, halaman_per_group):
        start = halaman[i].nomor
        end = halaman[min(i + halaman_per_group - 1, total_halaman - 1)].nomor
        grup_daftar_isi.append({
            'label': f"Halaman {start}–{end}",
            'start_page': start,
        })

    return render(request, 'daftar_isi.html', {
        'buku': buku,
        'grup_daftar_isi': grup_daftar_isi,
    })

def tambah_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        formset = HalamanFormSet(request.POST, queryset=Halaman.objects.none())
        if form.is_valid() and formset.is_valid():
            buku = form.save()
            for halaman_form in formset:
                if halaman_form.cleaned_data and not halaman_form.cleaned_data.get('DELETE', False):
                    halaman = halaman_form.save(commit=False)
                    halaman.buku = buku
                    halaman.save()
                return redirect('daftar_buku')
    else:
        form = BukuForm()
        formset = HalamanFormSet(queryset=Halaman.objects.none())

        return render(request, 'tambah_buku.html', {
        'form': form,
        'formset': formset
    })

def baca_buku(request, buku_id, halaman_awal=1):
    buku = get_object_or_404(Buku, pk=buku_id)
    semua_halaman = Halaman.objects.filter(buku=buku).order_by('nomor')
    total_halaman = semua_halaman.count()

    halaman_awal = max(1, halaman_awal)
    halaman_akhir = min(halaman_awal + 9, total_halaman)

    halaman_list = semua_halaman[halaman_awal - 1 : halaman_akhir]

    # Hitung halaman next & prev
    next_page = halaman_akhir + 1 if halaman_akhir < total_halaman else None
    prev_page = halaman_awal - 10 if halaman_awal > 1 else None

    return render(request, 'baca_buku.html', {
        'buku': buku,
        'halaman_list': halaman_list,
        'halaman_awal': halaman_awal,
        'halaman_akhir': halaman_akhir,
        'total_halaman': total_halaman,
        'next_page': next_page,
        'prev_page': prev_page,
    })
from django.contrib import messages
from django.forms import modelformset_factory
@login_required
def edit_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    HalamanFormSet = modelformset_factory(Halaman, form=HalamanForm, extra=0, can_delete=True)

    # Hapus buku jika tombol hapus ditekan
    if request.method == 'POST' and 'hapus_buku' in request.POST:
        buku.delete()
        messages.success(request, 'Buku berhasil dihapus.')
        return redirect('daftar_buku')

    # Proses update buku dan halaman
    if request.method == 'POST':
        buku_form = BukuForm(request.POST, instance=buku)
        formset = HalamanFormSet(request.POST, queryset=Halaman.objects.filter(buku=buku))

        if buku_form.is_valid() and formset.is_valid():
            buku_form.save()
            formset.save()
            messages.success(request, 'Buku berhasil diperbarui.')
            return redirect('daftar_buku')
    else:
        buku_form = BukuForm(instance=buku)
        formset = HalamanFormSet(queryset=Halaman.objects.filter(buku=buku))

    return render(request, 'edit_buku.html', {
        'buku_form': buku_form,
        'formset': formset,
        'buku': buku
    })

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

