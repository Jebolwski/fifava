import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.api import serializers
from base.api.serializers import ForumYanitSerializer

from base.models import *


#!FORUM CEVABI FONKSİYONLARI

@api_view(['POST','GET'])
def ForumCevabiniBegen(request,pk):
    if request.method=="POST":
        user = User.objects.get(username=request.data.get("username"))
        cevap = ForumSoruCevap.objects.get(id=pk)
        if user in cevap.likes.all():
            cevap.likes.remove(user.id)
        else:
            cevap.likes.add(user.id)
            cevap.dislikes.remove(user.id)
    
    begen_sayi = ForumSoruCevap.objects.get(id=pk).likes.all().count()

    return Response(begen_sayi)

@api_view(['POST','GET'])
def ForumCevabiniBegenme(request,pk):
    if request.method=="POST":
        user = User.objects.get(username=request.data.get("username"))
        cevap = ForumSoruCevap.objects.get(id=pk)
        if user in cevap.dislikes.all():
            cevap.dislikes.remove(user.id)
        else:
            cevap.dislikes.add(user.id)
            cevap.likes.remove(user.id)

    begenme_sayi = ForumSoruCevap.objects.get(id=pk).dislikes.all().count()
    
    return Response(begenme_sayi)

@api_view(['POST','GET'])
def ForumCevapBegenRenk(request,pk):
    user = User.objects.get(username=request.data.get("username"))
    cevap = ForumSoruCevap.objects.get(id=pk)

    begen = 0
    if user in cevap.likes.all():
        begen="begenildi"
    else:
        begen="begenildi isaretlenmedi"
    
    return Response(begen)

@api_view(['POST','GET'])
def ForumCevapBegenmeRenk(request,pk):
    user = User.objects.get(username=request.data.get("username"))
    cevap = ForumSoruCevap.objects.get(id=pk)

    begenme = 0
    if user in cevap.dislikes.all():
        begenme="begenilmedi"
    else:
        begenme="begenilmedi isaretlenmedi"
    
    return Response(begenme)


@api_view(['POST','GET'])
def ForumCevapla(request,pk):
    cevaba_cevap1 = "-1"
    if request.data['cevaba_cevap']!="-1":
        cevaba_cevap1 = ForumSoruCevap.objects.get(id=request.data['cevaba_cevap'])
    else:
        cevaba_cevap1 = None
    
    ForumSoruCevap.objects.create(
        profil = ProfilFoto.objects.get(user_id=pk),
        onay_durum = OnayDurum.objects.get(kisi_id=pk),
        cevaba_cevap = cevaba_cevap1,
        soru = ForumSoru.objects.get(id=request.data['soru_id']),
        cevap = request.data['cevap'],
    )
    forum1 = ForumSoruCevap.objects.filter(cevap=request.data['cevap']).order_by("-guncellenme_tarihi")[0]
    serializer = ForumYanitSerializer(forum1,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def ForumCevapSil(request,pk):
    forumcevap = ForumSoruCevap.objects.get(id=pk)
    user_id = request.data['user_id']
    if (forumcevap.profil==ProfilFoto.objects.get(user_id=user_id)) or User.objects.get(id=user_id).is_superuser:
        forumcevap.delete()
        return Response("Silindi")

@api_view(['POST','GET'])
def ForumCevapGel(request):
    profil = ProfilFoto.objects.get(username=request.data['username'])
    print(profil)
    forum_soru_cevap = list(ForumSoruCevap.objects.all().filter(profil_id=profil.id).order_by("-guncellenme_tarihi"))
    print(forum_soru_cevap)
    serializer = ForumYanitSerializer(forum_soru_cevap,many=False)
    return Response(serializer.data)

#!FORUM FONKSİYONLARI
@api_view(['POST','GET'])
def ForumBegen(request,pk):
    if request.method=="POST":
        user = User.objects.get(username=request.data.get("username"))
        cevap = ForumSoru.objects.get(id=pk)
        if user in cevap.likes.all():
            cevap.likes.remove(user.id)
        else:
            cevap.likes.add(user.id)
            cevap.dislikes.remove(user.id)
    
    forum_sayi = ForumSoru.objects.get(id=pk).likes.all().count()

    return Response(forum_sayi)

@api_view(['POST','GET'])
def ForumBegenme(request,pk):
    if request.method=="POST":
        user = User.objects.get(username=request.data.get("username"))
        cevap = ForumSoru.objects.get(id=pk)
        if user in cevap.dislikes.all():
            cevap.dislikes.remove(user.id)
        else:
            cevap.dislikes.add(user.id)
            cevap.likes.remove(user.id)

    forum_sayi = ForumSoru.objects.get(id=pk).dislikes.all().count()

    return Response(forum_sayi)

@api_view(['POST','GET'])
def ForumBegenmeRenk(request,pk):
    user = User.objects.get(username=request.data.get("username"))
    cevap = ForumSoru.objects.get(id=pk)

    begenme = 0
    if user in cevap.dislikes.all():
        begenme="begenilmedi"
    else:
        begenme="begenilmedi isaretlenmedi"
    
    return Response(begenme)

@api_view(['POST','GET'])
def ForumBegenRenk(request,pk):
    user = User.objects.get(username=request.data.get("username"))
    cevap = ForumSoru.objects.get(id=pk)

    begen = 0
    if user in cevap.likes.all():
        begen="begenildi"
    else:
        begen="begenildi isaretlenmedi"
    
    return Response(begen)


#!ANASAYFANIN İLETİŞİM FONKSİYONLARI
@api_view(['POST','GET'])
def IletisimCevaplama(request):
    data = request.data
    Iletisim.objects.create(
        ad_soyad = data['ad_soyad'],
        baslik = data['baslik'],
        aciklama = data['aciklama'],
        user = User.objects.get(username=data['username']),
    )
    return Response("Oluşturuldu!")

