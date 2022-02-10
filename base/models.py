from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Kullanici(models.Model):
    oyun_ad_soyad        = models.CharField(max_length=25,blank=False,null=False)
    meslek               = models.CharField(max_length=25,blank=False,null=False)
    olusturulma_tarihi = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True, null=True)
