from django import forms
from .models import Artikel, Buku, Halaman
from django.forms import modelformset_factory


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi']

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul', 'penulis', 'cover_url', 'deskripsi', 'pdf_url']

class HalamanForm(forms.ModelForm):
    class Meta:
        model = Halaman
        fields = ['gambar_url', 'nomor']

HalamanFormSet = modelformset_factory(
    Halaman,
    form=HalamanForm,
    extra=1,           # Mulai dengan 1 form kosong
    can_delete=True    # Bisa hapus halaman jika perlu
)



