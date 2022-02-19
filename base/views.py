from re import template
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import CevapForm,SorularForm,KayitForm


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
        else:
            messages.error(request,"Kullanıcı adı veya şifre hatalı...")
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
    cevaplananlar=Cevaplar.objects.all().filter(kayitli_id=request.user.id).order_by('-guncellenme_tarihi')
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
    form=CevapForm()
    sorular=Sorular.objects.get(id=pk)
    if request.method=="POST":
        form_copy=request.POST.copy()
        form_copy['kayitli']=str(request.user.id)
        form_copy['baslik']=sorular.baslik
        form_copy['sorular']=sorular
        form=CevapForm(form_copy)
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
    form = Sorular.objects.get(id=pk)
    cevap = Cevaplar.objects.all().filter(sorular_id=form.id)
    
    sorucount=0
    soru1=NULL
    soru2=NULL
    soru3=NULL
    soru4=NULL
    soru5=NULL
    soru6=NULL
    soru7=NULL
    soru8=NULL
    soru9=NULL
    soru10=NULL


    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    soru1_cevap=0
    soru2_cevap=0
    soru3_cevap=0
    soru4_cevap=0
    soru5_cevap=0
    soru6_cevap=0
    soru7_cevap=0
    soru8_cevap=0
    soru9_cevap=0
    soru10_cevap=0
    for i in cevap:
        
        # print(i.soru6_cevap)
        if i.soru1_cevap!=None:
            soru1_cevap+= int(i.soru1_cevap)
            count1+=1
        else:
            # print("none :D")
            pass


        if i.soru2_cevap!=None:
            soru2_cevap += int(i.soru2_cevap)
            count2+=1
        else:
            # print("none :D")
            pass


        if i.soru3_cevap!=None:
            soru3_cevap += int(i.soru3_cevap)
            count3+=1
        else:
            # print("none :D")
            pass


        if i.soru4_cevap!=None:
            soru4_cevap += int(i.soru4_cevap)
            count4+=1
        else:
            # print("none :D")
            pass

            
        if i.soru5_cevap!=None:
            soru5_cevap += int(i.soru5_cevap)
            count5+=1
        else:
            # print("none :D")
            pass

        
        if i.soru6_cevap!=None:
            soru6_cevap += int(i.soru6_cevap)
            count6+=1
        else:
            # print("none :D")
            pass


        
        if i.soru7_cevap!=None:
            soru7_cevap+= int(i.soru7_cevap)
            count7+=1
        else:
            # print("none :D")
            pass


        if i.soru8_cevap!=None:
            soru8_cevap+= int(i.soru8_cevap)
            count8+=1
        else:
            # print("none :D")
            pass


        if i.soru9_cevap!=None:
            soru9_cevap+= int(i.soru9_cevap)
            count9+=1
        else:
            # print("none :D")
            pass


        if i.soru10_cevap!=None:
            soru10_cevap+= int(i.soru10_cevap)
            count10+=1
        else:
            # print("none :D")
            pass




    if count1!=0:
        soru1=soru1_cevap/count1
    if count2!=0:
        soru2=soru2_cevap/count2
    if count3!=0:
        soru3=soru3_cevap/count3
    if count4!=0:
        soru4=soru4_cevap/count4
    if count5!=0:
        soru5=soru5_cevap/count5
    if count6!=0:
        soru6=soru6_cevap/count6
    if count7!=0:
        soru7=soru7_cevap/count7
    if count8!=0:
        soru8=soru8_cevap/count8
    if count9!=0:    
        soru9=soru9_cevap/count9
    if count10!=0:
        soru10=soru10_cevap/count10


   

    array=[]
    if soru1!=0:
        array.append(soru1*20)
    if soru2!=0:
        array.append(soru2*20)
    if soru3!=0:
        array.append(soru3*20)
    if soru4!=0:
        array.append(soru4*20)
    if soru5!=0:
        array.append(soru5*20)
    if soru6!=0:
        array.append(soru6*20)
    if soru7!=0:
        array.append(soru7*20)
    if soru8!=0:
        array.append(soru8*20)
    if soru9!=0:
        array.append(soru9*20)
    if soru10!=0:
        array.append(soru10*20) 
    

    for i in cevap:
        if i.soru11_cevap:
            soru11_cevap = i.soru12_cevap
            sorucount+=1
        if i.soru13_cevap:
           soru13_cevap = i.soru13_cevap
           sorucount+=1
        if i.soru14_cevap:
            soru14_cevap = i.soru14_cevap
            sorucount+=1
        if i.soru15_cevap:
            soru15_cevap = i.soru15_cevap
            sorucount+=1
        if i.soru16_cevap:
            soru16_cevap = i.soru16_cevap
            sorucount+=1
        if i.soru17_cevap:
            soru17_cevap = i.soru17_cevap
            sorucount+=1
        if i.soru18_cevap:
            soru18_cevap = i.soru18_cevap
            sorucount+=1




    bolmesayac=0
    for i in array:
        if i!=NULL:
            bolmesayac+=1

    top=0
    for i in array:
        if i!=NULL:
            top += i
    
    array=[]
    if soru1!=0:
        array.append(soru1*20)
    if soru2!=0:
        array.append(soru2*20)
    if soru3!=0:
        array.append(soru3*20)
    if soru4!=0:
        array.append(soru4*20)
    if soru5!=0:
        array.append(soru5*20)
    if soru6!=0:
        array.append(soru6*20)
    if soru7!=0:
        array.append(soru7*20)
    if soru8!=0:
        array.append(soru8*20)
    if soru9!=0:
        array.append(soru9*20)
    if soru10!=0:
        array.append(soru10*20) 



    yuzde=top/bolmesayac
    print("Genel katılma yüzdesi :",yuzde,"%","Ankete katılan kişi sayısı :",len(cevap))
    for i in range(0,len(array)):
        if array[i]!=0:
            print("Soru "+str(i+1)+" katılma yüzdesi",array[i],"%")

    for i in cevap:
        print(i.soru10_cevap)

    context = {'form':form,'cevap':cevap,'yuzde':yuzde,'sikli_soru_sayisi':bolmesayac,'dizi':array,'sorusayac':sorucount}

    return render(request,"base/form/form-analiz.html",context)



def CevapDetay(request,pk):
    cevap = Cevaplar.objects.get(id=pk)
    print(cevap.sorular.soru1)
    context = {'cevap':cevap}
    return render(request,"base/form/cevap-detay.html",context)



def CevapSil(request,pk):
    cevap=Cevaplar.objects.filter(id=pk)
    cevap.delete()
    return redirect("formlar")