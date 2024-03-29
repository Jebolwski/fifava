from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Kullanici)
class Person(admin.ModelAdmin):
    list_display = ('oyun_ad_soyad', 'meslek', 'olusturulma_tarihi')
    list_filter = ('oyun_ad_soyad', 'meslek',)
    search_fields = ('oyun_ad_soyad', 'meslek')


admin.site.register(ForumSoru)
admin.site.register(ForumSoruCevap)
admin.site.register(Iletisim_cevap)
admin.site.register(ProfilFoto)
admin.site.register(Iletisim)
admin.site.register(Haberler)
admin.site.register(Cevaplar)
admin.site.register(Sorular)
admin.site.register(OnayDurum)
admin.site.register(Hareket)