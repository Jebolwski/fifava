from django.db import models
from django.contrib.auth.models import User
    

class Kullanici(models.Model):
    oyun_ad_soyad          = models.CharField(max_length=25,blank=False,null=False)
    meslek                 = models.CharField(max_length=25,blank=False,null=False)
    olusturulma_tarihi     = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.oyun_ad_soyad


class Haberler(models.Model):
    baslik                 = models.CharField(max_length=30,null=False,blank=False)
    aciklama               = models.TextField(max_length=250,null=True,blank=True)
    resim                  = models.ImageField(upload_to="haberler",null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.baslik

ANKET_SECIMLERI = (
    ('1','Kesinlikle Katılmıyorum'),
    ('2','Katılmıyorum'),
    ('3','Kararsızım'),
    ('4','Katılıyorum'),
    ('5','Kesinlikle Katılıyorum'),
    )




class Sorular(models.Model):
    baslik                 = models.CharField(max_length=30,null=True,blank=True)
    soru1                  = models.TextField(max_length=50,null=True,blank=True)
    soru2                  = models.TextField(max_length=50,null=True,blank=True)
    soru3                  = models.TextField(max_length=50,null=True,blank=True)
    soru4                  = models.TextField(max_length=50,null=True,blank=True)
    soru5                  = models.TextField(max_length=50,null=True,blank=True)
    soru6                  = models.TextField(max_length=50,null=True,blank=True)
    soru7                  = models.TextField(max_length=50,null=True,blank=True)
    soru8                  = models.TextField(max_length=50,null=True,blank=True)
    soru9                  = models.TextField(max_length=50,null=True,blank=True)
    soru10                 = models.TextField(max_length=50,null=True,blank=True)
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)   


    def __str__(self):
        return self.baslik


        
class Form(models.Model):
    
    sorular                = models.ManyToManyField(Sorular,null=True,blank=True)

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
    olusturulma_tarihi     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi     = models.DateTimeField(auto_now=True,blank=True, null=True)   

    def __str__(self):
        return self.baslik