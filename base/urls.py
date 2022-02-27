from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.Ev, name="anasayfa"),

    path("giris-yap/", views.GirisYap, name="giris-yap"),
    path("kayit-ol/",views.KayitOl,name="kayit-ol"),
    path("cikis-yap/", LogoutView.as_view(), name="cikis-yap"),

    path("nasil-katilabilirim/",views.NasilKatilabilirim,name="nasil-katilabilirim"),

    path("kayit-onay/",views.KayitOnay,name="kayit-onay"),
    path("kayit-onay-form/<int:pk>",views.KayitOnayForm,name="kayit-onay-form"),

    path("kisiler/", views.Kisiler.as_view(), name="kisiler"),
    path("kisi-ekle/", views.KisiEkle.as_view(), name="kisi-ekle"),
    path("kisi/<int:pk>", views.KisiDetay.as_view(), name="kisi-detay"),
    path("kisi-duzenle/<int:pk>", views.KisiDuzenle.as_view(), name="kisi-duzenle"),
    path("kisi-sil/<int:pk>", views.KisiSil.as_view(), name="kisi-sil"),


    path("haberler/", views.Haberlerim, name="haberler"),
    path("haber-ekle/", views.HaberEkle, name="haber-ekle"),
    path("haber/<str:pk>/", views.HaberDetay, name="haber-detay"),
    path("haber-duzenle/<str:pk>/", views.HaberDuzenle, name="haber-duzenle"),
    path("haber-sil/<str:pk>/", views.HaberSil, name="haber-sil"),


    path("formlar/", views.Formlar, name="formlar"),
    path("form-ekle/", views.FormEkle, name="form-ekle"),
    path("form-duzenle/<int:pk>", views.FormDuzenle, name="form-duzenle"),
    path("form-sil/<int:pk>", views.FormSil, name="form-sil"),
    path("form-cevapla/<int:pk>", views.FormCevapla, name="form-cevapla"),
    path("form-detay/<int:pk>", views.FormDetay, name="form-detay"),
    path("form-analiz/<int:pk>", views.FormAnaliz, name="form-analiz"),
    path("cevap-sil/<int:pk>", views.CevapSil, name="cevap-sil"),
    path("cevap-detay/<int:pk>", views.CevapDetay, name="cevap-detay"),
    path("cevaplanmis/", views.Cevaplanmis, name="cevaplanmis"),
    path("cevaplanmis-duzenle/<int:pk>", views.CevaplanmisDuzenle, name="cevaplanmis-duzenle"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
