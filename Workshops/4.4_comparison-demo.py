
# 1- Girilen 2 sayıdan hangisi büyüktür ? 

a=(input('İlk sayıyı giriniz: '))
b=(input('İkinci sayıyı giriniz: '))

if a>b:
  print('İlk sayı ikinci sayıdan daha büyük.')
else:
  print('İkinci sayı ilk sayıdan daha büyük')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 üstünde ise geçtin değilse kaldın yazdırın.

vize1=int(input('Birinci vize notunuzu giriniz: '))
vize2=int(input('İkinci vize notunuzu giriniz.'))
final=int(input('Final notunuzu giriniz: '))
ortalama= ((vize1+vize2)*0.6)+(final*0.4)
print(ortalama)
if ortalama>=50:
  print('Geçtiniz.')
else:
  print('Kaldınız.')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

sayı=int(input('Sayınızı giriniz: '))
result=sayı%2
if result>=1:
  print('Sayınız tekdir.')
else:
  print('Sayınız çiftdir.')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

data=int(input('Sayınızı giriniz: '))
if data<0 :
  print('Sayınız negatiftir.')
else:
  print('Sayınız pozitiftir.')

# 5- Parola ve email bilgisini siteyip doğrulugunu kontrol ediniz. 
#           (email:teteho007@gmail.com parola:merhababen123 )

mail=(input('Mail adresinizi giriniz: '))
password=(input('Şifrenizi girinzi: '))
result=(mail=='teteho007@gmail.com')

if (result>=True):
  print('Mail adresiniz doğru.')
else:
  print('Mail adresiniz yanlış.')


result2=(password=='merhababen123')


if (result2>=True):
  print('Şifreniz doğru.')
else:
  print('Şifreniz yanlış.')

