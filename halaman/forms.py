from django import forms
from .models import Artikel
from .models import Buku

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi']

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul', 'penulis', 'deskripsi', 'cover_url', 'gdrive_embed_url', 'gdrive_download_url']

        