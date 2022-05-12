from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models import ForumSoruCevap, Iletisim




class ForumYanitSerializer(ModelSerializer):
    
    url = serializers.SerializerMethodField('get_profil_url')
    username = serializers.SerializerMethodField('get_username')
    cevaba_cevap_cevap = serializers.SerializerMethodField('get_cevaba_cevap_cevap')
    cevaba_cevap_profil_resim_url = serializers.SerializerMethodField('get_foru_cevaba_cevap_profil_resim_url')
    total_likes = serializers.SerializerMethodField('get_total_likes')
    total_dislikes = serializers.SerializerMethodField('get_total_dislikes')
    cevaba_cevap_username = serializers.SerializerMethodField('get_cevaba_cevap_username')


    class Meta:
        model       = ForumSoruCevap
        fields      = "__all__"

    def get_profil_url(self,forum):
        if forum.profil.resim:
            url = forum.profil.resim.url
            return url
        else:
            return None

    def get_username(self,forum):
        username = forum.profil.user.username
        return username

    def get_cevaba_cevap_cevap(self,forum):
        if forum.cevaba_cevap:
            cevaba_cevap = forum.cevaba_cevap.cevap
            return cevaba_cevap
        else:
            return None

    def get_foru_cevaba_cevap_profil_resim_url(self,forum):
        if forum.cevaba_cevap and forum.cevaba_cevap.profil.resim:
            cevaba_cevap_resim = forum.cevaba_cevap.profil.resim.url
            return cevaba_cevap_resim
        else:
            return None

    def get_total_likes(self,forum):
        total_likes = forum.likes.all().count()
        return total_likes

    def get_total_dislikes(self,forum):
        total_dislikes = forum.dislikes.all().count()
        return total_dislikes

    def get_cevaba_cevap_username(self,forum):
        if forum.cevaba_cevap:
            a = forum.cevaba_cevap.profil.user.username
            return a