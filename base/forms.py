from dataclasses import field, fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


class OyuncuForm(forms.ModelForm):
    
    class Meta:
        model = Kullanici
        fields = '__all__'
        exclude = ['oyun_ad_soyad_slug','goruldu']

class OnayForm(forms.ModelForm):
    class Meta:
        model = OnayDurum
        fields = '__all__'

class KayitForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control'})

class CevapForm(forms.ModelForm):
    class Meta:
        model = Cevaplar
        fields="__all__"
        exclude=["baslik"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields['soru1_cevap'].widget.attrs.update({'rows':'3','class':'soru1 form-control'})
            self.fields['soru2_cevap'].widget.attrs.update({'rows':'3','class':'soru2 form-control'})
            self.fields['soru3_cevap'].widget.attrs.update({'rows':'3','class':'soru3 form-control'})
            self.fields['soru4_cevap'].widget.attrs.update({'rows':'3','class':'soru4 form-control'})
            self.fields['soru5_cevap'].widget.attrs.update({'rows':'3','class':'soru5 form-control'})
            self.fields['soru6_cevap'].widget.attrs.update({'rows':'3','class':'soru6 form-control'})
            self.fields['soru7_cevap'].widget.attrs.update({'rows':'3','class':'soru7 form-control'})
            self.fields['soru8_cevap'].widget.attrs.update({'rows':'3','class':'soru8 form-control'})
            self.fields['soru9_cevap'].widget.attrs.update({'rows':'3','class':'soru9 form-control'})
            self.fields['soru10_cevap'].widget.attrs.update({'rows':'3','class':'soru10 form-control'})
            self.fields['soru11_cevap'].widget.attrs.update({'rows':'3','class':'soru11 form-control'})
            self.fields['soru12_cevap'].widget.attrs.update({'rows':'3','class':'soru12 form-control'})
            self.fields['soru13_cevap'].widget.attrs.update({'rows':'3','class':'soru13 form-control'})
            self.fields['soru14_cevap'].widget.attrs.update({'rows':'3','class':'soru14 form-control'})
            self.fields['soru15_cevap'].widget.attrs.update({'rows':'3','class':'soru15 form-control'})
            self.fields['soru16_cevap'].widget.attrs.update({'rows':'3','class':'soru16 form-control'})
            self.fields['soru17_cevap'].widget.attrs.update({'rows':'3','class':'soru17 form-control'})
            self.fields['soru18_cevap'].widget.attrs.update({'rows':'3','class':'soru18 form-control'})
            self.fields['soru19_cevap'].widget.attrs.update({'rows':'3','class':'soru19 form-control'})
            self.fields['onay1_cevap'].widget.attrs.update({'class':'input1 form-check-input','checked':False})
            self.fields['onay2_cevap'].widget.attrs.update({'class':'input2 form-check-input','checked':False})
            self.fields['onay3_cevap'].widget.attrs.update({'class':'input3 form-check-input','checked':False})
            self.fields['onay4_cevap'].widget.attrs.update({'class':'input4 form-check-input','checked':False})

class HaberForm(forms.ModelForm):
    baslik=forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    aciklama=forms.CharField(max_length=5000, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    class Meta:
        model=Haberler
        fields="__all__"

class SorularForm(forms.ModelForm):

    class Meta:
        model = Sorular
        fields="__all__"


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control col-4','rows':'3'})


class IletisimForm(forms.ModelForm):
    ad_soyad=forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control col-8'}))
    baslik=forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control col-8'}))
    aciklama=forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control col-8'}))
    
    class Meta:
        model = Iletisim
        fields=['ad_soyad','baslik','aciklama']

class ProfilFotoForm(forms.ModelForm):

    class Meta:
        model = ProfilFoto
        fields = "__all__"
        exclude =["takipciler","takip_edilenler"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        # for fields in self.fields:
        #     self.fields['resim'].widget.attrs.update({'accept':'image/png, image/jpg, image/jpeg'})
        #     self.fields['arka_plan'].widget.attrs.update({'accept':'image/png, image/jpg, image/jpeg'})
    
    


class ForumEkleForm(forms.ModelForm):
    class Meta:
        model = ForumSoru
        fields = "__all__"

