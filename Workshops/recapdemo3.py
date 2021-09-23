# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:36:06 2021

@author: mrtke
"""

# 2,3,5,7,11,13
sayi=int(input('Sayı giriniz: '))
asal='asaldır.'
for x in range(2,sayi):
    if sayi % x == 0:
        asal='asal değildir.'
        break

print('{} sayısı {}'.format(sayi, asal))

        
