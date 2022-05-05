from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #!FORUM CEVABI OTOMATİKLEŞTİRME 
    path("forum/cevap/<int:pk>/begen/",views.ForumCevabiniBegenme,name="forum_cevabini_begen"),
    path("forum/cevap/<int:pk>/begenme/",views.ForumCevabiniBegenmeme,name="forum_cevabini_begenme"),
    path("forum/cevap/<int:pk>/begen/sayisi/",views.ForumCevapBegenmeSayi,name="forum_cevabini_begen_sayi"),
    path("forum/cevap/<int:pk>/begenme/sayisi/",views.ForumCevapBegenmemeSayi,name="forum_cevabini_begenme_sayi"),
    path("forum/cevap/<int:pk>/begen/renk/",views.ForumCevapBegenRenk,name="forum_cevabini_begen_renk"),
    path("forum/cevap/<int:pk>/begenme/renk/",views.ForumCevapBegenmeRenk,name="forum_cevabini_begenme_renk"),
    
    #!FORUM OTOMATİKLEŞTİRME 
    path("forum/<int:pk>/begen/",views.ForumBegenme,name="forum__begen"),
    path("forum/<int:pk>/begenme/",views.ForumBegenmeme,name="forum_begenme"),
    path("forum/<int:pk>/begen/sayisi/",views.ForumBegenmeSayi,name="forum_begen_sayi"),
    path("forum/<int:pk>/begenme/sayisi/",views.ForumBegenmemeSayi,name="forum_begenme_sayi"),
    path("forum/<int:pk>/begen/renk/",views.ForumBegenRenk,name="forum_begen_renk"),
    path("forum/<int:pk>/begenme/renk/",views.ForumBegenmeRenk,name="forum_begenme_renk"),
    
    #!FORUM OTOMATİKLEŞTİRME 
    path("iletisim/ekle/",views.IletisimCevaplama,name="iletisim_cevaplama"),
    
]
