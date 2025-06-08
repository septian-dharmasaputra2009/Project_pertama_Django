from django.contrib import admin
from .models import Artikel, Buku, Halaman

# Register your models here.
admin.site.register(Artikel)

class HalamanInline(admin.TabularInline):
    model = Halaman
    extra = 1

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis')
    inlines = [HalamanInline]

admin.site.register(Halaman)