from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from .forms import FormForm,SorularForm,KayitForm


from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


#?CLASS BASED VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


def KayitOlma(request):
    form = KayitForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('giris-yap')
    context = {'form':form}
    return render(request,"base/kayit.html",context)


def GirisYap(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        person = authenticate(
            request, username=username, password=password)

        if person is not None:
            login(request,person)
            return redirect('anasayfa')
    return render(request,"base/giris.html")
    

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
    sorular=Sorular.objects.all().order_by('-guncellenme_tarihi')
    cevaplananlar=Form.objects.all().filter(kayitli_id=request.user.id).order_by('-guncellenme_tarihi')
    context={"formlar":sorular,"cevap":cevaplananlar}
    return render(request,"base/form/formlar.html",context)



def FormEkle(request):
    form = SorularForm()
    if request.method=="POST":
        form = SorularForm(request.POST)
        print("form valid değil")
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("form valid")
            return redirect("formlar")
    context={"form":form}
    return render(request,"base/form/form-ekle.html",context)


def FormDuzenle(request,pk):
    form_instance = Sorular.objects.get(id=pk)
    form = SorularForm(instance=form_instance)
    if request.method=="POST":
        form = SorularForm(request.POST,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    context={"form":form}
    return render(request,"base/form/form-duzenle.html",context)


def FormSil(request,pk):
    form=Sorular.objects.get(id=pk)
    if request.method=='POST':
        form.delete()
        return redirect("formlar")
    context={'form':form}
    return render(request,"base/form/form-sil.html",context)


def FormCevapla(request,pk):
    form=FormForm()
    sorular=Sorular.objects.get(id=pk)
    if request.method=="POST":
        form_copy=request.POST.copy()
        form_copy['kayitli']=str(request.user.id)
        form=FormForm(form_copy)
        print(form_copy)
        if form.is_valid():
            form.save()
            return redirect('formlar')
        else:
            print("valid degilmis")
    context={'form':form,'sorular':sorular}
    return render(request,"base/form/form-cevapla.html",context)


def FormDetay(request,pk):
    soru=Sorular.objects.get(id=pk)
    context={'soru':soru}
    return render(request,"base/form/form-detay.html",context)



def FormAnaliz(request,pk):
    form = Form.objects.get(id=pk)
    # yuzde = (soru1+soru2+soru3+soru4+soru5+soru6+soru7+soru8+soru9+soru10)/50*100

    context = {'form':form}

    return render(request,"base/form/form-analiz.html",context)