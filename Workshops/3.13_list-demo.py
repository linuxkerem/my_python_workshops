#bmw mercedes opel mazda elemanlarına sahip liste oluşturunuz
#liste kaç elemanlıdır X
#listenin ilk ve son elemanı nedir X
#mazda değerini toyota ile değiştirinn (!)
#mercedes listenin bir elemanı mıdır ? 
#listenin -2 indikesinde ki değer nedir ?
#listenin ilk 3 elemanını alın
#listenin son 2 elemanı yerine toyoa ve renault değerleni ekleyin
#listenin üzerine audi ve enissan değerlerini ekleyin
#listenin son elemanını silin
#liste elemanları nı tersten yazdırın

 liste=['Bmw','Mercedes','Opel','Mazda']

 soru='Mercedes' in liste

 print(len(liste))

print('Listenin ilk elemanı: '+liste[0]+'\n'+'Listenin son elemanı: '+liste[3])

 print(liste[-2])

 liste[-1]='Toyota'

 liste=liste[0:3]

 liste[-2:]=['Toyoa','Renault']
 liste=liste + ['Audi','Nissan']
 del liste[-1]

 liste=liste[::-1]

 print(liste)  

 print(soru)

studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

#Liste elemanlarını ekrana yazdırınız

print('Birinci öğrenci: {a}\nİkinci Öğrenci: {b}\nÜçüncü Öğrenci: {c}'.format(a=studentA,b=studentB,c=studentC))

#ortalama heasplayan bi program yapınız

print('{a} {b} Adlı öğrenci {c} yaşında ve not ortalaması {d}'.format(a=studentA[0],b=studentA[1],c=2019-studentA[2],d=(studentA[3][0]+studentA[3][1]+studentA[3][2]/3)))

