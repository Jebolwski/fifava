from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class KayitForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']


class CevapForm(forms.ModelForm):
    class Meta:
        model = Cevaplar
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields['soru1_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru2_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru3_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru4_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru5_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru6_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru7_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru8_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru9_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru10_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru11_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru12_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru13_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru14_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru15_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru16_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru17_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['soru18_cevap'].widget.attrs.update({'rows':'3','class':'form-control'})
            self.fields['onay1_cevap'].widget.attrs.update({'rows':'3','class':'form-check-input'})
            self.fields['onay2_cevap'].widget.attrs.update({'rows':'3','class':'form-check-input'})
            self.fields['onay3_cevap'].widget.attrs.update({'rows':'3','class':'form-check-input'})
            self.fields['onay4_cevap'].widget.attrs.update({'rows':'3','class':'form-check-input'})


class SorularForm(forms.ModelForm):

    class Meta:
        model = Sorular
        fields="__all__"


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control col-4','rows':'3'})
