from re import template
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.Ev, name="anasayfa"),
    path("giris-yap/", LoginView.as_view(template_name="base/giris.html"), name="giris-yap"),
    path("cikis-yap/", LogoutView.as_view(), name="cikis-yap"),
    path("kisiler/", views.Kisiler.as_view(), name="kisiler"),
    path("kisi-ekle/", views.KisiEkle.as_view(), name="kisi-ekle"),
    path("kisi/<int:pk>", views.KisiDetay.as_view(), name="kisi-detay"),
    path("kisi-duzenle/<int:pk>", views.KisiDuzenle.as_view(), name="kisi-duzenle"),
    path("kisi-sil/<int:pk>", views.KisiSil.as_view(), name="kisi-sil"),
    path("haberler/", views.Haberler.as_view(), name="haberler"),
    path("haber-ekle/", views.HaberEkle.as_view(), name="haber-ekle"),
    path("haber/<int:pk>", views.HaberDetay.as_view(), name="haber-detay"),
    path("haber-duzenle/<int:pk>", views.HaberDuzenle.as_view(), name="haber-duzenle"),
    path("haber-sil/<int:pk>", views.HaberSil.as_view(), name="haber-sil"),
]
