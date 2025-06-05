from django.contrib import admin
from .models import Artikel
from .models import Buku

# Register your models here.
admin.site.register(Buku)
admin.site.register(Artikel)