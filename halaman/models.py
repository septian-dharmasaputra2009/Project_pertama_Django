from django.db import models

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul