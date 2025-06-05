from django.db import models

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

#daftar buku online
class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    deskripsi = models.TextField()
    cover_url = models.URLField(blank=True)
    gdrive_embed_url = models.URLField(help_text="URL dari Google Drive")
    gdrive_download_url = models.URLField(help_text="Link langsung untuk download PDF")

    def __str__(self):
        return self.judul