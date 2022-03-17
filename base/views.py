from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


from .forms import CevapForm, OnayForm, OyuncuForm,SorularForm,KayitForm,HaberForm,IletisimForm

from django.core.paginator import Paginator


from .models import *

from django.contrib import messages


#?CLASS BASED VIEWS
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


def Bulunamadi1(request):
    return render(request,'base/404.html')


def Bulunamadi(request,exception):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/404.html',context)


def Hata(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request,'base/500.html',context)


def GirisYap(request):
    if request.user.is_authenticated and OnayDurum.objects.get(kisi_id=request.user.id).onaydurum!="Yasakla":
            return redirect('anasayfa')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        person = authenticate(
            request, username=username, password=password)

        if person is not None:
            if OnayDurum.objects.get(kisi_id=person.id).onaydurum=="Yasakla":
                messages.success(request,"Bu hesap yasaklandı.")
                return redirect("giris-yap")
            login(request, person)
            messages.success(request, 'Başarıyla giriş yapıldı.')
            return redirect('anasayfa')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı.')
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    context = {'haberler':haberler}
    return render(request, 'base/giris.html',context)


def CikisYap(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı.")
    return redirect("anasayfa")


def KayitOl(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form = KayitForm()
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarıyla kayıt olundu.')
            OnayDurum.objects.update_or_create(kisi = User.objects.get(username = request.POST['username']),onaydurum = "Cevapsız")
            return redirect('giris-yap')
        else:
            messages.error(request, "Kayıt başarı ile gerçekleştirilemedi.")

    context = {
        'form': form,'haberler':haberler
    }
    return render(request, 'base/kayit.html', context)



def Ev(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form = IletisimForm()
    if request.method=='POST':
        Iletisim.objects.create(
        baslik=request.POST['baslik'],
        ad_soyad = request.POST['ad_soyad'],
        aciklama=request.POST['aciklama'],
        dosya = request.FILES.get('file'),
        )
        messages.success(request,"Bilgiler başarıyla kaydedildi.")
        return redirect("anasayfa")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'durum':durum,'haberler':haberler,'form':form}
    else:
        context={'haberler':haberler,'form':form}
    return render(request,"base/anasayfa.html",context)


def NasilKatilabilirim(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'durum':durum,'haberler':haberler}
    else:
        context={'haberler':haberler}
    return render(request,"base/nasil-katilabilirim.html",context)

#?KİŞİ CRUD
def Kisiler(request):
    kisiler = Kullanici.objects.all().order_by('oyun_ad_soyad')
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    
    if request.method=="POST":
        arama = request.POST['arama']
        kisiler = Kullanici.objects.all().filter(oyun_ad_soyad__contains=arama).order_by('oyun_ad_soyad')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'kisiler':kisiler,'haberler':haberler,'durum':durum}
    else:
        context = {'kisiler':kisiler,'haberler':haberler}
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
            messages.success(request,'Emailiniz başarıyla değiştirildi.')
            return redirect('ayarlar')
        elif yeni_email1!=yeni_email2:
            messages.success(request,'Yeni emailler uyuşmuyor...')
        elif eski_email!=request.user.email:
            messages.success(request,'Eski emailinizi yanlış girdiniz...')
        else:
            messages.success(request,'Bir hata oluştu.')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
    context={'durum':durum}
    return render(request,"base/email-degistir.html")

@login_required(login_url='giris-yap')
def KisiEkle(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form = OyuncuForm()
    if request.method == 'POST':
        data = request.POST.copy()
        data['oyun_ad_soyad_slug'] = slugify(request.POST['oyun_ad_soyad'])
        form = OyuncuForm(data)
        if form.is_valid():
            form.save()
            messages.success(request,"Oyuncu başarıyla oluşturuldu.")
            return redirect('kisiler')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
    context = {'form':form,'haberler':haberler,'durum':durum}
    return render(request,"base/kisi/kisi-ekle.html",context)

@login_required(login_url='giris-yap')
def KisiDuzenle(request,my_slug):
    
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    instance = Kullanici.objects.get(oyun_ad_soyad_slug=my_slug)
    form = OyuncuForm(instance=instance)
    if request.method == 'POST':
        data = request.POST.copy()
        data['oyun_ad_soyad_slug'] = slugify(request.POST['oyun_ad_soyad'])
        form = OyuncuForm(instance=instance,data = data)
        if form.is_valid():
            form.save()
            messages.success(request,"Oyuncu başarıyla düzenlendi.")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'form':form , 'haberler':haberler,'durum':durum}
    else:
        context = {'form':form , 'haberler':haberler}

    return render(request,"base/kisi/kisi-duzenle.html",context)

@login_required(login_url='giris-yap')
def KisiSil(request,my_slug):
    
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    instance = Kullanici.objects.get(oyun_ad_soyad_slug=my_slug)
    
    if request.method == 'POST':
        instance.delete()
        messages.success(request,"Oyuncu başarıyla silindi.")
        return redirect('kisiler')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {"haberler":haberler,'kisi':instance,'durum':durum}
    else:
        context = {"haberler":haberler,'kisi':instance}
    return render(request,"base/kisi/kisi-sil.html",context)


#?HABER CRUD
def Haberlerim(request):
    
    haberler1 = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')
    p = Paginator(haberler,10)
    page = request.GET.get('page')
    haber = p.get_page(page)
    if request.method=='POST':
        arama=request.POST['arama']
        sorular=Haberler.objects.filter(baslik__icontains=arama).order_by('-guncellenme_tarihi')
        p = Paginator(sorular,10)
        page = request.GET.get('page')
        haber = p.get_page(page)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haber,'haberler1':haberler1,'durum':durum}
    else:
        context = {'haberler':haber,'haberler1':haberler1}
    return render(request,"base/haber/haberler.html",context)


