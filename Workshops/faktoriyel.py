# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:28:58 2021

@author: mrtke
"""
sayi=int(input('Faktöriyelini almak istediğiniz sayıyı giriniz: '))
sonuc=1
# def faktoriyel(a):
#     a*(a-1)


for x in range(1,sayi+1):
    sonuc=sonuc*x

print(sonuc)

