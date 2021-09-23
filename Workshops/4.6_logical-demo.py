1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

sayi=int(input('Sayıyı giriniz: '))
result=0<sayi<100
print(result)

2- Girilen bri sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi=int(input('Sayıyı giriniz: '))
result=sayi>=0 and sayi%2==0
print('Girilen sayı çift sayı mı ? : ',result)

3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email=('keremmertizmir39@gmail.com')
password=('merhababen123')
useremail=input('Lütfen e-mailinizi giriniz: ')
userpassword=input('Lütfen şifrenizi giriniz: ')
result=email==useremail and password==userpassword

if result==1:
  print('Giriş başarıyla yapıldı.')
else:
  print('E-mail yada parola hatalı.')

4- Girilen 3 sayıyı büyüklük olarak karşılaştırın

a=int(input('Birinci sayıyı giriniz: '))
b=int(input('İkinci sayıyı giriniz: '))
c=int(input('Üçüncü sayıyı giriniz: '))
result=(a>b)and(a>c)
if result==1:
  print('İlk sayı en büyüktür.')
else:
  result=(b>a)and(b>c)

if result==1:
  print('İkinci sayı en büyüktür.')
else:
  result=(c>a)and(c>b)

if result==1:
  print('Üçüncü sayı en büyüktür.')
else:
  print('Sayıları tekrar kontrol edin.')

5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 üstündeyse geçti geçmedi mesajını verin, ve;
a-) Ortalama 50 ve üstündeyse bile final notu en az 50 olmaldır.
b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1=int(input('Birinci vize notunuzu giriniz: '))
vize2=int(input('İkinci vize notunuzu giriniz: '))
final=int(input('Final notunuzu giriniz: '))
ortalama= (vize1+vize2)*0.6 + (final*0.4)
if ortalama>=50and final>=50:
  print('Tebrikler, başarıyla geçtiniz.')
else:
    if final>=70:
      print('Tebrikler,başarıyla geçtiniz.')
    else:
      print('Üzgünüm, geçemedin.')

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo endekslerini hesaplayınız.
      Formül: (Kilo/boy uzunluğunun karesi)
      Aşağıdaki tabloya göre kişi hangi gruba girmektedir
      0-18.4 => Zayıf
      18.5-24.9=> Normal
      25.0-29.9=> Fazla Kilolu
      30.0-34.9=> Şişman (Obez)


name=input('Lütfen adınızı giriniz: ')
kilo=float(input('Lütfen kilonuzu giriniz: '))
boy=float(input('Lütfen boyunuzu giriniz: '))
formul=(kilo) / (boy ** 2)
if 0<=formul<=18.4:
  print('{} kişişi boy kilo endeksine göre zayıf. '.format(name))
else:
  if 18.5<=formul<=24.9:
    print('{} kişisi boy kilo endeksine göre normal. '.format(name))
  else:
    if 25<=formul<=29.9:
      print('{} kişisi boy kilo endeksine göre fazla kilolu. '.format(name))
    else:
      if 30.0<=formul<=34.9:
        print('{} kişisi boy kilo endeksine göre obezite.'.format(name))
      else:
        print('{} kişisi boy kilo endeksine göre obezite.'.format(name))


      