@login_required(login_url='giris-yap')
def HaberEkle(request):
    form = HaberForm()
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    
    if request.method=='POST':
        Haberler.objects.create(
        baslik=request.POST['baslik'],
        aciklama=request.POST['aciklama'],
        resim=request.FILES.get('file'),
        baslik_slug = slugify(request.POST['baslik']),
        )
        messages.success(request,"Haber başarıyla oluşturuldu.")
        return redirect('haberler')
        context = {'form':form,'haberler':haberler}
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'form':form,'haberler':haberler,'durum':durum}
    else:
        context = {'form':form,'haberler':haberler}
    return render(request,"base/haber/haber-ekle.html",context)
            

def HaberDetay(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    haber = Haberler.objects.get(baslik_slug=my_slug)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haber':haber,'haberler':haberler,'durum':durum}
    else:
        context = {'haber':haber,'haberler':haberler}
    return render(request,"base/haber/haber-detay.html",context)


@login_required(login_url='giris-yap')
def HaberDuzenle(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    instance = Haberler.objects.get(baslik_slug=my_slug)
    if request.method == 'POST':
            instance.baslik=request.POST['baslik']
            instance.aciklama=request.POST['aciklama']
            instance.baslik_slug = slugify(request.POST['baslik'])
            temizle=request.POST.get('temizle')
            if temizle=='on':
                instance.resim.delete()
            if request.FILES:
                instance.resim=request.FILES['file']
            instance.save()
            messages.success(request,"Haber başarıyla düzenlendi.")
            return redirect("haberler")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'instance':instance,'haberler':haberler,'durum':durum}
    else:
        context = {'instance':instance,'haberler':haberler}
    return render(request,"base/haber/haber-duzenle.html",context)


@login_required(login_url='giris-yap')
def HaberSil(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    haber = Haberler.objects.get(baslik_slug=my_slug)
    if request.method=="POST":
        haber.delete()
        messages.success(request,'Haber başarıyla silindi.')
        return redirect('haberler')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'haber':haber,'haberler':haberler,'durum':durum}
    else:
        context={'haber':haber,'haberler':haberler}

    return render(request,"base/haber/haber-sil.html",context)

#!FORM
def Formlar(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    sorular=Sorular.objects.all().order_by('-guncellenme_tarihi')
    cevaplananlar=Cevaplar.objects.all().filter(kayitli_id=request.user.id).order_by('-guncellenme_tarihi')
    p = Paginator(sorular,10)
    page = request.GET.get('page')
    soru = p.get_page(page)
    if request.method=='POST':
        arama=request.POST['arama']
        sorular=Sorular.objects.filter(baslik__icontains=arama).order_by('-guncellenme_tarihi')
        p = Paginator(sorular,10)
        page = request.GET.get('page')
        soru = p.get_page(page)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={"formlar":soru,"cevap":cevaplananlar,'haberler':haberler,'durum':durum}
    else:
        context={"formlar":soru,"cevap":cevaplananlar,'haberler':haberler}
    return render(request,"base/form/formlar.html",context)


@login_required(login_url='giris-yap')
def FormEkle(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form = SorularForm()
    if request.method=="POST":
        print(request.POST)
        data = request.POST.copy()
        data['baslik_slug'] = slugify(data['baslik'])
        form = SorularForm(data)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,"Anket başarıyla oluşturuldu.")
            return redirect("formlar")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={"form":form,'haberler':haberler,'durum':durum}
    else:
        context={"form":form,'haberler':haberler}
    return render(request,"base/form/form-ekle.html",context)


@login_required(login_url='giris-yap')
def FormDuzenle(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form_instance = Sorular.objects.get(baslik_slug=my_slug)
    form = SorularForm(instance=form_instance)
    if request.method=="POST":
        data = request.POST.copy()
        data['baslik_slug'] = slugify(request.POST['baslik'])
        form = SorularForm(data,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={"form":form,'haberler':haberler,'durum':durum}
    else:
        context={"form":form,'haberler':haberler}

    return render(request,"base/form/form-duzenle.html",context)


@login_required(login_url='giris-yap')
def FormSil(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form=Sorular.objects.get(baslik_slug=my_slug)
    if request.method=='POST':
        form.delete()
        return redirect("formlar")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'form':form,'haberler':haberler,'durum':durum}
    else:
        context={'form':form,'haberler':haberler}

    return render(request,"base/form/form-sil.html",context)


@login_required(login_url='giris-yap')
def FormCevapla(request,my_slug):
    form = CevapForm()
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    sorular = Sorular.objects.get(baslik_slug = my_slug)
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
            messages.success(request, 'Cevaplarınız başarıyla kaydedildi.')
            return redirect('formlar')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'form':form,'sorular':sorular,'haberler':haberler,'durum':durum}
    else:
        context={'form':form,'sorular':sorular,'haberler':haberler}

    return render(request,"base/form/form-cevapla.html",context)


def FormDetay(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    soru=Sorular.objects.get(baslik_slug = my_slug)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'soru':soru,'haberler':haberler,'durum':durum}
    else:
        context={'soru':soru,'haberler':haberler}
    return render(request,"base/form/form-detay.html",context)


@login_required(login_url='giris-yap')
def FormAnaliz(request,my_slug):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form = Sorular.objects.get(baslik_slug = my_slug)
    cevap = Cevaplar.objects.all().filter(sorular_id=form.id)
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
    for i in range(0,len(array)):
        if array[i]!=0:
            print("Soru "+str(i+1)+" katılma yüzdesi",array[i],"%")
    cevaplar = Cevaplar.objects.all().order_by('-guncellenme_tarihi')
    p = Paginator(Cevaplar.objects.all().filter(sorular_id=form.id),1)
    page = request.GET.get('page')
    cevaplar_hepsi = p.get_page(page)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {
        'form':form,'cevap':cevap,'yuzde':yuzde,'sikli_soru_sayisi':bolmesayac,
    'dizi':array,'sorusayac':sorucount,'cevaplar':cevaplar_hepsi,'cevaplarim':cevaplar,'haberler':haberler,'durum':durum}
    else:
        context = {
        'form':form,'cevap':cevap,'yuzde':yuzde,'sikli_soru_sayisi':bolmesayac,
    'dizi':array,'sorusayac':sorucount,'cevaplar':cevaplar_hepsi,'cevaplarim':cevaplar,'haberler':haberler}

    return render(request,"base/form/form-analiz.html",context)


@login_required(login_url='giris-yap')
def Cevaplanmis(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haberler,'durum':durum}
    else:
        context = {'haberler':haberler}

    return render(request,"base/form/cevaplanmis.html",context)


@login_required(login_url='giris-yap')
def CevaplanmisDuzenle(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    form_instance = Cevaplar.objects.get(id=pk)
    form = CevapForm(instance=form_instance)
    sorular = Sorular.objects.filter(id=form_instance.sorular_id)
    if request.method=='POST':
        data = request.POST.copy()
        data['baslik']=form_instance.baslik
        form = CevapForm(data,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect("formlar")
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'form':form,'sorular':sorular,'haberler':haberler,'durum':durum}
    else:
        context={'form':form,'sorular':sorular,'haberler':haberler}


    return render(request,"base/form/cevaplanmis-duzenle.html",context)


@login_required(login_url='giris-yap')
def CevapDetay(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    cevap = Cevaplar.objects.get(id=pk)
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'cevap':cevap,'haberler':haberler,'durum':durum}
    else:
        context = {'cevap':cevap,'haberler':haberler}

    return render(request,"base/form/cevap-detay.html",context)

@login_required(login_url='giris-yap')
def CevapSil(request,pk):
    cevap=Cevaplar.objects.filter(id=pk)
    cevap.delete()
    return redirect("formlar")


@login_required(login_url='giris-yap')
def KayitOnay(request):
    onay = OnayDurum.objects.all().order_by("-onaydurum")
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haberler,'onay':onay,'durum':durum}
    else:
        context = {'haberler':haberler,'onay':onay}

    return render(request,"base/kayitonay/kayit-onay.html",context)

@login_required(login_url='giris-yap')
def KayitKabulEt(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    user = User.objects.get(id=pk)
    form = OnayForm()
    if request.method=='POST':
        data = request.POST.copy()
        data['kisi'] = user
        data.kisi = user
        print(data)
        form = OnayForm(data)
        if form.is_valid():
            form.save()
            return redirect('kayit-onay')
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'form':form,'haberler':haberler,'durum':durum}
    else:
        context = {'form':form,'haberler':haberler}

    return render(request,"base/kayitonay/kayit-kabul-et.html",context)


@login_required(login_url='giris-yap')
def KayitBeklet(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    user = User.objects.get(id=pk)
    form = OnayForm()
    if request.method=='POST':
        data = request.POST.copy()
        data.kisi = user
        form = OnayForm(data)
        if form.is_valid():
            form.save()
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'form':form,'kisi':user,'haberler':haberler,'durum':durum}
    else:
        context = {'form':form,'kisi':user,'haberler':haberler}

    return render(request,"base/kayitonay/kayit-beklet.html",context)


@login_required(login_url='giris-yap')
def KayitReddet(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    user = User.objects.get(id=pk)
    form = OnayForm()
    if request.method=='POST':
        data = request.POST.copy()
        data.kisi = user
        form = OnayForm(data)
        if form.is_valid():
            form.save()
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)       
        context = {'form':form,'kisi':user,'haberler':haberler,'durum':durum}
    else:
        context = {'form':form,'kisi':user,'haberler':haberler}

    return render(request,"base/kayitonay/kayit-beklet.html",context)


@login_required(login_url='giris-yap')
def KayitOnayFormDuzenle(request,pk):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    kisi = User.objects.get(id=pk)
    sorular = Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu")
    instance = OnayDurum.objects.get(kisi_id=kisi.id)
    form = OnayForm(instance=instance)
    if request.method=="POST":
        data = request.POST.copy()
        data['kisi'] = str(kisi.id)
        form = OnayForm(instance=instance,data=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Onay durumu güncellendi.")
            return redirect("kayit-onay")
          
    if Cevaplar.objects.all().filter(kayitli_id=kisi.id,sorular_id=sorular.id):
        
        cevaplar = Cevaplar.objects.get(sorular_id=sorular.id,kayitli_id=kisi.id)
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)  
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'durum':durum} 
        else:
            context = {'cevap':cevaplar,'sorular':sorular,'form':form} 

    else:
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)  
            context = {'sorular':sorular,'haberler':haberler,'durum':durum}  
        else:
            context = {'sorular':sorular,'haberler':haberler}  

    return render(request,"base/kayitonay/kayit-onay-form.html",context)


@login_required(login_url='giris-yap')
def KayitOnayForm(request,pk):
    kisi = User.objects.get(id=pk)
    sorular = Sorular.objects.get(baslik="FIFAVOX RolePlay Kayıt Formu")
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if len(OnayDurum.objects.all().filter(kisi_id=kisi.id))>0:
        return redirect('kayit-onay-form-duzenle',kisi.id)
    form = OnayForm()
    if request.method=="POST":
        data = request.POST.copy()
        data['kisi'] = str(kisi.id)
        form = OnayForm(data)
        if form.is_valid():
            form.save()
            messages.success(request,"Onay durumu kaydedildi.")
            return redirect("kayit-onay")
    
    if Cevaplar.objects.all().filter(sorular_id=sorular.id):
        cevaplar = Cevaplar.objects.get(sorular_id=sorular.id)
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'haberler':haberler,'durum':durum}  
        else:
            context = {'cevap':cevaplar,'sorular':sorular,'form':form,'haberler':haberler}  
    else:
        if OnayDurum.objects.all().filter(kisi_id=request.user.id):
            durum = OnayDurum.objects.get(kisi_id=request.user.id)
            context = {'sorular':sorular,'haberler':haberler,'durum':durum}  
        else:
            context = {'sorular':sorular,'haberler':haberler}  

    return render(request,"base/kayitonay/kayit-onay-form.html",context)


@login_required(login_url='giris-yap')
def Profil(request,my_slug):
    user = User.objects.get(username = request.user.username)
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context={'durum':durum,'haberler':haberler,'user':user}
    else:
        context={'haberler':haberler,'user':user}
    
    return render(request,"base/profil.html",context)  


def Ayarlar(request):
    haberler = Haberler.objects.all().order_by('-guncellenme_tarihi')[:5]
    if OnayDurum.objects.all().filter(kisi_id=request.user.id):
        durum = OnayDurum.objects.get(kisi_id=request.user.id)
        context = {'haberler':haberler,'durum':durum}
    else:
        context = {'haberler':haberler}
    return render(request,"base/ayarlar.html",context)  


def KayitOnbilgi(request):
    return render(request,"base/kayit-onbilgi.html")
