# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:51:10 2021

@author: mrtke
"""
class math():
    def topla(sayi1,sayi2): 
        print('\nToplama işlemi sonucu:' ,sayi1+sayi2)
    def cikar(sayi1,sayi2):
        print('\nÇıkrma işlemi sonucu:' ,sayi1-sayi2)
    def bol(sayi1,sayi2):
        print('\nBölme işlemi sonucu:' ,sayi1/sayi2)
    def carp(sayi1,sayi2):
        print('\nÇarpma işlemi sonucu:' ,sayi1*sayi2)
i=1
while i>0:
    print('\n1- Topla\n2- Çıkar\n3- Böl\n4- Çarp\n0-Çıkış')
    d=input('Operasyon ? : ')
    if d=='1':
        sayi1=int(input('Lütfen birinci sayıyı giriniz: '))
        sayi2=int(input('Lütfen ikinci sayıyı giriniz: '))
        math.topla(sayi1, sayi2)
        continue
    elif d=='2':
        sayi1=int(input('Lütfen birinci sayıyı giriniz: '))
        sayi2=int(input('Lütfen ikinci sayıyı giriniz: '))
        math.cikar(sayi1, sayi2)
        continue
    elif d=='3':
        sayi1=int(input('Lütfen birinci sayıyı giriniz: '))
        sayi2=int(input('Lütfen ikinci sayıyı giriniz: '))
        math.bol(sayi1, sayi2)
        continue
    elif d=='4':
        sayi1=int(input('Lütfen birinci sayıyı giriniz: '))
        sayi2=int(input('Lütfen ikinci sayıyı giriniz: '))
        math.carp(sayi1, sayi2)  
        continue
    elif d=='0':
        print('\nUygulamamı Kullandığın için teşekkür ederim.')
        break
            
        
    
    