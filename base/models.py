from urllib import request
from django.db import models
from django.contrib.auth.models import User



class Kullanici(models.Model):
    oyun_ad_soyad          = models.CharField(max_length=40,blank=False,null=False)
    oyun_ad_soyad_slug     = models.SlugField(unique=True,null=False,blank=False)
    meslek                 = models.CharField(max_length=40,blank=False,null=False)
    dosya                  = models.ImageField(upload_to="oyuncu",null=True,blank=True)
    hikaye                 = models.TextField(max_length=10000,blank=False,null=False)
    olusturulma_tarihi     = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    goruldu = models.ManyToManyField(User,related_name='goruldu_oyuncu',default=None,blank=True)

    def __str__(self):
        return str(self.oyun_ad_soyad)


class Haberler(models.Model):
    baslik                 = models.CharField(max_length=100,null=False,blank=False)
    baslik_slug            = models.SlugField(unique=True,null=False,blank=False)
    aciklama               = models.TextField(max_length=5000,null=True,blank=True)
    resim                  = models.ImageField(upload_to="haberler",null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    goruldu = models.ManyToManyField(User,related_name='goruldu_haber',default=None,blank=True)

    def __str__(self):
        return str(self.baslik)



ONAY_DURUM = (
    ('Kabul Et','Kabul Et'),
    ('Bekle','Bekle'),
    ('Reddet','Reddet'),
    ('Yasakla','Yasakla'),
    ('Cevapsız','Cevapsız'),
)



ANKET_SECIMLERI = (
    ('1','Kesinlikle Katılmıyorum'),
    ('2','Katılmıyorum'),
    ('3','Kararsızım'),
    ('4','Katılıyorum'),
    ('5','Kesinlikle Katılıyorum'),
)


class OnayDurum(models.Model):
    kisi                   = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    onaydurum              = models.CharField(max_length=8, choices=ONAY_DURUM,blank=True,null=True) 
    olusturulma_tarihi     = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    
    def __str__(self):
        return str(self.kisi.username)

    def discord_id(self):
        cevaplar = Cevaplar.objects.get(kayitli_id=self.kisi.id, sorular_id=Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu").id)
        return cevaplar.soru15_cevap

    def steam_hex_id(self):
        cevaplar = Cevaplar.objects.get(kayitli_id=self.kisi.id, sorular_id=Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu").id)
        return cevaplar.soru14_cevap



class Sorular(models.Model):
    baslik                 = models.CharField(max_length=60,null=False,blank=False)
    onaydurum              = models.ForeignKey(OnayDurum,on_delete=models.CASCADE,null=True,blank=True)
    
    soru1                  = models.TextField(max_length=200,null=True,blank=True)
    soru2                  = models.TextField(max_length=200,null=True,blank=True)
    soru3                  = models.TextField(max_length=200,null=True,blank=True)
    soru4                  = models.TextField(max_length=200,null=True,blank=True)
    soru5                  = models.TextField(max_length=200,null=True,blank=True)
    soru6                  = models.TextField(max_length=200,null=True,blank=True)
    soru7                  = models.TextField(max_length=200,null=True,blank=True)
    soru8                  = models.TextField(max_length=200,null=True,blank=True)
    soru9                  = models.TextField(max_length=200,null=True,blank=True)
    soru10                 = models.TextField(max_length=200,null=True,blank=True)
    soru11                 = models.TextField(max_length=200,null=True,blank=True)
    soru12                 = models.TextField(max_length=200,null=True,blank=True)
    soru13                 = models.TextField(max_length=200,null=True,blank=True)
    soru14                 = models.TextField(max_length=200,null=True,blank=True)
    soru15                 = models.TextField(max_length=200,null=True,blank=True)
    soru16                 = models.TextField(max_length=200,null=True,blank=True)
    soru17                 = models.TextField(max_length=200,null=True,blank=True)
    soru18                 = models.TextField(max_length=200,null=True,blank=True)
    soru19                 = models.TextField(max_length=200,null=True,blank=True)

    onay1                  = models.CharField(max_length=120,null=True,blank=True)
    onay2                  = models.CharField(max_length=120,null=True,blank=True)
    onay3                  = models.CharField(max_length=120,null=True,blank=True)
    onay4                  = models.CharField(max_length=120,null=True,blank=True)


    goruldu = models.ManyToManyField(User,related_name='goruldu_form',default=None,blank=True)
    
    
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)   


    def __str__(self):
        return str(self.baslik)

    def metinli_soru_sayisi(self):
        sayi = 0
        if self.soru10:
            sayi+=1
        if self.soru11:
            sayi+=1
        if self.soru12:
            sayi+=1
        if self.soru13:
            sayi+=1
        if self.soru14:
            sayi+=1
        if self.soru15:
            sayi+=1
        if self.soru16:
            sayi+=1
        if self.soru17:
            sayi+=1
        if self.soru18:
            sayi+=1
            
        return sayi

    def sikli_soru_sayisi(self):
        sayi = 0
        if self.soru1:
            sayi+=1
        if self.soru2:
            sayi+=1
        if self.soru3:
            sayi+=1
        if self.soru4:
            sayi+=1
        if self.soru5:
            sayi+=1
        if self.soru6:
            sayi+=1
        if self.soru7:
            sayi+=1
        if self.soru8:
            sayi+=1
        if self.soru9:
            sayi+=1
        if self.soru10:
            sayi+=1
        return sayi

    def kullanici_cevap_yuzdesi(self):
        cevap_sayi = Cevaplar.objects.filter(sorular=self).count()
        user_sayi = User.objects.all().count()
        oran = cevap_sayi/user_sayi
        return oran*100



class Cevaplar(models.Model):
    
    baslik                 = models.CharField(max_length=60,null=False,blank=False)
    baslik_slug            = models.SlugField(unique=True,null=True,blank=True)


    sorular                = models.ForeignKey(Sorular,on_delete=models.CASCADE,null=True,blank=True)

    kayitli                = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    soru1_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)  
    soru2_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)
    soru3_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)  
    soru4_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)  
    soru5_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True) 
    soru6_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)  
    soru7_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)   
    soru8_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True) 
    soru9_cevap            = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True)        
    soru10_cevap           = models.CharField(max_length=5, choices=ANKET_SECIMLERI,blank=True,null=True) 
    soru11_cevap           = models.TextField(max_length=200,blank=True,null=True) 
    soru12_cevap           = models.TextField(max_length=10000,blank=True,null=True) 
    soru13_cevap           = models.TextField(max_length=200,blank=True,null=True) 
    soru14_cevap           = models.TextField(max_length=200,blank=True,null=True) 
    soru15_cevap           = models.TextField(max_length=200,blank=True,null=True) 
    soru16_cevap           = models.TextField(max_length=200,blank=True,null=True) 
    soru17_cevap           = models.TextField(max_length=500,blank=True,null=True) 
    soru18_cevap           = models.TextField(max_length=200,blank=True,null=True)
    soru19_cevap           = models.TextField(max_length=2000,blank=True,null=True)

    onay1_cevap            = models.BooleanField(default=False)
    onay2_cevap            = models.BooleanField(default=False)
    onay3_cevap            = models.BooleanField(default=False)
    onay4_cevap            = models.BooleanField(default=False)

    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)   

    def __str__(self):
        return str(self.kayitli)



