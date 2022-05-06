from rest_framework.response import Response
from rest_framework.decorators import api_view

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
