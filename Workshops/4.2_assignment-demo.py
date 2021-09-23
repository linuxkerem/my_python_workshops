x,y,z=2,5,10

numbers=1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ? 
a=input('Birinci sayıyı giriniz: ')
b=input('İkinci sayıyı giriniz: ')
toplam=x+y+z
a=int(a)
b=int(b)
toplam=int(toplam)
print('Sonucunuz: ',((a*b)-toplam))

# 2- y'nin x'e kalansız bölümünü hesaplayınız
d=y//x
print(d)

# 3- (x,y,z) toplamının mod 3'ü nedir ? 
result=(x+y+z)%3
print(result)

# 4- y'nin x. kuvvetini hesaplayınız
result= y**x
print(result)

# 5- x, *y,z=numbers işlemine göre z'nin küpü kaçtır ? 
x,*y,z=numbers
result=z**3
print(result)

# 6- x,*y,z=numbers işlemine göre y nin değerleri toplamı kaçtır ? 
x,*y,z=numbers
result=y[0]+y[1]+y[2]
print(result)