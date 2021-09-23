""""

  1 - Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

  Müsteri adı
  Müsteri soyaıd
  Müsteri ad + soyad
  Müşteri cinsiyet
  müşteri tc kimlik not
  müşteri doğum yılı
  müşteri adres bilgisi
  müşteri yaşı
"""
k="kadın"
e="erkek"
b="bilinmiyor"
musteriadi="Uğur"
musterisoyadi="Çetin"
musteriadsoyad=musteriadi+" "+musterisoyadi
mustericinsiyet=b
musteriTcKimlik="216548972"
musteridogumyili=1912
musteriadres="evevevev"
musteriyasi=2021-musteridogumyili
print("Müşterimiz hakkında bilgiler")
print("Müşteri Doğum Tarihi: "+ str(musteridogumyili))
print("Müşteri yaşı: "+ str(musteriyasi))
print("Müşteri Adı Ve Soyadı "+ musteriadsoyad) 
print("Müşteri Cinsiyet "+mustericinsiyet)
print("Müşteri TC Kimlik Numarası "+musteriTcKimlik)
print("Müşteri adresi: "+musteriadres)
""""  
    2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
      
      Sipariş 1 => 110  TL
      Sipariş 2 => 11005 TL 
      Sipariş 3 => 356.95 TL    
"""
order1=110
order2=11005
order3=356.95
total=order1+order2+order3
print("Total; ", total)