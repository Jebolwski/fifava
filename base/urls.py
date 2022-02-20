from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.Ev, name="anasayfa"),

    path("kayit-ol/",views.KayitOl,name="kayit-ol"),
    path("giris-yap/", views.GirisYap, name="giris-yap"),
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


    path("formlar/", views.Formlar, name="formlar"),
    path("form-ekle/", views.FormEkle, name="form-ekle"),
    path("form-duzenle/<int:pk>", views.FormDuzenle, name="form-duzenle"),
    path("form-sil/<int:pk>", views.FormSil, name="form-sil"),
    path("form-cevapla/<int:pk>", views.FormCevapla, name="form-cevapla"),
    path("form-detay/<int:pk>", views.FormDetay, name="form-detay"),
    path("form-analiz/<int:pk>", views.FormAnaliz, name="form-analiz"),
    path("cevap-sil/<int:pk>", views.CevapSil, name="cevap-sil"),
    path("cevap-detay/<int:pk>", views.CevapDetay, name="cevap-detay"),
]
