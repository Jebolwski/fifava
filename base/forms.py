from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class KayitForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    email = forms.EmailField(min_length=6, max_length=25, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

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
            self.fields[fields].widget.attrs.update({'class':'form-control col-4','rows':'3'})


class SorularForm(forms.ModelForm):

    class Meta:
        model = Sorular
        fields="__all__"


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control col-4','rows':'3'})
