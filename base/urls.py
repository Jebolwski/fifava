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
    path("profil-foto/<int:pk>",views.ProfilFotoView,name="profil-foto"),
    path("profil-foto-duzenle/<int:pk>/",views.ProfilFotoDuzenle,name="profil-foto-duzenle"),

    #!FORUMLAR
    path("forumlar/",views.Forumlar,name="forumlar"),
    path("forum/<int:pk>/",views.ForumCevapla,name="forum"),
    path("forum-ekle/",views.ForumEkle,name="forum-ekle"),
    path("forum/<slug:my_slug>/sil/",views.ForumSil,name="forum-sil"),
    path("forum-cevap/<int:pk>/begen/",views.Begenme,name="forum-begen"),
    path("forum-cevap/<int:pk>/begenme/",views.Begenmeme,name="forum-begenme"),
    path("forum/<int:pk>/begen/",views.BegenmeForum,name="forum-begen-1"),
    path("forum/<int:pk>/begenme/",views.BegenmemeForum,name="forum-begenme-1"),
    path("forum-profil/<int:pk>/begen/",views.BegenmeProfilForum,name="forum-begen-2"),
    path("forum-profil/<int:pk>/begenme/",views.BegenmemeProfilForum,name="forum-begenme-2"),
    path("forum-cevap/<int:pk>/sil/",views.ForumCevapSil,name="forum-cevap-sil"),
    path("forum-eklenemez/",views.ForumOlusturulamaz,name="forum-eklenemez"),



    #!AYARLAR
    path("ayarlar/",views.Ayarlar,name="ayarlar"),
    path("bulunamadi/",views.Bulunamadi1,name="404"),



    #!NASIL KATILABİLİRİM
    path("nasil-katilabilirim/",views.NasilKatilabilirim,name="nasil-katilabilirim"),
    

    #!EMAİL DEGİSTİR
    path("email-degistir/",views.EmailDegistir,name="email-degistir"),

    

    #!KAYIT FORMU İŞLEMLERİ
    path("kayit-onay/",views.KayitOnay,name="kayit-onay"),
    path("kayit-onay-form/<int:pk>/",views.KayitOnayForm,name="kayit-onay-form"),
    path("kayit-onay-form-duzenle/<int:pk>/",views.KayitOnayFormDuzenle,name="kayit-onay-form-duzenle"),
    

    #!OYUNCULAR
    path("oyuncular/", views.Kisiler, name="kisiler"),
    path("oyuncu-ekle/", views.KisiEkle, name="kisi-ekle"),
    path("oyuncu-duzenle/<slug:my_slug>/", views.KisiDuzenle, name="kisi-duzenle"),
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
    path("cevaplanmis-duzenle/<int:pk>/", views.CevaplanmisDuzenle, name="cevaplanmis-duzenle"),


     #!İLETİŞİM
    path("gelen-kutusu-cevaplama/<int:iletisim_id>",views.GelenKutusuCevaplama,name="gelen-kutusu-cevaplama"),
    path("cevap/<int:pk>/",views.CevabaCevap,name="cevaba-cevap"),
    
    
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


