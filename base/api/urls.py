from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #!FORUM CEVABI OTOMATİKLEŞTİRME 
    path("forum/cevap/<int:pk>/begen/",views.ForumCevabiniBegen,name="forum_cevabini_begen"),
    path("forum/cevap/<int:pk>/begenme/",views.ForumCevabiniBegenme,name="forum_cevabini_begenme"),
    path("forum/cevap/<int:pk>/begen/renk/",views.ForumCevapBegenRenk,name="forum_cevabini_begen_renk"),
    path("forum/cevap/<int:pk>/begenme/renk/",views.ForumCevapBegenmeRenk,name="forum_cevabini_begenme_renk"),
    path("forum/cevap/<int:pk>/ekle/",views.ForumCevapla,name="forum_cevaplama"),
    path("forum/cevap/gel/",views.ForumCevapGel,name="forum_cevap_gel"),
    path("forum/cevap/<int:pk>/sil/",views.ForumCevapSil,name="forum_cevap_gel"),
    path("forum-sayisi/",views.ForumSayisi,name="forum_sayisi"),
    
    #!FORUM OTOMATİKLEŞTİRME 
    path("forum/<int:pk>/begen/",views.ForumBegen,name="forum__begen"),
    path("forum/<int:pk>/begenme/",views.ForumBegenme,name="forum_begenme"),
    path("forum/<int:pk>/begen/renk/",views.ForumBegenRenk,name="forum_begen_renk"),
    path("forum/<int:pk>/begenme/renk/",views.ForumBegenmeRenk,name="forum_begenme_renk"),

    #!FORUM OTOMATİKLEŞTİRME 
    path("iletisim/ekle/",views.IletisimCevaplama,name="iletisim_cevaplama"),


    path("takip-etme/",views.TakipEtme,name="takip-etme"),
    path("takibi-birak/",views.TakibiBirak,name="takibi-birak"),

    
]
