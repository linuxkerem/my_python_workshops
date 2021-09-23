names=['ali','yagmur','hakan','deniz']
years=[1998,2000,1998,1987]

#1-cenk ismini listenin sonuna ekleyiniz.
names.insert(4,"cenk")
#2-sena değernini listenin başına ekleyiniz
names.insert(0,'sena')
#3-deniz ismini listeden siliniz
# names.remove('deniz')
#4-deniz isminin indeksi nedir
index=names.index('deniz')
print(index)
#5-ali listenin bir elemanı mıdır
soru='ali' in names
#6-liste elemanlarını ters çevirin
names.reverse()
#7-liste elemanlarını alfabetik olarak yazın
names.sort()
#8-years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
#9-str="shevrolet,dacia" karakter dizisini listeye çeviriniz.
str="Chevrolet,Dacia"
result=str.split(',')
print(str)

#10- years dizisinin  en buyuk ve en kucuk elemani nedir 
enbuuk=max(years)
enkucuk=min(years)

#11- years dizinde kaç tane 1998 değeri vardır ? 
years=years.count('1998')

#12- years listesinin tüm elemanlarını siliniz
years.clear()

#13- kullanıcıdan aldığınız 3 tane marka bilgisini bir listede saklayınız
markalar= []
marka= input('marka: ')
markalar.append(marka)
marka= input('marka: ')
markalar.append(marka)
marka= input('marka: ')
markalar.append(marka)

print('Listeniz: ',markalar)


print(names)
print(years)
print(soru)
print(enbuuk)
print(enkucuk)