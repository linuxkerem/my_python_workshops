# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 01:37:23 2021

@author: mrtke
"""
a=float(input('Birinci sayıyı giriniz: '))
b=float(input('İkinci sayıyı griniz: '))
if a>b:
    print('{} sayısı {} sayısından büyüktür.'.format(a,b))
elif a<b:
    print('{} sayısı {} sayısından büyüktür.'.format(b,a))
elif a==b:
    print('Girdiğiniz sayılar eşit.')
else:
    print('Hatalı giriş.')
