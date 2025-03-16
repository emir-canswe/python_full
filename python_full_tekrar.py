# -----LİST---
'''
x="my name is thomms thelby"

print("what is your name:",x)

print(x[5])#bu sekilde yaparsan sana istedigin kisimdaki harfi verir c dilidendeki dizler gibi
#listeler de elemanlar 0 dan baslar

a="aaaliiiia"
k=0
for i in a:#bu koddda i degeri i degerlerine teker teker ataniyor  o sirada a degerine esit old
    if i=='a':
        k+=1

#sakin unutma tek bir karakter atamsi yaptigin zaman ' ' tek tirnak işateri kulllan


print("girilen cumlede kullanilan a harfis sayisi:",k)


list=["emir","veli","kemal",535]
#listlelerin içinde farkli veri tipleri bulundurabilit
#c dilindeki diziler gibi ama diziler farkili veri tipleri bulundurmazken listelrde farkli veri tipleri bulunabilr

print(list[3])#bu sekilde istedigin elemani yazabilirsin
#listeler de diziler gibi 0 indexten baslarlar

for i in list:#bu sekilde listedeki tum elemanlari yazdirma imkanina sahipsindir
    print(i)



mylove=[12,"emir","can","gs","icardi"]

my_peach=[23,"fenerbahce","realmadrit"]


ali=mylove+my_peach

  #bu sekide iki tane listeyi birlestirebilirsin



for i in mylove:
    print(i)
#bu kod sana lşsteyş teker teker yazmani saglar
print()
for i in my_peach:
    print(i)
print()
for i in ali:
    print(i)



#----DEMETLER----

#demetler ile listeler birbirlerine benzerdir ama listelerde
# eleman atama ve cekme işlemi olurken demet veri tipnde bu işlemleri gercekelstiremiyorsun
#listeler koseli parantezlerle olusturulurken demketler normal parantezlerle olusturulur()
#pek kullanlimadigi için sg ett
mylove=[12,"emir","can","gs","icardi"]

mylove.remove("can")#silmek sitedigin degeri direkt içine yaz indexi degilll

for i in mylove:
    print(i)




#Bir alışveriş sitesinde 100 TL ve üzerine kargo bedava iken 100 TL altındaki alışverişlerde ise 20 TL
# kargo ücreti alınmaktadır. Buna göre kullanıcıdan alışveriş tutarını alıp, kargo ücreti dahil ödemesi gereken toplam tutarını ekrana yazdırınız.


a=int(input("enter please first number:"))

if a>=100:
    print("total fee:",a)
elif a<100:
    a=a+20
    print("total fee:",a)


#--------SOZLUKLER----


#c dilindeki struckara birazcik benzer
#onun gibi koseli parantez kullanimi olur



person={
   "name":"emir",
    "surmane":"can",
    "age":10
}
print(person)
b=type(person)
print(b)#girdigin degişkenin tipini istedigin sekilde bulabirsin
#kafa karistirici bir durum soz konusu degil sadece degişkkenleri içieride yazarkaen "" kullan

a=person["name"]#bu sekide istedin parametreye uzaktan ulasabiileirsin


print(a)


a = "benim adim emircan"
b = len(a)  # stringin uzunluğunu al


for i in range(b - 1, -1, -1):  # indeksi 0'a kadar tersten ilerlet ama -1 ve b-1 dahil etmiyor onlar haricindeki degerlei aliyor
    print(a[i], end="")  # aynı satırda yazmak için end parametresini kullan


for i in range(1,10):
    print(i)


a=int(input("enter please value:"))

#matigi:once a degerine bak
while(a!=0):
    print(a)
    a-=1




#---------RANGE FONKSİYONU

print(*range(3))#range fonsiyonu iki sana girdigin degere kadar olan sayilari yazdir


# ------BREAK ADN CONTUNUE---

chose = int(input("enter please number:"))

while 1:
    print("1:toplama\n2:cikarma\n3:bolme\n4:carpma\n5:cikis")
    a = int(input("\nyapmak istedigininz islemi giriniz\n"))
    if a == 1:
        b = int(input("bir sayi giriniz:"))
        c = int(input("basla bir sayi giriniz:"))
        print(b + c)
    elif a == 2:
        b = int(input("bir sayi giriniz:"))
        c = int(input("basla bir sayi giriniz:"))
        print(b - c)
    elif a == 3:
        b = int(input("bir sayi giriniz:"))
        c = int(input("basla bir sayi giriniz:"))
        print(b / c)
    elif a == 4:
        b = int(input("bir sayi giriniz:"))
        c = int(input("basla bir sayi giriniz:"))
        print(b * c)
    elif a == 5:
        print("islem sonladirilmistir")
        break


#----------METOTLARRR-----------

#metolar ozellestirilmis fonksiyonlar gibi


#-----append fonksiyonu

isim=["emir","azad","nesat","diyar"]

isim.append("muhammed")#son endexe appen içindeki degeri atiyor
print(isim)
#----İNSERT FONKSİYONU
#bu foksiyon ise senin istedigin indexe sayi atmani saglar

isim.insert(1,"galatasaray")
#1 parametre index ikinci parametre ise girmek istedigin deger

print(isim)#1 parametreyr isim degerini atadi

#CLEAR=tum degeri siler




# ---------FONKSİYONLAR----

# foksiyonlarin diger dilelrdeki fonksiyonlardan pek bir farki bulunmuyor

def fonk():
    print("mauro icardiiii")


fonk()


def fonk2(number, number1):
    return number1 + number


result = fonk2(23, 3)
print(result)
#amk farkli bir durum soz konusu degil




#-----KOMLİKE ORNEKK-----


def tip_bul(x):
    if(x==str(x)):
        return  str
    elif(x==int(x)):
        return  int
    elif(x==float(x)):
        return  float
    elif(x==bool(x)):
        return bool


list=[1,22,3242,"emir",True,"can"]

for i in list:
    print("girilen degerin turu:",tip_bul(i))




def fonk(x):
    if x > 10:

        for i in range(2, 10):
            if x % i == 0:
                return -1

    else:
        for i in range(2, 5):
            if x % i == 0:
                return -1

    return 1


a = int(input("enter please number:"))

result = fonk(a)

if result == -1:
    print("girien sayi asal degildir")
elif result == 1:
    print("girilen sayi asaldir")





#-----args foksiyonu----

#bu metot senin foksiyoa goderdşgşn sayilari hafizada turar
#ve senin işlem yapmani kolaylastiri
def toplama(*args):
    total=0
    for i in args:
        total+=i
    print("girilen sayilarin toplami:",total)

toplama(112,23,4)




# ------global degişkenler-----

# butun fonksiyonlarin içinde kullanilabiril
#fonkisyonarin uzerinde yazman lazim
t=34
def sayi():
    print(t)

def number():
    print("global degişkenin degeri:",t)
sayi()
number()

#-----end komutu


print("beni vurup yerde biakma ",end="      ")
print("emre aydin")#gereksiz bir foksiyon bir sike yaradigi yok

#---ENUMETA FONKSİYONU----
#olusturdugun listeyi indexi ile birlikte yazmani saglayan komuttur

list=["emir","can","kemal","ali"]

for b,a in enumerate(list,1):#hangi deger ve kactan basliasin demek istiyor
    print(b,a)#birinci parametre indexi yazmani 2 ise degişkenin içndeki degeri yazmani saglar




#-----  TEK BİR SATİRDA KULLANİCİDAN SAYİ ALMA İSLEMİ----
#bunu yapmak için split fonksiyonunu son kisma ekliyeceksin ama degişken turunu baslangicta kullanmana gerek yok

x,y=input("enter please x and y number:").split()



#import  math
from math import pow
#yukardaki sekidle yaparsan asida math demene gerek yok


faktoryel=math.factorial(4)#bir sayinin faktoryeli otomatik bulmani saglar

print(faktoryel)





#----datatime---

import datetime
#bugun tarihni yazmani saglar

print(datetime.datetime.now())#yil ay gun diye sana cikti verecktir



#-----UYUTMA MODELİ----

#bu sikko modul senin iki kodu ayni anda caişmani engeller

import time

print("hello")
time.sleep(4)#bu kod caliştiktan 4 saniye sonra asagidaki kod calisacak
print("softwate")

#modulelri kaydetmek için İMPORT verişsi kullanilir
"""
import os

os.system("dir")#bunu kullanmak seni tum dosayalari kaydetmeni saglar bbunun baska bir kullani daha mevcut

from os import system as komut

komut("dir")#bu sekilde sen kendine gor bir fonksiyokn adi olusturabilirsin yaptigin projelere kendi kafandan bir isim verebilirsin




#TİME MODULU

import time #bu moıdul senin ilk ciktini yazar sonra 4 saniye bekliyip diger kodunu nyazar

print("emircan")
time.sleep(4)
print("emircvanc an bu konu hakindaki fikirlerinni beyam")
time.sleep(4)
print("benim")

#olusan sayilarin sanişye cinsinden birbiribden cikjaerabilirsi,n

#RONDOM MODULU

#bilgisayar rasgele sayi secme olayidir



#bu uygul

import random
import os

while True:
     
    rasgele=random.randint(1,9)

    aayi=int(input("bir sayi gritiniz lutfen::"))
    print("rasgele girilens sayii::",rasgele)

    if rasgele==aayi:
        print("tebrikler dogru secimm")
        quit()
    else:
        input("yeniden oynamak için entere basiniz..")



    #NESNE OLUSTURMA(sinif)

    #c dilindeki strucklara benzer ayni sekilde ertişim de yapabilirsin
    #bu yerde liste  de kullanbilirssin

            #liste yomteminfde hem sayi hem de string tarzimsa kullanimi mevcutt
            
class karakter():980
        
    saglik = 0
    silah = " "
    ekipman=""
    isim=""
    cephanelik=0
    saldiri=0


savasci=karakter()
savasci.saglik=250
savasci.cephanelik=43
savasci.isim="emircan"
savasci.ekipman="kiliç"
savasci.silah="f16"
savasci.saldiri=233

buyucu=karakter()
buyucu.saglik=233
buyucu.cephanelik=50
buyucu.isim="gandalf"
buyucu.ekipman="asa"
buyucu.silah="buyu"
buyucu.saldiri=200



savasci.saglik=savasci.saglik-buyucu.saldiri
print("savascinin mevdcut sagligi::",savasci.saglik)

    


class karaketer():
    list=[]

battal=karaketer()
battal.list+=[" ede"]#bu kismda listeye eleman ekleme firsati veriyor


print(battal.list)
emir=karaketer()

emir.list+=["galatasaray"]
print(emir.list)


      """

import random
import os

class Hedef:
    def __init__(self):
        self.saglik = random.randint(5, 10)
        self.guc = random.randint(3, 8)
        self.kalkan = random.randint(1, 6)
        self.yasiyormu = True
    
    def vur(self, oyuncu):
        atak = self.guc - oyuncu.kalkan
        if atak > 0:  # Saldırı gücü pozitif olmalı
            oyuncu.saglik -= atak
        if oyuncu.saglik <= 0:
            oyuncu.yasiyormu = False


class Oyuncu:
    def __init__(self):
        self.saglik = 40
        self.guc = 7
        self.kalkan = 2
        self.yasiyormu = True
    
    def vur(self, hedeff):
        atak = self.guc - hedeff.kalkan
        if atak > 0:  # Saldırı gücü pozitif olmalı
            hedeff.saglik -= atak
        if hedeff.saglik <= 0:
            hedeff.yasiyormu = False
            hedef.remove(hedeff)  # Sağlığı sıfır olan hedefi listeden kaldır


# Hedef listesi oluşturuluyor
hedef = [Hedef() for _ in range(5)]
oyuncu = Oyuncu()

while True:
    # Konsolu temizle
    os.system("cls" if os.name == "nt" else "clear")
    
    # Oyuncu istatistiklerini yazdır
    print("Oyuncu ---- Sağlık değeri: {} ---- Saldırı değeri: {} ---- Kalkan değeri: {}".format(
        oyuncu.saglik, oyuncu.guc, oyuncu.kalkan))
    
    # Hedeflerin istatistiklerini yazdır
    for a in hedef:
        print("{}. Hedef --- Sağlık değeri: {} ---- Saldırı değeri: {} ---- Kalkan değeri: {}".format( hedef.index(a) + 1, a.saglik, a.guc, a.kalkan))
    
    # Oyuncu kaybettiyse
    if not oyuncu.yasiyormu:
        print("Kaybettiniz!")
        break
    # Tüm hedefler yenildiyse
    elif not hedef:
        print("Kazandınız!")
        break
    
    # Kullanıcının hedef seçmesi
    try:
        secim = int(input("Hedef giriniz (1-{}): ".format(len(hedef))))
        vurulanhedef = hedef[secim - 1]  # Seçilen hedef
        oyuncu.vur(vurulanhedef)  # Oyuncu hedefe vurur
        
        # Eğer hedefler kaldıysa rastgele bir hedef oyuncuya saldırır
        if hedef:
            saldirgan = hedef[random.randint(0, len(hedef) - 1)]
            saldirgan.vur(oyuncu)  # Rastgele bir hedef oyuncuya saldırır
    
    except (IndexError, ValueError):
        print("Hatalı giriş yaptınız!")
  class Hero:
    def __init__(self, healty, gun, shield, attack):
        # Karakter özelliklerini başlatma
        self.healty = healty  # Sağlık puanı
        self.gun = gun        # Silah türü
        self.shield = shield  # Kalkan değeri
        self.attack = attack  # Saldırı gücü

    def attack_opponent(self, opponent):
        # Rakibe saldırı gerçekleştirme fonksiyonu
        damage = self.attack - opponent.shield  # Saldırı gücünden rakibin kalkan gücünü çıkararak hasarı hesapla
        if damage > 0:
            opponent.healty -= damage  # Eğer hasar sıfırdan büyükse, rakibin sağlığından hasar çıkar
        else:
            damage = 0  # Eğer hasar negatifse, hasar sıfır olur (kalkan tüm hasarı engelledi)
        
        # Saldırı sonucu bilgileri ekrana yazdırma
        print(f"{opponent} karakterine {damage} hasar verildi!")
        print(f"{opponent}'in kalan sağlığı: {opponent.healty}")
        
        # Eğer rakibin sağlığı sıfıra eşit ya da daha az ise True döndür (rakip öldü)
        return opponent.healty <= 0  

    def __str__(self):
        # Karakter özelliklerini okunabilir formatta geri döndürme
        return f"Sağlık: {self.healty}, Silah: {self.gun}, Kalkan: {self.shield}, Saldırı: {self.attack}"


# Karakterlerin oluşturulması
# Elf karakteri: Sağlık 1200, Silah 'hancer', Kalkan 300, Saldırı gücü 300
elf = Hero(1200, "hancer", 300, 300)
# Ork karakteri: Sağlık 1500, Silah 'kilic', Kalkan 200, Saldırı gücü 350
ork = Hero(1500, "kilic", 200, 350)
# İnsan karakteri: Sağlık 1000, Silah 'hancer', Kalkan 400, Saldırı gücü 250
human = Hero(1000, "hancer", 400, 250)

# Kullanıcıdan saldıracak ve savunacak karakterlerin seçimi
saldiran = input("Saldıracak karakteri giriniz (elf, ork, human): ").lower()  # Karakter ismini küçük harfe çevirir
savunan = input("Savunacak karakteri giriniz (elf, ork, human): ").lower()   # Karakter ismini küçük harfe çevirir

# Seçilen saldırgan karakteri tanımlama
if saldiran == "elf":
    attacker = elf
elif saldiran == "ork":
    attacker = ork
elif saldiran == "human":
    attacker = human
else:
    print("Geçersiz saldıran karakter seçimi.")
    attacker = None  # Geçersiz giriş olursa saldırganı 'None' yap

# Seçilen savunucu karakteri tanımlama
if savunan == "elf":
    defender = elf
elif savunan == "ork":
    defender = ork
elif savunan == "human":
    defender = human
else:
    print("Geçersiz savunan karakter seçimi.")
    defender = None  # Geçersiz giriş olursa savunucuyu 'None' yap

# Eğer hem saldıran hem savunan doğru karakterler ise saldırı işlemi başlasın
if attacker and defender:
    for i in range(5):  # 5 saldırı hakkı olacak, bu yüzden döngü 5 defa çalışacak
        input(f"{i + 1}. saldırı için Enter'a basın...")  # Her saldırı için Enter'a basılmasını bekle
        if attacker.attack_opponent(defender):  # Rakip ölüyor mu? (True dönerse döngü kırılır)
            print(f"{saldiran.capitalize()} kazandı!")  # Saldırgan kazandı mesajı
            break  # Döngü biter
    else:
        # Eğer 5 saldırı sonunda her iki karakter de hayatta ise, sağlıklarına bakarak kazananı belirle
        if attacker.healty > defender.healty:
            print(f"{saldiran.capitalize()} kazandı!")  # Saldırgan daha fazla sağlıkta ise kazandı
        elif attacker.healty < defender.healty:
            print(f"{savunan.capitalize()} kazandı!")  # Savunucu daha fazla sağlıkta ise kazandı
        else:
            print("Berabere!")  # Sağlıkları eşitse berabere

#CLASS  VERİ TİPİ
'''
class karakter():
    healty=0
    gun=""
    striker=0
    kalkan=0


