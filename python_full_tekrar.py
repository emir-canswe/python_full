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


'''



# ---JSONN---
# jspn sozluk veri tipindeki degerleri ' ' tek tirnak içine alma işlemidir

