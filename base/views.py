import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .forms import CevapForm, OnayForm, OyuncuForm, ProfilFotoForm,SorularForm,KayitForm,HaberForm,IletisimForm,ForumEkleForm

from django.core.paginator import Paginator
import locale

from .models import *

from django.contrib import messages





locale.setlocale(locale.LC_TIME, 'tr')


def Bulunamadi(request,exception):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/hata_bulunamadi/404.html',context)




def Hata(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/hata_bulunamadi/500.html',context)

    
def Bulunamadi1(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/hata_bulunamadi/404.html',context)


def Hata1(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/hata_bulunamadi/500.html',context)


def GirisYap(request):
    if request.user.is_authenticated and OnayDurum.objects.get(kisi_id=request.user.id).onaydurum!="Yasakla":
            return redirect('anasayfa')

    if request.method == 'POST':
        username1 = request.POST.get('username')
        if len(User.objects.filter(username=username1))>0:
            username1 = request.POST.get('username')
        else:
            if( len(User.objects.all().filter(email=username1)) > 0):
                username1 = User.objects.get(email=username1).username
        password = request.POST.get('password')
        

        person = authenticate(
            request,username=username1, password=password)

        if person is not None:
            if OnayDurum.objects.get(kisi_id=person.id).onaydurum=="Yasakla":
                messages.success(request,'<div class="btn btn-danger message p-2 rounded-3">Bu hesap yasaklandı.</div>')
                return redirect("giris-yap")
            Hareket.objects.create(
                hareket = username1+" adlı kullanıcı giriş yaptı.",
                admin_mi = 1,
            )
            login(request, person)
            messages.success(request, '<div class="btn btn-success message p-2 rounded-3">Başarıyla giriş yapıldı.</div>')
            return redirect('anasayfa')
        else:
            messages.error(request,'<div class="btn btn-danger message p-2 rounded-3">Kullanıcı adı, email veya şifre hatalı.</div>')
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request, 'base/giris.html',context)



def CikisYap(request):
    Hareket.objects.create(
                hareket = request.user.username+" adlı kullanıcı çıkış yaptı.",
                admin_mi = 1,
            )
    logout(request)
    messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Başarıyla çıkış yapıldı.</div>')
    return redirect("anasayfa")


def KayitOl(request):

    if request.user.is_authenticated:
        return redirect("anasayfa")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = KayitForm()
    if request.method == 'POST': 
        dizi=[]
        for i in User.objects.all():
            dizi.append(i.email)
        if request.POST['email'] in dizi:
            messages.error(request, '<div class="btn btn-info message p-2 rounded-3">Girdiğiniz email kullanımda.</div>')
            return redirect('kayit-ol')

    if request.method == 'POST': 
        dizi1=[]
        for i in User.objects.all():
            dizi1.append(i.username.lower())
        if request.POST['username'].lower() in dizi1:
            messages.error(request, '<div class="btn btn-danger message p-2 rounded-3">Girdiğiniz kullanıcı adı kullanımda.</div>')
            return redirect('kayit-ol')
        
        
        form = KayitForm(request.POST)
        if form.is_valid():
            form.save()
            Hareket.objects.create(
                hareket = request.POST['username'] +" adlı kullanıcı aramıza katıldı.",
                admin_mi=0,
            )
            messages.success(request, '<div class="btn btn-success message p-2 rounded-3">Başarıyla kayıt olundu.</div>')
            ProfilFoto.objects.update_or_create(
                user=User.objects.get(username = request.POST['username']),
                username=request.POST['username'],
                username_slug=slugify(request.POST['username']),
                biyografi=None,
                resim=None,
                arka_plan=None)
            OnayDurum.objects.update_or_create(kisi = User.objects.get(username = request.POST['username']),onaydurum = "Cevapsız")
            return redirect('giris-yap')
        else:
            messages.error(request, '<div class="btn btn-danger message p-2 rounded-3">Kayıt başarı ile gerçekleştirilemedi.</div>')

    context = {
        'form': form,'haberler':haberler
    }
    return render(request, 'base/kayit.html', context)


def Ev(request):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = IletisimForm()
    cevaplar = Iletisim.objects.all().order_by('-guncellenme_tarihi')
    cevaplara_cevap = Iletisim_cevap.objects.all().filter(user_id = request.user.id)

    gonderdikleriniz=None

    if request.user.is_superuser:
        gonderdikleriniz = Iletisim_cevap.objects.all().filter(user_id=request.user.id)
    else:
        gonderdikleriniz = Iletisim.objects.all().filter(user_id=request.user.id)
    if request.method=='POST':
        form = IletisimForm(request.POST)
        if request.user.is_authenticated:    
            form.instance.user = request.user
        if request.FILES:
            form.instance.dosya = request.FILES.get('file')
        

        if form.is_valid():
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Bilgiler başarıyla kaydedildi.</div>')
            return redirect("anasayfa")
        else:
            messages.error(request,'<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    
    
    context={'haberler':haberler,'form':form,'cevaplar':cevaplar,
            'cevaplara_cevap':cevaplara_cevap,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim
            ,'gonderdikleriniz':gonderdikleriniz}
    return render(request,"base/anasayfa.html",context)


def CevabaCevap(request,pk):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    cevaplara_cevap = Iletisim_cevap.objects.all().get(id = pk) 
    if request.user.is_authenticated:
        cevaplara_cevap.goruldu.add(request.user.id)
    soru = Iletisim.objects.get(id=cevaplara_cevap.iletisim_id)
    context={'haberler':haberler,'c':cevaplara_cevap,'soru':soru}
    return render(request,"base/cevaba-cevap.html",context)


def NasilKatilabilirim(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    context={'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/bilgiler/nasil-katilabilirim.html",context)


def Bilgiler(request):
    return render(request,"base/hata_bulunamadi/404.html")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    context={'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/bilgiler/bilgiler.html",context)

def Terimler(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    context={'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/bilgiler/terimler.html",context)



#?KİŞİ CRUD
def Kisiler(request):
    kisiler = Kullanici.objects.all().order_by('-meslek')
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    
    ad_soyad_dizi=[]
    for i in kisiler:
        ad_soyad_dizi.append([i.oyun_ad_soyad])


    if request.user.is_authenticated:
        for i in Kullanici.objects.all().order_by('-guncellenme_tarihi'):
            if request.user.is_authenticated and request.user not in i.goruldu.all():
                i.goruldu.add(request.user.id)
                
    
    

    if request.method=="POST":
        arama = request.POST['arama']
        kisiler = Kullanici.objects.all().filter(oyun_ad_soyad__contains=arama).order_by('-meslek')

    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    context = {'kisiler':kisiler,'ad_soyad':ad_soyad_dizi,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/kisi/kisiler.html",context)


@login_required(login_url='giris-yap')
def EmailDegistir(request):
    if request.method == 'POST':
        eski_email = request.POST['eski-email']
        yeni_email1 = request.POST['yeni-email1']
        yeni_email2 = request.POST['yeni-email2']

        if eski_email==request.user.email and yeni_email1==yeni_email2 and eski_email!=yeni_email1:
            request.user.email = yeni_email1
            request.user.save()
            messages.success(request, '<div class="btn btn-success message p-2 rounded-3">Emailiniz başarıyla değiştirildi.</div>')
            return redirect('ayarlar')
        elif yeni_email1!=yeni_email2:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Yeni emailler uyuşmuyor.</div>')
        elif eski_email!=request.user.email:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Eski emailinizi yanlış girdiniz.</div>')
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')

    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
            
    context={'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/ayarlar/email-degistir.html",context)


@login_required(login_url='giris-yap')
def KisiEkle(request):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break


    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = OyuncuForm()
    if request.method == 'POST':
        data = request.POST.copy()
        data['oyun_ad_soyad_slug'] = slugify(request.POST['oyun_ad_soyad'])
        if request.FILES:
            size = request.FILES.get("dosya").size/(1024*1024)
            if size>2:
                messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Girdiğiniz fotoğraf 2 mb`dan küçük olmalı ('+str(round(size,2))+' mb)</div>')
                return redirect('kisi-ekle')
        form = OyuncuForm(data,files=request.FILES)
        if form.is_valid():
            form.save()
            Hareket.objects.create(
                hareket = request.POST['oyun_ad_soyad'] +" adlı oyuncu "+ request.user.username +" tarafından eklendi.",
                admin_mi=0,
            )
            messages.success(request, '<div class="btn btn-success message p-2 rounded-3">Oyuncu başarıyla oluşturuldu.</div>')
            return redirect('kisiler')
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')

    
    context = {'form':form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/kisi/kisi-ekle.html",context)


@login_required(login_url='giris-yap')
def KisiDuzenle(request,pk):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    instance = Kullanici.objects.get(id=pk)
    form = OyuncuForm(instance=instance)
    if request.method == 'POST':
        data = request.POST.copy()
        data['oyun_ad_soyad_slug'] = slugify(request.POST['oyun_ad_soyad'])
        if request.FILES:
            size = request.FILES.get("dosya").size/(1024*1024)
            if size>2:
                messages.error(request,'<div class="bg-success message p-2 rounded-3">Girdiğiniz fotoğraf 2 mb`dan küçük olmalı ('+str(round(size,2))+' mb).</div>')
                return redirect('kisi-duzenle',pk)
        form = OyuncuForm(instance=instance,data = data,files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.oyun_ad_soyad_slug = slugify(request.POST.get('oyun_ad_soyad_slug'))
            obj.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Oyuncu başarıyla düzenlendi.</div>')
            return redirect("kisiler")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    
    
    context = {'form':form , 'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/kisi/kisi-duzenle.html",context)


@login_required(login_url='giris-yap')
def KisiSil(request,pk):
    if not request.user.is_superuser:
        return redirect("404")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    instance = Kullanici.objects.get(id=pk)
    if request.method == 'POST':
        instance.delete()
        Hareket.objects.create(
            hareket=instance.oyun_ad_soyad+" isimli oyuncu silindi.",
            admin_mi=0,
        )
        messages.success(request,'<div class="btn btn-danger message p-2 rounded-3">Oyuncu başarıyla silindi.</div>')
        return redirect('kisiler')

    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    context = {"haberler":haberler,'kisi':instance,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/kisi/kisi-sil.html",context)


def KisiDetay(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    kisi = Kullanici.objects.get(id=pk)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if request.user.is_authenticated:
        kisi.goruldu.add(request.user.id)
    context = {'kisi':kisi,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/kisi/kisi-detay.html",context)


#?HABER CRUD
def Haberlerim(request):
    
    haberler2 = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')
    p = Paginator(haberler,10)
    page = request.GET.get('page')
    haber = p.get_page(page)


    if request.user.is_authenticated:
        for i in Haberler.objects.all().order_by('-guncellenme_tarihi'):
            if request.user.is_authenticated and request.user not in i.goruldu.all():
                i.goruldu.add(request.user.id)
    
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber1 in haberler1:
            if request.user not in haber1.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    
    

    context = {'haberler':haber,'haberler1':haberler1,'haberler2':haberler2,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/haber/haberler.html",context)


@login_required(login_url='giris-yap')
def HaberEkle(request):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler2 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler2:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    form = HaberForm()
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    
    if request.method=='POST':
        if request.FILES:
            size = request.FILES.get("file").size/(1024*1024)
            if size>2:
                messages.error(request,'<div class="btn btn-danger message p-2 rounded-3">Girdiğiniz fotoğraf 2 mb`dan küçük olmalı ('+str(round(size,2))+' mb)</div>')
                return redirect('haber-ekle')
        Haberler.objects.create(
        baslik=request.POST['baslik'],
        aciklama=request.POST['aciklama'],
        resim=request.FILES.get('file'),
        baslik_slug = slugify(request.POST['baslik']),
        )
        Hareket.objects.create(
                hareket = request.POST['baslik'] +" başlıklı haber haberlere eklendi.",
                admin_mi=0,
            )
        messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Haber başarıyla oluşturuldu.</div>')
        return redirect('haberler')
        context = {'form':form,'haberler':haberler}
    
    
    
    context = {'form':form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/haber/haber-ekle.html",context)
            

def HaberDetay(request,my_slug):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler2 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler2:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    haber = Haberler.objects.get(baslik_slug=my_slug)
    if request.user.is_authenticated:
        haber.goruldu.add(request.user.id)
    
    context = {'haber':haber,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/haber/haber-detay.html",context)


@login_required(login_url='giris-yap')
def HaberDuzenle(request,my_slug):
    if not request.user.is_superuser:
        return redirect("404")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    instance = Haberler.objects.get(baslik_slug=my_slug)
    if request.method == 'POST':
            if request.FILES:
                size = request.FILES.get("file").size/(1024*1024)
                if size>2:
                    messages.error(request,'<div class="btn btn-danger message p-2 rounded-3">Girdiğiniz fotoğraf 2 mb`dan küçük olmalı ('+str(round(size,2))+' mb)</div>')
                    return redirect('haber-duzenle',my_slug)
            instance.baslik=request.POST['baslik']
            instance.aciklama=request.POST['aciklama']
            instance.baslik_slug = slugify(request.POST['baslik'])
            temizle=request.POST.get('temizle')
            if temizle=='on':
                instance.resim.delete()
            if request.FILES:
                instance.resim=request.FILES['file']
            instance.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Haber başarıyla düzenlendi.</div>')
            return redirect("haberler")
    
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler2 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break
        for haber in haberler2:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    

    context = {'instance':instance,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/haber/haber-duzenle.html",context)


@login_required(login_url='giris-yap')
def HaberSil(request,my_slug):
    if not request.user.is_superuser:
        return redirect("404")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    haber1 = Haberler.objects.get(baslik_slug=my_slug)
    if request.method=="POST":
        haber1.delete()
        Hareket.objects.create(
            hareket=haber1.baslik+" başlıklı haber silindi.",
            admin_mi=0,
        )
        messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Haber başarıyla silindi.</div>')
        return redirect('haberler')

    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    
    context={'haber':haber1,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/haber/haber-sil.html",context)


#!FORM
#!------------------------------
def Formlar(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    sorular=Sorular.objects.all().order_by('-guncellenme_tarihi')
    cevaplananlar=Cevaplar.objects.all().filter(kayitli_id=request.user.id).order_by('-guncellenme_tarihi')
    p = Paginator(sorular,10)
    page = request.GET.get('page')
    soru = p.get_page(page)

    if request.user.is_authenticated:
        for i in Sorular.objects.all().order_by('-guncellenme_tarihi'):
            if request.user.is_authenticated and request.user not in i.goruldu.all():
                i.goruldu.add(request.user.id)
    
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    
    context={"formlar":soru,"cevap":cevaplananlar,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/form/formlar.html",context)


@login_required(login_url='giris-yap')
def FormEkle(request):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = SorularForm()

    


    if request.method=="POST":
        
        data = request.POST.copy()
        form = SorularForm(data)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Form başarıyla oluşturuldu.</div>')
            Hareket.objects.create(
                hareket = request.POST['baslik'] +" başlıklı form formlara eklendi.",
                admin_mi=0,
            )
            return redirect("formlar")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    context={"form":form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/form/form-ekle.html",context)


@login_required(login_url='giris-yap')
def FormDuzenle(request,pk):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form_instance = Sorular.objects.get(id=pk)
    form = SorularForm(instance=form_instance)
    if request.user.is_authenticated:
        form_instance.goruldu.add(request.user.id)
    if request.method=="POST":
        data = request.POST.copy()
        form = SorularForm(data,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    
    context={"form":form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/form-duzenle.html",context)


@login_required(login_url='giris-yap')
def FormSil(request,pk):
    if not request.user.is_superuser:
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form=Sorular.objects.get(id=pk)
    if request.method=='POST':
        form.delete()
        Hareket.objects.create(
            hareket=form.baslik+" başlıklı form silindi.",
            admin_mi=0,
        )
        messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Form başarıyla silindi.</div>')
        return redirect("formlar")

    
    context={'form':form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/form-sil.html",context)


@login_required(login_url='giris-yap')
def FormCevapla(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    form = CevapForm()
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    sorular = Sorular.objects.get(id = pk)
    benim_cevaplarim = Cevaplar.objects.filter(kayitli_id=request.user.id,sorular_id=sorular.id)
    if len(Cevaplar.objects.filter(kayitli_id=request.user.id,sorular_id=sorular.id))>0 :
        return redirect('cevaplanmis')
    if request.method=="POST":
        form_copy=request.POST.copy()
        form_copy['kayitli']=str(request.user.id)
        form_copy['baslik']=sorular.baslik
        form_copy['baslik_slugify']=slugify(sorular.baslik)
        form_copy['sorular']=sorular
        form=CevapForm(form_copy)
        

        if form.is_valid():
            form.save()
            if sorular.baslik == "FIFAVOX RolePlay Kayıt Formu":
                onaydurum = OnayDurum.objects.get(kisi_id = request.user.id)
                onaydurum.onaydurum = "Bekle"
                onaydurum.save()
                Hareket.objects.create(hareket=request.user.username+" adlı kullanıcı FIFAVOX RolePlay Kayıt Formunu cevapladı.",admin_mi=1)
            else:
                Hareket.objects.create(hareket=request.user.username+" adlı kullanıcı " + form_copy['baslik']+" başlıklı formu cevapladı.",admin_mi=1)

            messages.success(request, '<div class="btn btn-success message p-2 rounded-3">Cevaplarınız başarıyla kaydedildi.</div>')
            return redirect('formlar')


        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    context={'form':form,'sorular':sorular,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/form-cevapla.html",context)


def FormDetay(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    soru=Sorular.objects.get(id = pk)
    if request.user.is_authenticated:
        soru.goruldu.add(request.user.id)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'soru':soru,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context={'soru':soru,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/form/form-detay.html",context)


@login_required(login_url='giris-yap')
def FormAnaliz(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = Sorular.objects.get(id = pk)
    cevap = Cevaplar.objects.all().filter(sorular_id=form.id)
    if request.user.is_authenticated:
        form.goruldu.add(request.user.id)
    if True:
        sorucount=0
        soru1=0
        soru2=0
        soru3=0
        soru4=0
        soru5=0
        soru6=0
        soru7=0
        soru8=0
        soru9=0
        soru10=0


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

            if i.soru1_cevap!=None:
                soru1_cevap+= int(i.soru1_cevap)
                count1+=1


            if i.soru2_cevap!=None:
                soru2_cevap += int(i.soru2_cevap)
                count2+=1



            if i.soru3_cevap!=None:
                soru3_cevap += int(i.soru3_cevap)
                count3+=1



            if i.soru4_cevap!=None:
                soru4_cevap += int(i.soru4_cevap)
                count4+=1



            if i.soru5_cevap!=None:
                soru5_cevap += int(i.soru5_cevap)
                count5+=1



            if i.soru6_cevap!=None:
                soru6_cevap += int(i.soru6_cevap)
                count6+=1




            if i.soru7_cevap!=None:
                soru7_cevap+= int(i.soru7_cevap)
                count7+=1



            if i.soru8_cevap!=None:
                soru8_cevap+= int(i.soru8_cevap)
                count8+=1



            if i.soru9_cevap!=None:
                soru9_cevap+= int(i.soru9_cevap)
                count9+=1



            if i.soru10_cevap!=None:
                soru10_cevap+= int(i.soru10_cevap)
                count10+=1





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




        bolmesayac=1
        for i in array:
            if i!=None:
                bolmesayac+=1

        top=0
        for i in array:
            if i!=None:
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
    # if len(Cevaplar.objects.all())>1:
    #     bolmesayac=bolmesayac-1
      

    yuzde=top/bolmesayac
    cevaplar = Cevaplar.objects.all().order_by('-guncellenme_tarihi')
    p = Paginator(Cevaplar.objects.all().filter(sorular_id=form.id),1)
    page = request.GET.get('page')
    cevaplar_hepsi = p.get_page(page)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {
        'form':form,'cevap':cevap,'yuzde':yuzde,'sikli_soru_sayisi':bolmesayac,
    'dizi':array,'sorusayac':sorucount,'cevaplar':cevaplar_hepsi,'cevaplarim':cevaplar,'haberler':haberler,'durum':durum,
    'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {
        'form':form,'cevap':cevap,'yuzde':yuzde,'sikli_soru_sayisi':bolmesayac,
    'dizi':array,'sorusayac':sorucount,'cevaplar':cevaplar_hepsi,'cevaplarim':cevaplar,'haberler':haberler,
    'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/form-analiz.html",context)


@login_required(login_url='giris-yap')
def Cevaplanmis(request):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/cevaplanmis.html",context)
#!------------------------------

@login_required(login_url='giris-yap')
def CevaplanmisDuzenle(request,pk):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form_instance = Cevaplar.objects.get(id=pk)
    form = CevapForm(instance=form_instance)
    sorular = Sorular.objects.filter(id=form_instance.sorular_id)
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    if request.method=='POST':
        data = request.POST.copy()
        data['baslik']=form_instance.baslik
        form = CevapForm(data,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'form':form,'sorular':sorular,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context={'form':form,'sorular':sorular,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}


    return render(request,"base/form/cevaplanmis-duzenle.html",context)

@login_required(login_url='giris-yap')
def CevapDetay(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    cevap = Cevaplar.objects.get(id=pk)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'cevap':cevap,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {'cevap':cevap,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/form/cevap-detay.html",context)

@login_required(login_url='giris-yap')
def CevapSil(request,pk):
    cevap=Cevaplar.objects.filter(id=pk)
    cevap.delete()
    return redirect("formlar")

@login_required(login_url='giris-yap')
def KayitOnay(request):
    if not request.user.is_superuser:
        return redirect("404")
    
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    onay = OnayDurum.objects.all().order_by("onaydurum")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haberler,'onay':onay,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {'haberler':haberler,'onay':onay,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/kayitonay/kayit-onay.html",context)

@login_required(login_url='giris-yap')
def KayitOnayFormDuzenle(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    kisi = User.objects.get(id=pk)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    sorular = Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu")
    instance = OnayDurum.objects.get(kisi_id=kisi.id)
    form = OnayForm(instance=instance)
    if request.method=="POST":
        data = request.POST.copy()
        data['kisi'] = str(kisi.id)
        form = OnayForm(instance=instance,data=data)
        if form.is_valid():
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Onay durumu güncellendi.</div>')
            return redirect("kayit-onay")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
 
    
    if Cevaplar.objects.all().filter(kayitli_id=kisi.id,sorular_id=sorular.id):
        
        cevaplar = Cevaplar.objects.get(sorular_id=sorular.id,kayitli_id=kisi.id)
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)  
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'haberler':haberler,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim} 
        else:
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'haberler':haberler,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim} 

    else:
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)  
            context = {'sorular':sorular,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  
        else:
            context = {'sorular':sorular,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  
    return render(request,"base/kayitonay/kayit-onay-form.html",context)

@login_required(login_url='giris-yap')
def KayitOnayForm(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    kisi = User.objects.get(id=pk)
    sorular = Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if len(OnayDurum.objects.all().filter(kisi_id=kisi.id))>0:
        return redirect('kayit-onay-form-duzenle',kisi.id)
    form = OnayForm()
    if request.method=="POST":
        data = request.POST.copy()
        data['kisi'] = str(kisi.id)
        form = OnayForm(data)
        if form.is_valid():
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Onay durumu kaydedildi.</div>')
            return redirect("kayit-onay")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    
    
    if Cevaplar.objects.all().filter(sorular_id=sorular.id):
        cevaplar = Cevaplar.objects.get(sorular_id=sorular.id)
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  
        else:
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  
    else:
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)
            context = {'sorular':sorular,'haberler':haberler,'durum':durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  
        else:
            context = {'sorular':sorular,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}  

    return render(request,"base/kayitonay/kayit-onay-form.html",context)



#!HAREKETLER
def Hareketler(request):
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    if not request.user.is_superuser:
        return redirect("404")
    hareketler = Hareket.objects.all().order_by("-guncellenme_tarihi")
    p = Paginator(hareketler,20)
    page = request.GET.get('page')
    hareket = p.get_page(page)

    context = {'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim,'hareketler':hareket}
    return render(request,"base/hareket/hareketler.html",context)  



@login_required(login_url='giris-yap')
def GelenKutusuCevaplama(request,iletisim_id):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    iletisim= Iletisim.objects.get(id=iletisim_id)
    if request.user.is_authenticated:
        iletisim.goruldu.add(request.user.id)
    if request.method=='POST':
        Iletisim_cevap.objects.create(
            user=User.objects.get(id=iletisim.user.id),
            cevap=request.POST['cevap'],
            iletisim=iletisim,
        )
        messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Cevabınız kaydedildi.</div>')
        return redirect("anasayfa")
    context={'iletisim':iletisim,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/gelen-kutusu-cevaplama.html",context)


#!AYARLAR VE PROFİL
#!------------------------------
@login_required(login_url='giris-yap')
def Ayarlar(request):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     

    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    

    context = {'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/ayarlar/ayarlar.html",context)  

@login_required(login_url='giris-yap')
def ProfilFotoView(request,pk):
    onaydurum = OnayDurum.objects.get(kisi_id=pk)
    
    if ProfilFoto.objects.all().filter(user_id=pk):
        return redirect("profil-foto-duzenle",ProfilFoto.objects.get(user_id=pk).user.id)
    
    form = ProfilFotoForm()
    if request.method=='POST':
        data = request.POST.copy()
        data['user'] = User.objects.get(id=pk)
        form = ProfilFotoForm(data=data,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Profiliniz güncellendi.</div>')
            return redirect("ayarlar")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
        
        
    if ProfilFoto.objects.all().filter(user_id=pk):
        foto = ProfilFoto.objects.get(user_id=pk)
        context = {'form':form,'foto':foto,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {'form':form,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/ayarlar/profil-foto.html",context)


def Profil(request,my_slug):
    profil_user = ProfilFoto.objects.get(username_slug=my_slug)
    cevap_profil_url="";
    if request.user.is_authenticated:
        cevap_profil_url=ProfilFoto.objects.get(user_id=request.user.id).resim

    user = User.objects.get(username = profil_user.username)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    forumlari = ForumSoru.objects.filter(profil_id=profil_user.id)
    takipciler = ProfilFoto.objects.get(username_slug=my_slug).takipciler.all()
    takip_edilenler = ProfilFoto.objects.get(username_slug=my_slug).takip_edilenler.all()

    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     

    if OnayDurum.objects.all().filter(kisi_id=profil_user.user.id):
        durum = OnayDurum.objects.get(kisi_id=profil_user.user.id)
        context={'durum':durum,'haberler':haberler,'cevap_profil_url':cevap_profil_url,'user':user,'profil':profil_user,'forumlari':forumlari,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim,"takipciler":takipciler,"takip_edilenler":takip_edilenler}
    else:
        context={'haberler':haberler,'cevap_profil_url':cevap_profil_url,'user':user,'profil':profil_user,'forumlari':forumlari,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim,"takipciler":takipciler,"takip_edilenler":takip_edilenler}
    return render(request,"base/ayarlar/profil.html",context)  

def Profil1(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     

    profil_user = ProfilFoto.objects.get(id=pk)

    user = User.objects.get(username = profil_user.username)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    forumlari = ForumSoru.objects.filter(profil_id=profil_user.id)

    
    if OnayDurum.objects.all().filter(kisi_id=profil_user.user.id):
        durum = OnayDurum.objects.get(kisi_id=profil_user.user.id)
        context={'durum':durum,'haberler':haberler,'user':user,'profil':profil_user,'forumlari':forumlari,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context={'haberler':haberler,'user':user,'profil':profil_user,'forumlari':forumlari,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/ayarlar/profil.html",context)  

@login_required(login_url='giris-yap')
def ProfilFotoDuzenle(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
        
    foto = ProfilFoto.objects.get(user_id=pk)
    onaydurum = OnayDurum.objects.get(kisi_id=pk)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    if foto.username!=request.user.username:
        return redirect("404")

    if foto.user!=request.user:
        return redirect("404")

    ins = ProfilFoto.objects.get(user_id=pk)
    form = ProfilFotoForm(instance=ins)
    if request.method=='POST':
        data = request.POST.copy()
        data['user'] = User.objects.get(id=pk)
        data['username'] = User.objects.get(id=pk).username
        data['username_slug'] = slugify(User.objects.get(id=pk).username)
        data['takipciler'] = len(ProfilFoto.objects.get(user_id=request.user.id).takipciler.all())
        data['takip_edilenler'] = len(ProfilFoto.objects.get(user_id=request.user.id).takip_edilenler.all())
        data['username_slug'] = slugify(User.objects.get(id=pk).username)
        form = ProfilFotoForm(instance=ins,data=data,files=request.FILES)
        if form.is_valid():
            Hareket.objects.create(
                hareket = foto.username + " adlı kullanıcı profilini güncelledi.",
                admin_mi=0,
            )
            form.save()
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Profiliniz başarıyla güncellendi.</div>')
            return redirect("profil",slugify(request.user.username))
        else:
            messages.error(request,'<div class="btn btn-danger message p-2 rounded-3">Girdileriniz doğru değil, girdiğiniz dosyaların türünü kontrol ediniz.</div>')
        
        
            
        
    context = {'foto':foto,'form':form,'onaydurum':onaydurum,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/ayarlar/profil-foto.html",context)
#!------------------------------



#!FORUMLAR
#!------------------------------
def Forumlar(request):
    if request.user.is_authenticated:
        for i in ForumSoru.objects.all().order_by('-guncellenme_tarihi'):
            if request.user.is_authenticated and request.user not in i.goruldu.all():
                i.goruldu.add(request.user.id)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    forumlar = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
    cevap_profil_url="";
    if request.user.is_authenticated:
        cevap_profil_url=ProfilFoto.objects.get(user_id=request.user.id).resim
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    if request.method=='POST':
        arama = request.POST['arama']
        forumlar = ForumSoru.objects.all().filter(baslik__contains=arama).order_by('guncellenme_tarihi')
    if request.user.is_authenticated:
        onay_durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'forumlar':forumlar,'cevap_profil_url':cevap_profil_url,'haberler':haberler,'onaydurum':onay_durum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    else:
        context = {'forumlar':forumlar,'cevap_profil_url':cevap_profil_url,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}

    return render(request,"base/forum/forumlar.html",context) 


@login_required(login_url='giris-yap')
def Begenme(request,pk):
    forum = ForumSoruCevap.objects.get(id=pk)
    if request.user in forum.likes.all():
        forum.likes.remove(request.user.id)
    else:
        forum.likes.add(request.user.id)
        forum.dislikes.remove(request.user.id)
    
    return redirect("forum",forum.soru.id)


@login_required(login_url='giris-yap')
def Begenmeme(request,pk):
    forum = ForumSoruCevap.objects.get(id=pk)
    if request.user in forum.dislikes.all():
        forum.dislikes.remove(request.user.id)
    else:
        forum.dislikes.add(request.user.id)
        forum.likes.remove(request.user.id)
    
    return redirect("forum",forum.soru.id)


@login_required(login_url='giris-yap')
def BegenmeForum(request,pk):
    forum = ForumSoru.objects.get(id=pk)
    if request.user in forum.likes.all():
        forum.likes.remove(request.user.id)
    else:
        forum.likes.add(request.user.id)
        forum.dislikes.remove(request.user.id)
    
    return redirect("forumlar")
    

@login_required(login_url='giris-yap')    
def BegenmemeForum(request,pk):
    forum = ForumSoru.objects.get(id=pk)
    if request.user in forum.dislikes.all():
        forum.dislikes.remove(request.user.id)
    else:
        forum.dislikes.add(request.user.id)
        forum.likes.remove(request.user.id)
    
    return redirect("forumlar")


@login_required(login_url='giris-yap')
def BegenmeProfilForum(request,pk):
    forum = ForumSoru.objects.get(id=pk)
    if request.user in forum.likes.all():
        forum.likes.remove(request.user.id)
    else:
        forum.likes.add(request.user.id)
        forum.dislikes.remove(request.user.id)
    
    return redirect("profil",slugify(forum.profil.user.username))


@login_required(login_url='giris-yap')
def BegenmemeProfilForum(request,pk):
    forum = ForumSoru.objects.get(id=pk)
    if request.user in forum.dislikes.all():
        forum.dislikes.remove(request.user.id)
    else:
        forum.dislikes.add(request.user.id)
        forum.likes.remove(request.user.id)
    return redirect("profil",forum.profil.username_slug)


def ForumCevapla(request,pk):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum1 in forumlar1:
            if request.user not in forum1.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
    soru = ForumSoru.objects.get(id=pk)
    forum = ForumSoruCevap.objects.all().filter(soru_id=soru.id)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    
    if request.user.is_authenticated:
        soru.goruldu.add(request.user.id)
    if request.method=='POST':
        list_post = list(request.POST)
        list_post.sort()
        if list_post[0] == "cevap":
            ForumSoruCevap.objects.create(
                profil=ProfilFoto.objects.get(user_id=request.user),
                onay_durum=OnayDurum.objects.get(kisi_id=request.user),
                soru=soru,
                cevap=request.POST['cevap'],
                cevaba_cevap = None,
            )  
        else:
            ForumSoruCevap.objects.create(
                profil=ProfilFoto.objects.get(user_id=request.user),
                onay_durum=OnayDurum.objects.get(kisi_id=request.user),
                soru=soru,
                cevap=request.POST['cevap'],
                cevaba_cevap = ForumSoruCevap.objects.get(id=int(list_post[0])),
            )
        soru.yanit_sayi = str(int(soru.yanit_sayi)+1)
        soru.save()
    context = {'forum':forum,'soru':soru,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/forum/forum.html",context) 


@login_required(login_url='giris-yap')
def ForumCevapSil(request,pk):
    forum = ForumSoruCevap.objects.get(id=pk)
    soru = ForumSoru.objects.get(id=forum.soru_id)
    if len(ForumSoruCevap.objects.filter(cevaba_cevap=forum.id))>0:
        sayi = len(ForumSoruCevap.objects.filter(cevaba_cevap=forum.id))
        soru.yanit_sayi = str(int(soru.yanit_sayi)-sayi-1)
    else:
        soru.yanit_sayi = str(int(soru.yanit_sayi)-1)
    soru.save()
    forum.delete()
    return redirect("forum",forum.soru_id) 


@login_required(login_url='giris-yap')
def ForumSil(request,pk):
    forum = ForumSoru.objects.get(id=pk)
    if not((request.user.is_superuser)  or (forum.profil.username==request.user.username)):
        return redirect("404")
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum1 in forumlar1:
            if request.user not in forum1.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    
    if request.method=='POST':
        if request.user.is_superuser  or forum.profil.username==request.user.username:
            forum.delete()
            Hareket.objects.create(
                hareket=forum.baslik+" başlıklı forum "+ request.user.username +" adlı kişi tarafından silindi.",
                admin_mi=0,
            )
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Forum başarıyla silindi.</div>')
            return redirect("forumlar")
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
        
    context={'forum':forum,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'haberler':haberler,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/forum/forum-sil.html",context)


@login_required(login_url='giris-yap')
def ForumEkle(request):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    onaydurum = OnayDurum.objects.get(kisi_id = request.user.id)
    if onaydurum.onaydurum!="Kabul Et":
        return redirect("forum-eklenemez")
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    form = ForumEkleForm()
    if request.method=="POST":
        data = request.POST.copy()
        data['profil']=ProfilFoto.objects.get(user_id=request.user.id)
        data['onay_durum'] = OnayDurum.objects.get(kisi_id=request.user.id)
        
        form = ForumEkleForm(data)
        if form.is_valid():
            form.save()
            Hareket.objects.create(
                hareket = request.POST['baslik'] +" başlıklı forum "+ request.user.username +" tarafından forumlara eklendi.",
                admin_mi=0,
            )
            messages.success(request,'<div class="btn btn-success message p-2 rounded-3">Formunuz başarıyla oluşturuldu.</div>')
            return redirect('forumlar')
        else:
            messages.success(request, '<div class="btn btn-danger message p-2 rounded-3">Bir hata oluştu.</div>')
    
    
    context={'form':form,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/forum/forum-ekle.html",context)

@login_required(login_url='giris-yap')
def ForumOlusturulamaz(request):
    if True:
        haber_bildirim=False
        ev_bildirim=False
        forum_bildirim=False
        form_bildirim=False
        oyuncu_bildirim=False
        iletisim1 = Iletisim.objects.all().order_by('-guncellenme_tarihi')
        haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')
        forumlar1 = ForumSoru.objects.all().order_by('-guncellenme_tarihi')
        formlar1 = Sorular.objects.all().order_by('-guncellenme_tarihi')
        oyuncular1 = Kullanici.objects.all().order_by('-guncellenme_tarihi')
        for iletisim in iletisim1:
            if request.user not in iletisim.goruldu.all() and request.user.is_authenticated:
                ev_bildirim=True
                break;
        for haber in haberler1:
            if request.user not in haber.goruldu.all() and request.user.is_authenticated:
                haber_bildirim=True
                break;
        for forum in forumlar1:
            if request.user not in forum.goruldu.all() and request.user.is_authenticated:
                forum_bildirim=True
                break
        for form in formlar1:
            if request.user not in form.goruldu.all() and request.user.is_authenticated:
                form_bildirim=True
                break
        for oyuncu in oyuncular1:
            if request.user not in oyuncu.goruldu.all() and request.user.is_authenticated:
                oyuncu_bildirim=True
                break
     
    onaydurum = OnayDurum.objects.get(kisi_id=request.user.id)
    haberler = Haberler.objects.all().order_by('-olusturulma_tarihi')[:5]
    context={'onaydurum':onaydurum,'haberler':haberler,'ev_bildirim':ev_bildirim,'haber_bildirim':haber_bildirim,
            'forum_bildirim':forum_bildirim,'form_bildirim':form_bildirim,'oyuncu_bildirim':oyuncu_bildirim}
    return render(request,"base/forum/forum-eklenemez.html",context)

#!------------------------------