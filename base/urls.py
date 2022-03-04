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

    path("profil/<slug:my_slug>/",views.Profil,name="profil"),

    path("ayarlar/",views.Ayarlar,name="ayarlar"),

    path("nasil-katilabilirim/",views.NasilKatilabilirim,name="nasil-katilabilirim"),

    path("kayit-onay/",views.KayitOnay,name="kayit-onay"),
    path("kayit-onay-form/<int:pk>/",views.KayitOnayForm,name="kayit-onay-form"),
    path("kayit-onay-form-duzenle/<int:pk>/",views.KayitOnayFormDuzenle,name="kayit-onay-form-duzenle"),
    path("kayit-kisi-kabul-et/<int:pk>/",views.KayitKabulEt,name="kayit-kabul-et"),
    path("kayit-beklet/<int:pk>/",views.KayitBeklet,name="kayit-beklet"),
    path("kayit-reddet/<int:pk>/",views.KayitReddet,name="kayit-reddet"),

    path("kisiler/", views.Kisiler, name="kisiler"),
    path("kisi-ekle/", views.KisiEkle, name="kisi-ekle"),
    path("kisi/<int:pk>", views.KisiDetay, name="kisi-detay"),
    path("kisi-duzenle/<int:pk>", views.KisiDuzenle, name="kisi-duzenle"),
    path("kisi-sil/<int:pk>", views.KisiSil, name="kisi-sil"),


    path("haberler/", views.Haberlerim, name="haberler"),
    path("haber-ekle/", views.HaberEkle, name="haber-ekle"),
    path("haber/<slug:my_slug>/", views.HaberDetay, name="haber-detay"),
    path("haber-duzenle/<slug:my_slug>/", views.HaberDuzenle, name="haber-duzenle"),
    path("haber-sil/<slug:my_slug>/", views.HaberSil, name="haber-sil"),


    path("formlar/", views.Formlar, name="formlar"),
    path("form-ekle/", views.FormEkle, name="form-ekle"),
    path("form-duzenle/<slug:my_slug>", views.FormDuzenle, name="form-duzenle"),
    path("form-sil/<slug:my_slug>/", views.FormSil, name="form-sil"),
    path("form-cevapla/<slug:my_slug>/", views.FormCevapla, name="form-cevapla"),
    path("form-detay/<slug:my_slug>/", views.FormDetay, name="form-detay"),
    path("form-analiz/<slug:my_slug>/", views.FormAnaliz, name="form-analiz"),
    path("cevap-sil/<int:pk>/", views.CevapSil, name="cevap-sil"),
    path("cevap-detay/<int:pk>/", views.CevapDetay, name="cevap-detay"),
    path("cevaplanmis/", views.Cevaplanmis, name="cevaplanmis"),
    path("cevaplanmis-duzenle/<int:pk>", views.CevaplanmisDuzenle, name="cevaplanmis-duzenle"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = "base.views.Bulunamadi"

