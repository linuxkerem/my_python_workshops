# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini  isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.


isim=input('Adınızı giriniz: ')
yas=int(input('Yaşınızı Giriniz: '))
egitim=input('Eğitim bilgilerinizi giriniz (lise,üniversite vs.) : ')

if yas>=18 :
  if egitim==('lise'or'üniversite'):
    print('{} kişisi ehliyet almaya uygundur'.format(isim))
  else:
    print('{} kişisi eğitim şartlarından dolayı ehliyet almaya uygun değildir.'.format(isim))
else:
  print('{} kişisi yaş şartlarından dolayı ehliyet almaya uygun değildir.'.format(isim))


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#           0-24 ==> 0
#           25-44==> 1
#           45-54==> 2
#           55-69==> 3
#           70-84==> 4
#           85-100==>5

isim=input('İsminizi giriniz: ')
yazili1=float(input('Birinci yazılı sınavınızı giriniz: '))
yazili2=float(input('İkinci yazılı sınavınızı giriniz: '))
sozlu=float(input('Sözlü notunuzu giriniz: '))
ortalama=(yazili1+yazili2+sozlu)/3
if 0<=ortalama<=24:
  print("{} kişisinin ortalaması:{} ,not bilgisi 0'dır.".format(isim,ortalama))
elif 24<=ortalama<=44:
    print("{} kişisinin ortalaması:{} ,not bilgisi 1'dır.".format(isim,ortalama))
elif 45<=ortalama<=54:
    print("{} kişisinin ortalaması:{} ,not bilgisi 2'dır.".format(isim,ortalama))
elif 55<=ortalama<=69:
    print("{} kişisinin ortalaması:{} ,not bilgisi 3'dır.".format(isim,ortalama))
elif 70<=ortalama<=84:
    print("{} kişisinin ortalaması:{} ,not bilgisi 4'dır.".format(isim,ortalama))
elif 85<=ortalama<=100:
     print("{} kişisinin ortalaması:{} ,not bilgisi 5'dır.".format(isim,ortalama))
else:
  print('Yanlış yada hatalı bilgi girdiniz.')


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamnını aşağıdaki bilgilere göre hesaplayınız.
#     1. Bakım => 1. yıl 
#     2. Bakım => 2. yıl 
#     3. Bakım => 3. yıl
#     **Süre hesabına alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#     *** datetime modülünü kullanmanız gerekiyor
#   (simdi) - (2018/8/1) => gün
import datetime 

days=input('Aracınız hangi tarihte trafiğe çıktı ?(2019/8/9): ')
days=days.split('/')
simdi=datetime.datetime.now()
trafigeCikis=datetime.datetime(int(days[0]),int(days[1]),int(days[2]))
fark= simdi-trafigeCikis
days=fark.days
if days<=365:
  print('Birinci servis aralığı')
elif days>=365 and days<=365*2:
  print('İkinci servis aralığı')
elif days>=365*2 and days<=365*3:
  print('Üçüncü servis aralığı')
else:
  print('Hatalı süre bilgileri')