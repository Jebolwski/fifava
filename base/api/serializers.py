from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from ..models import ForumSoruCevap, Iletisim




class ForumYanitSerializer(ModelSerializer):
    
    
    class Meta:
        model       = ForumSoruCevap
        fields      = ['id','username','profil','cevaba_cevap','forum','cevap']