shadow=karakter()

shadow.gun="kilic"
shadow.healty=1000
shadow.striker=200


ork=karakter()
ork.striker=150
ork.gun="kemikkran"
ork.healty=1200
ork.kalkan=250


i=0

while True:
    if i==5:
        break
    else:
        ork.healty=ork.healty+ork.kalkan-shadow.striker
        if ork.healty==0:
            print("shadw karakteri ork karakterişni oldurmustur")

    print("devam etmerk entere basiniz")
    i+=1




import math

def bisection_method(f, a, b, imax, tol):
    Fa = f(a)
    Fb = f(b)
    
    # Başlangıç kontrolü: a ve b uç noktaları farklı işaretli olmalı
    if Fa * Fb > 0:
        print('Fonksiyon a ve b noktasında aynı işarete sahip')
        return None
    
    print(f"{'Iterasyon':<10}{'a':<15}{'b':<15}{'xi':<15}{'f(xi)':<15}{'Tolerans'}")
    
    for i in range(1, imax + 1):
        xi = (a + b) / 2  # Orta nokta hesaplanıyor
        tole = (b - a) / 2  # Güncel tolerans aralığı
        Fxi = f(xi)  # xi noktasındaki fonksiyon değeri
        
        # İterasyon bilgilerini yazdırıyoruz
        print(f"{i:<10}{a:<15}{b:<15}{xi:<15}{Fxi:<15}{tole:<15}")
        
        # Çözüm toleransı kontrolü
        if tole < tol or Fxi == 0:  # Tolerans değeri altında veya fonksiyon sıfırsa kök bulunmuştur
            print(f"Kök bulundu: {xi}")
            return xi
        
        # a ve b noktalarının yeni değerlerini belirleme
        if Fa * Fxi < 0:
            b = xi
            Fb = Fxi
        else:
            a = xi
            Fa = Fxi
    
    print("Maksimum iterasyon sayısına ulaşıldı.")
    return xi  # İterasyon sınırına ulaşsa da mevcut çözümü döndürüyoruz
