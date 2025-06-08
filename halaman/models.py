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
    cover_url = models.URLField(help_text="Link gambar cover")
    deskripsi = models.TextField()
    pdf_url = models.URLField(blank=True, null=True, help_text="Opsional: Link PDF untuk diunduh")

    def __str__(self):
        return self.judul

class Halaman(models.Model):
    buku = models.ForeignKey(Buku, related_name='halaman', on_delete=models.CASCADE)
    nomor = models.PositiveIntegerField()
    gambar_url = models.URLField(help_text="Link gambar halaman")
    pdf_url = models.URLField(blank=True, null=True, help_text="Opsional: Link PDF untuk diunduh")

    class Meta:
        ordering = ['nomor']  # agar urut sesuai nomor halaman

    def __str__(self):
        return f"{self.buku.judul} - Halaman {self.nomor}"