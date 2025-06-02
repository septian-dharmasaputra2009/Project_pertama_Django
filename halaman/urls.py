from django.urls import path
from . import views
from halaman import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tambah/', views.tambah_artikel, name='tambah'),
    path('edit/<int:id>/', views.edit_artikel, name='edit'),
    path('hapus/<int:id>/', views.hapus_artikel, name='hapus'),
    path('logout/', views.logout_view, name='logout'),
]
