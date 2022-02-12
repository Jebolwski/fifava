from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from filelock import BaseFileLock
# Create your models here.


class Kullanici(models.Model):
    oyun_ad_soyad        = models.CharField(max_length=25,blank=False,null=False)
    meslek               = models.CharField(max_length=25,blank=False,null=False)
    olusturulma_tarihi = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.oyun_ad_soyad


class Haberler(models.Model):
    baslik              = models.CharField(max_length=30,null=False,blank=False)
    aciklama           = models.TextField(max_length=250,null=True,blank=True)
    resim              = models.ImageField(upload_to="haberler",null=True,blank=True)
    olusturulma_tarihi = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.baslik