class Iletisim(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    ad_soyad = models.CharField(max_length=100,null=False,blank=False)
    baslik = models.CharField(max_length=100,null=False,blank=False)
    aciklama = models.TextField(max_length=1000,null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    goruldu = models.ManyToManyField(User,related_name='goruldu_iletisim',default=None,blank=True)

    def __str__(self):
        return str(self.baslik)

        
class Iletisim_cevap(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    iletisim = models.ForeignKey(Iletisim,on_delete=models.CASCADE,null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    cevap = models.TextField(max_length=600)
    goruldu = models.ManyToManyField(User,related_name='goruldu_iletisim_cevap',default=None,blank=True)

    def __str__(self):
        return str(self.user)



class ProfilFoto(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=160,null=True,blank=True)
    username_slug = models.CharField(max_length=160,null=True,blank=True)
    biyografi = models.CharField(max_length=160,null=True,blank=True)
    takipciler = models.ManyToManyField(User,related_name='takipciler',default=None,blank=True)
    takip_edilenler = models.ManyToManyField(User,related_name='takip_edilenler',default=None,blank=True)
    resim = models.ImageField(upload_to="profil_foto",null=False,blank=False,default='profil_foto/default-profile.jpg')
    arka_plan = models.ImageField(upload_to="arka_plan",null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    
    
    def __str__(self):
        return str(self.user)


    def takipci_sayisi(self):
        return self.takipciler.all().count()

    def takip_edilenler_sayisi(self):
        return self.takip_edilenler.all().count()


class ForumSoru(models.Model):
    profil = models.ForeignKey(ProfilFoto,on_delete=models.CASCADE,null=True,blank=True)
    baslik = models.CharField(max_length=100,null=False,blank=False)
    soru = models.TextField(max_length=1000,null=False,blank=False)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    likes = models.ManyToManyField(User,related_name='likes1',default=None,blank=True)
    dislikes = models.ManyToManyField(User,related_name='dislikes1',default=None,blank=True)
    goruldu = models.ManyToManyField(User,related_name='goruldu_soru',default=None,blank=True)
    

    def __str__(self):
        return str(self.baslik)

    def onay_durum(self):
        durum = OnayDurum.objects.get(kisi = self.profil.user)
        return durum

    def puan(self):
        return self.likes.count()-self.dislikes.count()

    def cevap_sayisi(self):
        uzunluk = len(ForumSoruCevap.objects.filter(soru_id=self.id))
        return uzunluk


class ForumSoruCevap(models.Model):
    profil = models.ForeignKey(ProfilFoto,on_delete=models.CASCADE,null=True,blank=True)
    onay_durum = models.ForeignKey(OnayDurum,on_delete=models.CASCADE,null=True,blank=True)
    soru = models.ForeignKey(ForumSoru,on_delete=models.CASCADE,null=True,blank=True)
    cevap = models.CharField(max_length=200,null=False,blank=False)
    cevaba_cevap = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)
    likes = models.ManyToManyField(User,related_name='likes',default=None,blank=True)
    dislikes = models.ManyToManyField(User,related_name='dislikes',default=None,blank=True)
    def __str__(self):
        return str(self.cevap)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Hareket(models.Model):
    hareket = models.TextField(max_length=1000,null=True,blank=True)
    admin_mi = models.TextField(max_length=1,null=False,blank=False,default=0)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)

    
    def __str__(self):
        return self.hareket
  
