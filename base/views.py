from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .forms import FormForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

#?CLASS BASED VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def Ev(request):
    return render(request,"base/anasayfa.html")

#?KİŞİ CRUD
class Kisiler(ListView):
    model               = Kullanici
    template_name       = 'base/kisi/kisiler.html'
    context_object_name = 'kisiler'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
       
        search_input = self.request.GET.get('arama') or ''
        if search_input:
            context["kisiler"] = context["kisiler"].filter(
                oyun_ad_soyad__contains=search_input)

        context["search_input"] = search_input

        return context

class KisiEkle(LoginRequiredMixin,CreateView):
    model               = Kullanici
    fields              = "__all__"
    template_name       = "base/kisi/kisi-ekle.html"
    success_url         = reverse_lazy('kisiler')

class KisiDetay(DetailView):
    model               = Kullanici
    context_object_name = 'kisi'
    template_name       = "base/kisi/kisi-detay.html"
    
class KisiDuzenle(LoginRequiredMixin,UpdateView):
    model               = Kullanici
    template_name       = 'base/kisi/kisi-duzenle.html'
    context_object_name = 'kisi'
    fields              = '__all__'
    success_url         = reverse_lazy('kisiler')

class KisiSil(LoginRequiredMixin,DeleteView):
    model               = Kullanici
    template_name       = 'base/kisi/kisi-sil.html'
    context_object_name = 'kisi'
    success_url         = reverse_lazy('kisiler')



#?HABER CRUD
class Haberler(ListView):
    model               = Haberler
    template_name       = 'base/haber/haberler.html'
    context_object_name = 'haberler'




class HaberEkle(LoginRequiredMixin,CreateView):
    model               = Haberler
    fields              = "__all__"
    template_name       = "base/haber/haber-ekle.html"
    success_url         = reverse_lazy('haberler')

class HaberDetay(DetailView):
    model               = Haberler
    context_object_name = 'haber'
    template_name       = "base/haber/haber-detay.html"
    
class HaberDuzenle(LoginRequiredMixin,UpdateView):
    model               = Haberler
    template_name       = 'base/haber/haber-duzenle.html'
    context_object_name = 'haber'
    fields              = '__all__'
    success_url         = reverse_lazy('haberler')

class HaberSil(LoginRequiredMixin,DeleteView):
    model               = Haberler
    template_name       = "base/haber/haber-sil.html"
    context_object_name = "haber"
    success_url         = reverse_lazy("haberler")


#!FORM
def Formlar(request):
    formlar=Form.objects.all()
    context={"formlar":formlar}
    return render(request,"base/form/formlar.html",context)



def FormEkle(request):
    form = FormForm()
    if request.method=="POST":
        form = FormForm(request.POST)
        print("form valid değil")
        if form.is_valid():
            form.save()
            print("form valid")
            return redirect("formlar")
    context={"form":form}
    return render(request,"base/form/form-ekle.html",context)


def FormDuzenle(request,pk):
    form_instance = Form.objects.get(id=pk)
    form = FormForm(instance=form_instance)
    if request.method=="POST":
        form = FormForm(request.POST,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    context={"form":form}
    return render(request,"base/form/form-duzenle.html",context)


def FormSil(request,pk):
    form=Form.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect("formlar")
    context={'form':form}
    return render(request,"base/form/form-sil.html",context)


def FormCevapla(request,pk):
    form=Form.objects.get(id=pk)
    if request.method=="POST":
        if request.POST:
            print("var")
        return redirect("formlar")
    context={'form':form}
    return render(request,"base/form/form-cevapla.html",context)