'''

import turtle
import math

# Ekranı ayarlayalım
screen = turtle.Screen()
screen.bgcolor("black")  # Arka plan rengini siyah yapalım

# Kalp çizen turtle'ı başlatıyoruz
kalp = turtle.Turtle()
kalp.shape("turtle")
kalp.color("red")  # Kalp kırmızı olacak
kalp.speed(10)  # Hızlı çizin

# Kalp şeklini çizen fonksiyon
def kalp_sekli():
    kalp.begin_fill()
    kalp.left(50)
    kalp.forward(133)
    kalp.circle(50, 200)  # Üst sol yuvarlak kısım
    kalp.right(140)
    kalp.circle(50, 200)  # Üst sağ yuvarlak kısım
    kalp.forward(133)
    kalp.end_fill()

# Kalp şekli çizeceğiz
def animasyon():
    for i in range(50):
        kalp.clear()  # Her animasyon döngüsünde ekranı temizler
        kalp.penup()
        
        # X ve Y koordinatlarıyla hareket
        kalp.goto(math.sin(i * 0.2) * 200, math.cos(i * 0.2) * 200)
        
        kalp.pendown()
        kalp_sekli()  # Kalp şekli çizilsin
        turtle.update()  # Ekranı günceller

# Başlatıyoruz
turtle.tracer(0, 0)  # Animasyonu hızlı hale getirmek için
animasyon()

# Animasyon bittiğinde ekranın kapanmaması için
turtle.done()

'''



# ---JSONN---
# jspn sozluk veri tipindeki degerleri ' ' tek tirnak içine alma işlemidir

