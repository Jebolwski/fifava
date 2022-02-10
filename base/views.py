from msilib.schema import ListView
from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
# Create your views here.

#?CLASS BASED VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def Ev(request):
    return render(request,"base/anasayfa.html")


class Kisiler(ListView):
    model               = Kullanici
    template_name       = 'base/kisiler.html'
    context_object_name = 'kisiler'

class KisiEkle(CreateView):
    model               = Kullanici
    fields              = "__all__"
    template_name       = "base/kisi-ekle.html"
    success_url         = reverse_lazy('kisiler')

class KisiDetay(DetailView):
    model               = Kullanici
    context_object_name = 'kisi'
    template_name       = "base/kisi-detay.html"
    
class KisiDuzenle(UpdateView):
    model               = Kullanici
    
    template_name       = 'base/kisi-duzenle.html'
    context_object_name = 'kisi'
    fields              = '__all__'
    success_url         = reverse_lazy('kisiler')

class KisiSil(DeleteView):
    model               = Kullanici
    template_name       = 'base/kisi-sil.html'
    context_object_name = 'kisi'
    success_url         = reverse_lazy('kisiler')


