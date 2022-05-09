from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models import ForumSoruCevap, Iletisim




class ForumYanitSerializer(ModelSerializer):
    
    url = serializers.SerializerMethodField('get_profil_url')
    username = serializers.SerializerMethodField('get_username')
    cevaba_cevap_cevap = serializers.SerializerMethodField('get_cevaba_cevap_cevap')
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
