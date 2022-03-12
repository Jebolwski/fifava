from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as authview

urlpatterns = [
    #!ANASAYFA
    path("", views.Ev, name="anasayfa"),


    #!GİRİŞ ÇIKIŞ İŞLEMELERİ
    path("giris-yap/", views.GirisYap, name="giris-yap"),
    path("kayit-ol/",views.KayitOl,name="kayit-ol"),
    path("cikis-yap/", views.CikisYap, name="cikis-yap"),


    #!PROFİL
    path("profil/<slug:my_slug>/",views.Profil,name="profil"),


    #!AYARLAR
    path("ayarlar/",views.Ayarlar,name="ayarlar"),


    #!NASIL KATILABİLİRİM
    path("nasil-katilabilirim/",views.NasilKatilabilirim,name="nasil-katilabilirim"),
    

    #!EMAİL DEGİSTİR
    path("email-degistir/",views.EmailDegistir,name="email-degistir"),


    #!KAYIT FORMU İŞLEMLERİ
    path("kayit-onay/",views.KayitOnay,name="kayit-onay"),
    path("kayit-onay-form/<int:pk>/",views.KayitOnayForm,name="kayit-onay-form"),
    path("kayit-onay-form-duzenle/<int:pk>/",views.KayitOnayFormDuzenle,name="kayit-onay-form-duzenle"),
    path("kayit-kisi-kabul-et/<int:pk>/",views.KayitKabulEt,name="kayit-kabul-et"),
    path("kayit-beklet/<int:pk>/",views.KayitBeklet,name="kayit-beklet"),
    path("kayit-reddet/<int:pk>/",views.KayitReddet,name="kayit-reddet"),
    path("kayit-onbilgi/",views.KayitOnbilgi,name="kayit-onbilgi"),
    

    #!OYUNCULAR
    path("oyuncular/", views.Kisiler, name="kisiler"),
    path("oyuncu-ekle/", views.KisiEkle, name="kisi-ekle"),
    path("oyuncu-duzenle/<slug:my_slug>", views.KisiDuzenle, name="kisi-duzenle"),
    path("oyuncu-sil/<slug:my_slug>", views.KisiSil, name="kisi-sil"),

    #!HABERLER
    path("haberler/", views.Haberlerim, name="haberler"),
    path("haber-ekle/", views.HaberEkle, name="haber-ekle"),
    path("haber/<slug:my_slug>/", views.HaberDetay, name="haber-detay"),
    path("haber-duzenle/<slug:my_slug>/", views.HaberDuzenle, name="haber-duzenle"),
    path("haber-sil/<slug:my_slug>/", views.HaberSil, name="haber-sil"),

    #!FORMLAR
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


    #!ŞİFRE İŞLEMLERİ
    path('sifre-sifirla/', authview.PasswordChangeView.as_view(template_name="base/password/passwordreset.html"),
         name="change_password"),
    
    path('sifre-sifirla-bitti/', authview.PasswordChangeDoneView.as_view(template_name="base/password/passwordresetdone1.html"),
         name="password_change_done"),
    path('sifre-sifirla-gonderildi/',
         authview.PasswordResetDoneView.as_view(template_name="base/password/passwordresetdone.html"), name="password_reset_done"),
    path('sifre-sifirla/<uidb64>/<token>/',
         authview.PasswordResetConfirmView.as_view(template_name="base/password/passwordresetemail.html"), name="password_reset_confirm"),
    path('sifre-sifirlandı/', authview.PasswordResetCompleteView.as_view(template_name='base/password/resetcomplete.html'),
         name="password_reset_complete"),
    path('sifre-unuttum/', authview.PasswordResetView.as_view(template_name="base/password/passwordforgotreset.html"),
         name="password_forgot_reset"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


