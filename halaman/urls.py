from django.urls import path
from . import views
from halaman import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tambah/', views.tambah_artikel, name='tambah'),
    path('edit/<int:id>/', views.edit_artikel, name='edit'),
    path('hapus/<int:id>/', views.hapus_artikel, name='hapus'),
    path('tambah_buku/', views.tambah_buku, name='tambah_buku'),
    path('daftar_buku/', views.daftar_buku, name='daftar_buku'),
    path('buku/<int:buku_id>/isi/', views.daftar_isi, name='daftar_isi'),
    path('buku/<int:buku_id>/baca/<int:halaman_awal>/', views.baca_buku, name='baca_buku'),
    path('buku/<int:buku_id>/edit/', views.edit_buku, name='edit_buku'),

]
