# ogrenciler={
#   '120':{
#     'ad':'Ali',
#     'soyad':'demir',
#     'telefon':'532 022012',
#   },
#   '240':{
#     'ad':'Ugur',
#     'soyad':'Cetin',
#     'telefon':'5058752356',
#   },
#   '125':{
#     'ad':'kerem',
#     'soyad':'izmir',
#     'telefon':'896655656',  
#   },
# }

ogrenciler ={}

number=input('ogrenci no: ')
name=input('ogrenci name: ')
surname=input('ogrenci soyad: ')
phone=input('phone giriniz: ')

# ogrenciler[number]={
#   'ad': name,
#   'soyad': surname,
#   'phone':phone,

# }

ogrenciler.update({
    number:{
      'ad':name,
      'soyad':surname,
      'telefon':phone,
    }
})

# print(ogrenciler)

print('*'*50)


ogrNo=input('öğrenci no:')
ogrenci=ogrenciler[ogrNo]
 
print('Aradığınız {a} nolu ogrencinin adi {b}, soyadı {c}, numarası ise {d} dir.'.format(a=ogrNo,b=ogrenci['ad'],c=ogrenci['soyad'],d=ogrenci['telefon']))